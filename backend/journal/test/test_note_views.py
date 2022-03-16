import json
import os

from django.conf import settings
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from django.contrib.auth.models import User

from ..models import JournalCollection, Note
from ..serializers import NoteSerializer

client = Client()
user = User(first_name="A", last_name="B", email="123@abc.com")
user_password = "123"
user.set_password(user_password)

with open(os.path.join(settings.BASE_DIR, 'journal', 'test', 'payloads.json'), 'r') as payloads_handle:
    payloads = json.load(payloads_handle)

class TestNoteListView(TestCase):
    """Test module for NoteListView"""
    
    def setUp(self):
        user.save()
        client.login(username=user.username, password=user_password)
        JournalCollection.objects.create(name="Collection 1", user=user)
    
    def test_post(self):
        payload = payloads.get("note_list").get("test_post_basic")
        client.login(username=user.email, password=user.password)
        response = client.post(reverse('note_list'), data=payload, content_type="application/json")
        data = Note.objects.get(pk=1)
        serializer = NoteSerializer(data)
        assert serializer.data == response.data
        assert response.status_code == status.HTTP_201_CREATED

    def test_get(self):
        response = client.get(reverse('note_list'))
        data = Note.objects.all()
        serializer = NoteSerializer(data, many=True)
        assert serializer.data == response.data
        assert response.status_code == status.HTTP_200_OK

class TestNoteDetailView(TestCase):
    """Tests module to test EventDetailView"""

    def setUp(self):
        user.save()
        client.login(username=user.username, password=user_password)
        collection = JournalCollection.objects.create(name="Collection 1", user=user)
        Note.objects.create(description="Watch Big Bang Theory", collection=collection, user=user)

    def test_get_put_delete(self):
        # Test get
        response = client.get(reverse('note_detail', args=[1]))
        data = Note.objects.get(pk=1)
        serializer = NoteSerializer(data)
        assert serializer.data == response.data
        assert response.status_code == status.HTTP_200_OK

        # Test with recurrence set to null
        payload = payloads.get("note_detail").get("test_put")
        response = client.put(
            reverse('note_detail', args=[1]), 
            data=payload,
            content_type='application/json'
        )

        assert response.data.get('description') == payload.get('description')
        assert response.status_code == status.HTTP_200_OK

        # Delete the note
        response = client.delete(reverse('note_detail', args=[1]))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert len(Note.objects.all()) == 0

            
