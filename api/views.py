from rest_framework import generics
from todolist.models import Task, UserProfile
from .serializers import TaskSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class CreateTaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class ListTaskView(generics.ListAPIView):
    def get_queryset(self):
        return super().get_queryset().filter(name="in progress")
