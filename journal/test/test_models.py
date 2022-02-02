from django.db import IntegrityError
from django.test import TestCase
from ..models import TaskState, Task, Event, Note, JournalCollection
from django.utils import timezone

class TaskStateTest(TestCase):
    """Test module for TastState"""

    def setUp(self):
        TaskState.objects.create(
            name="Active"
        )

    def test_object_creation(self):
        assert len(TaskState.objects.all()) == 1
        state = TaskState.objects.get(pk=1).name
        assert  state.name == "Active"
        assert str(state) == "Active"


class TaskTest(TestCase):
    """Test module for Task"""

    def setUp(self):
        collection = JournalCollection.objects.create(name="Today")
        state = TaskState.objects.create(name="Active")
        Task.objects.create(description="Test task", task_state=state, collection=collection)

    def test_object_creation_updation(self):
        assert len(Task.objects.all()) == 1
        task = Task.objects.get(pk=1)
        assert task.description == "Test task"
        assert str(task) == "Test task"
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


class EventTest(TestCase):
    """Test module for Event"""

    def setUp(self):
        collection = JournalCollection.objects.create(name="Test")
        Event.objects.create(description="Simple event", date=timezone.now(), collection=collection)

    def test_object_creation(self):
        assert len(Event.objects.all()) == 1
        assert str(Event.objects.get(pk=1)) == "Simple event"


class NoteTest(TestCase):
    """Test module for Note"""

    def setUp(self):
        collection = JournalCollection.objects.create(name="Test")
        Note.objects.create(description="Note", collection=collection)

    def test_object_creation(self):
        assert len(Note.objects.all()) == 1
        assert str(Note.objects.get(pk=1)) == "Note"


class JournalCollectionTest(TestCase):
    """Test module for JournalCollection"""

    def setUp(self):
        JournalCollection.objects.create(name="Test")

    def test_object_creation(self):
        assert len(JournalCollection.objects.all()) == 1
        assert str(JournalCollection.objects.get(pk=1)) == "Test"
    