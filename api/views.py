from rest_framework import generics
from todolist.models import Task, EndUsers
from .serializers import TaskSerializer, EndUsersSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from rest_framework.response import Response


class CreateTaskView(generics.ListCreateAPIView):
    queryset = Task.taskobjects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


class ListTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ListUsersView(generics.ListAPIView):
    queryset = EndUsers.objects.all()
    serializer_class = EndUsersSerializer
    permission_classes = [IsAdminUser]
