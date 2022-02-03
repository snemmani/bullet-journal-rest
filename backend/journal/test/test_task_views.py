import datetime
import json
import os

from django.conf import settings
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status

from ..models import JournalCollection, Task, TaskState
from ..serializers import TaskSerializer

client = Client()

with open(os.path.join(settings.BASE_DIR, 'journal', 'test', 'payloads.json'), 'r') as payloads_handle:
    payloads = json.load(payloads_handle)

class TestTaskListView(TestCase):
    """Test module for TaskListView"""
    
    def setUp(self):
        taskState = TaskState.objects.create(name="Active")
        collection = JournalCollection.objects.create(name="Collection 1")
        duration = datetime.timedelta(days=1, hours=2)
        Task.objects.create(description="Defeat Sith lords", task_state=taskState, due_date=timezone.now(), collection=collection, recurrence=duration)
        

    def test_get(self):
        response = client.get(reverse('task_list'))
        data = Task.objects.all()
        serializer = TaskSerializer(data, many=True)
        assert serializer.data == response.data
        assert response.status_code == status.HTTP_200_OK
    
    def test_post(self):
        payload = payloads.get("task_list").get("test_post_basic")
        response = client.post(reverse('task_list'), data=payload, content_type="application/json")
        data = Task.objects.get(pk=2)
        serializer = TaskSerializer(data)
        assert serializer.data == response.data
        assert response.status_code == status.HTTP_201_CREATED

class TestTaskDetailView(TestCase):
    """Tests module to test TaskDetailView"""

    def setUp(self):
        taskState = TaskState.objects.create(name="Active")
        collection = JournalCollection.objects.create(name="Collection 1")
        duration = datetime.timedelta(days=1, hours=2)
        Task.objects.create(description="Watch Big Bang Theory", task_state=taskState, due_date=timezone.now(), collection=collection, recurrence=duration)

    def test_get_put_delete(self):
        # Test get
        response = client.get(reverse('task_detail', args=[1]))
        data = Task.objects.get(pk=1)
        serializer = TaskSerializer(data)
        assert serializer.data == response.data
        assert response.status_code == status.HTTP_200_OK

        # Test put future log set to true
        payload = payloads.get("task_detail").get("test_put_regular")
        response = client.put(
            reverse('task_detail', args=[1]), 
            data=payload,
            content_type='application/json'
        )

        assert not response.data.get('recurrence')
        assert not response.data.get('number_of_recurrences')
        
        assert response.data.get('future_log')
        assert response.status_code == status.HTTP_200_OK

        # Existing future log true
        payload = payloads.get("task_detail").get("test_existing_future_log")
        response = client.put(
            reverse('task_detail', args=[1]), 
            data=payload,
            content_type='application/json'
        )

        assert not response.data.get('recurrence')
        assert not response.data.get('number_of_recurrences')
        assert response.data.get('future_log')
        assert response.status_code == status.HTTP_200_OK

        # Set future log to False and set recurrence
        payload = payloads.get("task_detail").get("test_future_log_false")
        response = client.put(
            reverse('task_detail', args=[1]), 
            data=payload,
            content_type='application/json'
        )

        assert response.data.get('recurrence') == "01:00:00"
        assert response.data.get('number_of_recurrences') == 1
        assert not response.data.get('future_log')
        assert response.status_code == status.HTTP_200_OK


        # Delete the task
        response = client.delete(reverse('task_detail', args=[1]))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert len(Task.objects.all()) == 0

            
