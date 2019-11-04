from django.shortcuts import render
from django.urls import reverse

from django.views.generic import ListView, CreateView
from .models import Task

# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = "todo/index.html"
    
index = TaskListView.as_view()

class TaskCreateView(CreateView):
    model = Task
    fields = ("title", "content", "status")
    template_name = "todo/new.html"

new = TaskCreateView.as_view()