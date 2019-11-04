from django.shortcuts import render

from django.views.generic import ListView
from .models import Task

# Create your views here.
class TodoListView(ListView):
    model = Task
    template_name = "todo/index.html"
    
index = TodoListView.as_view()