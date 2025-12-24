from django.urls import path, include
from . import views

app_name = 'todo'

urlpatterns = [
    path('task/', views.TaskCreateView.as_view(), name='task-list'),
    path('task/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', views.TaskDeleteview.as_view(), name='task-delete'),
    path('api/', include('todo.api.urls'))
]