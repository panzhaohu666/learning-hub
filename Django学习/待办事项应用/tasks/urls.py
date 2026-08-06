from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('toggle/<int:pk>/', views.task_toggle, name='task_toggle'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('clear-completed/', views.task_clear_completed, name='task_clear_completed'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
