from django.db import models
from django.db.models import CASCADE

# Create your models here.
class TaskState(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Task(models.Model):
    """A task/to-do item in Bullet Journal"""
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=250)
    task_state = models.ForeignKey("TaskState", related_name="task_state", on_delete=CASCADE)
    due_date = models.DateTimeField(null=True)
    recurrance = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    future_log = models.BooleanField(default=False)


class Event(models.Model):
    """An Event in Bullet Journal"""
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=250)
    due_date = models.DateTimeField(null=True)
    recurrance = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class JournalEntryType(models.Model):
    """Entry types are basic journal item types like Task/Event/Note"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class JournalEntry(models.Model):
    """An entry is basically any item in the bullet journal, they can be of EntryType types"""
    id = models.AutoField(primary_key=True)
    entryType = models.ForeignKey("JournalEntryType", related_name="journal_entry_type", on_delete=CASCADE)
    name = models.CharField(max_length=30)
    page = models.ForeignKey("JournalPage", related_name="journal_page", on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class JournalPage(models.Model):
    """A journal page is a page/collection in the bullet journal"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    calendar_day = models.DateField(null=True) # If this is null, the page might be a collection
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Index(models.Model):
    """Index is the collection of all the pages in a Bullet Journal"""
    id = models.AutoField(primary_key=True)
    page = models.ForeignKey("JournalPage", related_name="journal_entry", on_delete=CASCADE)
    page_number = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class FutureLog(models.Model):
    id = models.AutoField(primary_key=True)
    entry = models.ForeignKey("JournalEntry", related_name="journal_entry_fl", on_delete=CASCADE)
    month = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


