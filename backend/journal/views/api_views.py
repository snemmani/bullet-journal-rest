from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from journal import models
from journal import serializers
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class TaskListView(ListCreateAPIView):
    """
    List all tasks, create a new task
    """
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes =  (IsAuthenticated,)


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, destroy a task
    """
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes =  (IsAuthenticated,)


class TaskStateListView(ListCreateAPIView):
    """
    List all task types, create a new task state
    """
    queryset = models.TaskState.objects.all()
    serializer_class = serializers.TaskStateSerializer
    permission_classes =  (IsAuthenticated,)


class TaskStateDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, destroy a task-state
    """
    queryset = models.TaskState.objects.all()
    serializer_class = serializers.TaskStateSerializer
    permission_classes =  (IsAuthenticated,)


class EventListView(ListCreateAPIView):
    """
    List all events, create a new event
    """
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    permission_classes =  (IsAuthenticated,)


class EventDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, destroy an event
    """
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    permission_classes =  (IsAuthenticated,)


class NoteListView(ListCreateAPIView):
    """
    List all events, create a new note
    """
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
    permission_classes =  (IsAuthenticated,)


class NoteDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, destroy a note
    """
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
    permission_classes =  (IsAuthenticated,)


class JournalCollectionListView(ListCreateAPIView):
    """
    List all events, create a new note
    """
    queryset = models.JournalCollection.objects.all()
    serializer_class = serializers.JournalCollectionSerializer
    permission_classes =  (IsAuthenticated,)


class JournalCollectionDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, destroy a note
    """
    queryset = models.JournalCollection.objects.all()
    serializer_class = serializers.JournalCollectionSerializer
    permission_classes =  (IsAuthenticated,)
