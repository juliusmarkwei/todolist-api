from rest_framework import serializers
from todolist.models import Task, EndUsers


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


class EndUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndUsers
        fields = ["user", "email", "joined_date"]
