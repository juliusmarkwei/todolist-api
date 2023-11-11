from rest_framework import generics
from todolist.models import Task, UserProfile
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny


class CreateTaskView(generics.ListCreateAPIView):
    queryset = Task.taskobjects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ListTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
