from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import CreateTask
# Create your views here.

class TaskListview(ListView):
    model = Task
    paginate_by = 10
    context_object_name = 'tasks'
    ordering = 'id'

class TaskCreateView(CreateView):
    model = Task
    form_class = CreateTask
    success_url = '/home/task/'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = CreateTask
    success_url = '/home/task/'

class TaskDeleteview(DeleteView):
    model = Task
    success_url = '/home/task/'