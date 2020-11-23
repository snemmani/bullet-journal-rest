from rest_framework import serializers
from . import models


class TaskSerializer(serializers.Serializer):
    """A task/to-do item in Bullet Journal"""
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=250)
    task_state = serializers.PrimaryKeyRelatedField(queryset=models.TaskState.objects.all())
    due_date = serializers.DateTimeField(required=False)
    collection = serializers.PrimaryKeyRelatedField(queryset=models.JournalCollection.objects.all(), required=False)
    recurrence = serializers.DurationField()
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    future_log = serializers.BooleanField()

    def update(self, instance: models.Task, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.recurrence = validated_data.get('recurrence', instance.recurrence)
        instance.future_log = validated_data.get('future_log', instance.future_log)
        instance.collection = validated_data.get('collection', instance.collection)
        instance.task_state = validated_data.get('task_state', instance.task_state)
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


class JournalCollectionSerializer(serializers.Serializer):
    """A journal page is a collection in the bullet journal"""
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=10)
    calendar_day = serializers.DateField()  # If this is null, the page might be a collection
    tasks = TaskSerializer(many=True)
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
