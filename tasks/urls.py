from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_task, name='create_task'),  # HOME PAGE = Create Task
    path('list/', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/<int:pk>/update/', views.update_task, name='update_task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
]
