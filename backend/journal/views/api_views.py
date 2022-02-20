from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from journal import models
from journal import serializers


# Create your views here.
class TaskListView(ListCreateAPIView):
    """
    List all tasks, create a new task
    """
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, destroy a task
    """
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class TaskStateListView(ListCreateAPIView):
    """
    List all task types, create a new task state
    """
    queryset = models.TaskState.objects.all()
    serializer_class = serializers.TaskStateSerializer


class TaskStateDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, destroy a task-state
    """
    queryset = models.TaskState.objects.all()
    serializer_class = serializers.TaskStateSerializer


class EventListView(ListCreateAPIView):
    """
    List all events, create a new event
    """
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


class EventDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, destroy an event
    """
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


class NoteListView(ListCreateAPIView):
    """
    List all events, create a new note
    """
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer


class NoteDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, destroy a note
    """
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer


class JournalCollectionListView(ListCreateAPIView):
    """
    List all events, create a new note
    """
    queryset = models.JournalCollection.objects.all()
    serializer_class = serializers.JournalCollectionSerializer


class JournalCollectionDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, destroy a note
    """
    queryset = models.JournalCollection.objects.all()
    serializer_class = serializers.JournalCollectionSerializer
