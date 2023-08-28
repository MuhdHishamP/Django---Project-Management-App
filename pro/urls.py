from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('logout/', views.logout_user, name='logout_user' ),
    path('register/', views.register_user, name='register_user' ),
    path('update_project/<str:pk>/', views.update_project, name='update_project'),
    path('delete_project/<str:pk>/', views.delete_project, name='delete_project'),
    path('task/<str:pk>/', views.task, name='task'),
]
