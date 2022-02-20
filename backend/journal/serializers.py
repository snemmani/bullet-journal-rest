from rest_framework import serializers
from . import models
import datetime


class TaskSerializer(serializers.Serializer):
    """A task/to-do item in Bullet Journal"""
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=250)
    task_state = serializers.PrimaryKeyRelatedField(many=False, queryset=models.TaskState.objects.all())
    due_date = serializers.DateTimeField(required=False)
    collection = serializers.PrimaryKeyRelatedField(many=False, queryset=models.JournalCollection.objects.all())
    recurrence = serializers.DurationField(required=False)
    number_of_recurrences = serializers.IntegerField(required=False)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    future_log = serializers.BooleanField(required=False)

    def update(self, instance: models.Task, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.future_log = validated_data.get('future_log', instance.future_log)
        instance.collection = validated_data.get('collection', instance.collection)
        instance.task_state = validated_data.get('task_state', instance.task_state)

        # If the task is future logged, it cannot recur
        if 'future_log' in validated_data:
            if validated_data['future_log']:
                instance.recurrence = None
                instance.number_of_recurrences = None
            else:
                instance.recurrence = validated_data.get('recurrence', instance.recurrence)
                instance.number_of_recurrences = validated_data.get('number_of_recurrences', instance.number_of_recurrences)
        elif instance.future_log: 
            instance.recurrence = None
            instance.number_of_recurrences = None
        else:
            instance.recurrence = validated_data.get('recurrence', instance.recurrence)
            instance.number_of_recurrences = validated_data.get('number_of_recurrences', instance.number_of_recurrences)
        
        instance.save()
        return instance

    def create(self, validated_data):
        return models.Task.objects.create(**validated_data)

    class Meta:
        model = models.Task
        fields = "__all__"


class TaskStateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

    def create(self, validated_data):
        return models.TaskState.objects.create(**validated_data)

    class Meta:
        model = models.TaskState
        fields = '__all__'

class EventSerializer(serializers.Serializer):
    """An Event in Bullet Journal"""
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=250)
    date = serializers.DateTimeField(required=False)
    collection = serializers.PrimaryKeyRelatedField(queryset=models.JournalCollection.objects.all(), many=False)
    recurrence = serializers.DurationField(required=False)
    number_of_recurrences = serializers.IntegerField(required=False)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.date)
        instance.collection = validated_data.get('collection', instance.collection)

        if 'recurrence' in validated_data:
            instance.recurrence = validated_data.get('recurrence', instance.recurrence)
            if validated_data.get('recurrence') > datetime.timedelta(seconds=0):
                instance.number_of_recurrences = validated_data.get('number_of_recurrences', instance.number_of_recurrences)
            elif instance.recurrence:
                instance.number_of_recurrences = validated_data.get('number_of_recurrences', instance.number_of_recurrences)
            else:
                instance.number_of_recurrences = 0
        else:
            if instance.recurrence:
                instance.number_of_recurrences = validated_data.get('number_of_recurrences', instance.number_of_recurrences)
            else:
                instance.number_of_recurrences = 0
                
        instance.save()
        return instance

    def create(self, validated_data):
        return models.Event.objects.create(**validated_data)

    class Meta:
        model = models.Event
        fields = '__all__'


class NoteSerializer(serializers.Serializer):
    """A Note in Bullet Journal"""
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=250)
    collection = serializers.PrimaryKeyRelatedField(many=False, queryset=models.JournalCollection.objects.all())
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.collection = validated_data.get('collection', instance.collection)
        instance.save()
        return instance

    def create(self, validated_data):
        return models.Note.objects.create(**validated_data)

    class Meta:
        model = models.Note
        fields = '__all__'


class JournalCollectionSerializer(serializers.Serializer):
    """A journal page is a collection in the bullet journal"""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    calendar_day = serializers.DateField(required=False)  # If this is null, the page might be a collection
    tasks = TaskSerializer(required=False, many=True, read_only=True)
    events = EventSerializer(required=False, many=True, read_only=True)
    notes = NoteSerializer(required=False, many=True, read_only=True)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.calendar_day = validated_data.get("calendar_day", instance.calendar_day)
        instance.created = validated_data.get("created", instance.created)
        instance.updated = validated_data.get("updated", instance.updated)
        instance.save()
        return instance

    def create(self, validated_data):
        return models.JournalCollection.objects.create(**validated_data)

    class Meta:
        model = models.TaskState
        fields = '__all__'
