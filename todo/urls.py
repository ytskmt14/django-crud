from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('edit/<int:pk>', views.edit, name='edit'),
]
