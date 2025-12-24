from rest_framework.views import View
from rest_framework import viewsets
from todo.models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .paginations import Pagination
from rest_framework import filters

class TaskViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    pagination_class = Pagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['task']

    # Show tasks only for the user who created them 
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            # Assumes YourModel has a ForeignKey to the User model named 'owner'
            return Task.objects.filter(author=user)
        return Task.objects.none() 