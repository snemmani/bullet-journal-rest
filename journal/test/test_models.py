from django.db import IntegrityError
from django.test import TestCase
from ..models import TaskState, Task
from django.utils import timezone

class TaskStateTest(TestCase):
    """Test module for TastState"""

    def setUp(self):
        TaskState.objects.create(
            name="Active"
        )

    def test_object_creation(self):
        assert len(TaskState.objects.all()) == 1
        assert TaskState.objects.get(pk=1).name == "Active"


class TaskTest(TestCase):
    """Test module for Task"""

    def setUp(self):
        state = TaskState.objects.create(name="Active")
        Task.objects.create(description="Test task", task_state=state)

    def test_object_creation_updation(self):
        assert len(Task.objects.all()) == 1
        task = Task.objects.get(pk=1)
        assert task.description == "Test task"
        now_time = timezone.now()
        assert now_time > task.created
        task.description = "Test task 2"
        task.save()
        assert now_time < task.updated

    def test_object_creation_with_null_description(self):
        try:
            Task.objects.create()
            self.fail("Empty object created with null description for 'Task'")
        except IntegrityError:
            pass
    