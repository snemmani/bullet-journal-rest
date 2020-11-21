from django.db import models
from django.db.models import CASCADE

# Create your models here.
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
