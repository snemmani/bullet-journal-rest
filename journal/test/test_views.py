from dataclasses import dataclass
from django.urls import reverse
from django.test import TestCase, Client
from rest_framework import status
from ..models import JournalCollection
from ..serializers import JournalCollectionSerializer
from django.utils import timezone
import datetime

client = Client()


class TestJournalCollectionListView(TestCase):
    """Tests module for JournalCollectionListView"""

    def setUp(self):
        JournalCollection.objects.create(name="New Collection")

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
        JournalCollection.objects.create(name="New Collection")

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

