import datetime
import json
import os

from django.conf import settings
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status

from ..models import JournalCollection, Event
from ..serializers import EventSerializer

client = Client()

with open(os.path.join(settings.BASE_DIR, 'journal', 'test', 'payloads.json'), 'r') as payloads_handle:
    payloads = json.load(payloads_handle)

class TestEventListView(TestCase):
    """Test module for EventListView"""
    
    def setUp(self):
        collection = JournalCollection.objects.create(name="Collection 1")
        duration = datetime.timedelta(days=1, hours=2)
        Event.objects.create(description="Meet Sheldon Cooper about the empty apartment", collection=collection, recurrence=duration, number_of_recurrences=2)
        

    def test_get(self):
        response = client.get(reverse('event_list'))
        data = Event.objects.all()
        serializer = EventSerializer(data, many=True)
        assert serializer.data == response.data
        assert response.status_code == status.HTTP_200_OK
    
    def test_post(self):
        payload = payloads.get("event_list").get("test_post_basic")
        response = client.post(reverse('event_list'), data=payload, content_type="application/json")
        data = Event.objects.get(pk=2)
        serializer = EventSerializer(data)
        assert serializer.data == response.data
        assert response.status_code == status.HTTP_201_CREATED

class TestEventDetailView(TestCase):
    """Tests module to test EventDetailView"""

    def setUp(self):
        collection = JournalCollection.objects.create(name="Collection 1")
        duration = datetime.timedelta(days=1, hours=2)
        Event.objects.create(description="Watch Big Bang Theory", date=timezone.now(), collection=collection, recurrence=duration)

    def test_get_put_delete(self):
        # Test get
        response = client.get(reverse('event_detail', args=[1]))
        data = Event.objects.get(pk=1)
        serializer = EventSerializer(data)
        assert serializer.data == response.data
        assert response.status_code == status.HTTP_200_OK

        # Test with recurrence set to null
        payload = payloads.get("event_detail").get("test_with_recurrence_false")
        response = client.put(
            reverse('event_detail', args=[1]), 
            data=payload,
            content_type='application/json'
        )

        assert response.data.get('recurrence') == payload.get('recurrence')
        assert not response.data.get('number_of_recurrences')
        
        assert response.data.get('description') == payload.get("description")
        assert response.status_code == status.HTTP_200_OK

        # Test with recurrence and no of rec set
        payload = payloads.get("event_detail").get("test_recurrence_true")
        response = client.put(
            reverse('event_detail', args=[1]), 
            data=payload,
            content_type='application/json'
        )

        old_recurrence = payload.get('recurrence')

        assert response.data.get('recurrence') == payload.get('recurrence')
        assert response.data.get('number_of_recurrences') == payload.get('number_of_recurrences')
        assert response.status_code == status.HTTP_200_OK

        # Change only no of recurrences
        payload = payloads.get("event_detail").get("test_recurrence_already_true_and_no_of_recurrence_changed")
        response = client.put(
            reverse('event_detail', args=[1]), 
            data=payload,
            content_type='application/json'
        )
        assert response.data.get('recurrence') == old_recurrence
        assert response.data.get('number_of_recurrences') == payload.get("number_of_recurrences")
        assert response.status_code == status.HTTP_200_OK


        # Delete the event
        response = client.delete(reverse('event_detail', args=[1]))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert len(Event.objects.all()) == 0

            
