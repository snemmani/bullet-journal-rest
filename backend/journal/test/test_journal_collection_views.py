import datetime
import json
import os

from django.conf import settings
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from django.contrib.auth.models import User

from ..models import JournalCollection
from ..serializers import JournalCollectionSerializer

client = Client()
user = User(first_name="A", last_name="B", email="123@abc.com")
user_password = "123"
user.set_password(user_password)

with open(os.path.join(settings.BASE_DIR, 'journal', 'test', 'payloads.json'), 'r') as payloads_handle:
    payloads = json.load(payloads_handle)

class TestJournalCollectionListView(TestCase):
    """Tests module for JournalCollectionListView"""

    def setUp(self):
        user.save()
        client.login(username=user.username, password=user_password)
        JournalCollection.objects.create(name="New Collection", user=user)

    def test_get(self):
        collections = JournalCollection.objects.all()
        serializer = JournalCollectionSerializer(collections, many=True)
        response = client.get(reverse('collection_list'))
        assert response.data == serializer.data
        assert response.status_code == status.HTTP_200_OK
    
    def test_post(self):
        response = client.post(reverse('collection_list'), data=dict(name="Test Collection", calendar_day="2022-01-29"))
        collection = JournalCollection.objects.get(pk=2)
        serializer = JournalCollectionSerializer(collection)
        assert response.data == serializer.data
        assert response.status_code == status.HTTP_201_CREATED

class TestJournalCollectionDetailView(TestCase):
    """Tests module for JournalCollectionDetailView"""
    
    def setUp(self):
        user.save()
        client.login(username=user.username, password=user_password)
        JournalCollection.objects.create(name="New Collection", user=user)


    def test_get_put_delete(self):
        collection = JournalCollection.objects.get(pk=1)
        serializer = JournalCollectionSerializer(collection)
        response = client.get(reverse('collection_detail', args=[1]))
        assert response.data == serializer.data
        assert response.status_code == status.HTTP_200_OK

        # Test put
        response = client.put(reverse('collection_detail', args=[1]), content_type="application/json", data=dict(name="Another collection", calendar_day="2022-02-21"))
        collection = JournalCollection.objects.get(pk=1)
        assert collection.name == "Another collection"
        assert collection.calendar_day == datetime.date(2022, 2, 21)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == 1

        # Test delete
        response = client.delete(reverse('collection_detail', args=[1]))
        assert len(JournalCollection.objects.all()) == 0
        assert response.status_code == status.HTTP_204_NO_CONTENT