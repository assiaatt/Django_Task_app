from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.task_list), name='task_list'),
    path('task/<int:pk>/', login_required(views.task_detail), name='task_detail'),
    path('task/new/', login_required(views.task_create), name='task_create'),
    path('task/<int:pk>/edit/', login_required(views.task_edit), name='task_edit'),
    path('task/<int:pk>/delete/', login_required(views.task_delete), name='task_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'), 
    path('register/', views.register, name='register'),
]