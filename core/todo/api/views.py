from rest_framework.views import View
from rest_framework import viewsets
from todo.models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class TaskViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            # Assumes YourModel has a ForeignKey to the User model named 'owner'
            return Task.objects.filter(author=user)
        return Task.objects.none() 