from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import models
from . import serializers


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
    List all task types, create a new task type
    """
    queryset = models.TaskState.objects.all()
    serializer_class = serializers.TaskStateSerializer
