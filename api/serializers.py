from rest_framework import serializers
from todolist.models import Task, UserProfile
from core.settings import DATE_INPUT_FORMAT


class TaskSerializer(serializers.ModelSerializer):
    due_date = serializers.DateTimeField(required=False)
    countdown = serializers.DurationField(read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "author",
            "category",
            "title",
            "description",
            "due_date",
            "countdown",
            "status",
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["username", "email", "joined_date"]
