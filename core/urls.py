from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('delete-task/<str:pk>/', delete_task, name='delete-task'),
    path('update-task/<str:pk>/', update_task, name='update-task'),
    path('create-task/', create_task, name='create-task'),
]