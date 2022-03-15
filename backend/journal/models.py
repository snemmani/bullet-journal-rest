from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User


class TaskState(models.Model):
    """Task States like Active/Moved/Future Logged/Canceled/Completed"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    # created = models.ForeignKey()

    def __str__(self):
        return self.name


class Task(models.Model):
    """A task/to-do item in Bullet Journal"""
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=250)
    task_state = models.ForeignKey("TaskState", related_name="task_state", on_delete=CASCADE)
    due_date = models.DateTimeField(null=True)
    collection = models.ForeignKey("JournalCollection", related_name="task_page_rel", on_delete=CASCADE)
    recurrence = models.DurationField(null=True)
    number_of_recurrences = models.IntegerField(null=True)
    user = models.ForeignKey(User, related_name="task_user_rel", on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    future_log = models.BooleanField(default=False)

    def __str__(self):
        return self.description


class Event(models.Model):
    """An Event in Bullet Journal"""
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=250)
    date = models.DateTimeField(null=True)
    collection = models.ForeignKey("JournalCollection", related_name="event_page_rel", on_delete=CASCADE)
    recurrence = models.DurationField(null=True)
    number_of_recurrences = models.IntegerField(null=True)
    user = models.ForeignKey(User, related_name="event_user_rel", on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class Note(models.Model):
    """A Note in Bullet Journal"""
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=250)
    collection = models.ForeignKey("JournalCollection", related_name="note_page_rel", on_delete=CASCADE)
    user = models.ForeignKey(User, related_name="note_user_rel", on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class JournalCollection(models.Model):
    """A journal page is a page/collection in the bullet journal"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    calendar_day = models.DateField(null=True) # If this is null, the page might be a collection
    user = models.ForeignKey(User, related_name="collection_user_rel", on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
