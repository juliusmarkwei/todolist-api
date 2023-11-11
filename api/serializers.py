from rest_framework import serializers
from todolist.models import Task, UserProfile


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "author",
            "category",
            "title",
            "description",
            "due_date",
            "status",
        ]


# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ["username", "email", "joined_date"]
