from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('logout/', views.logout_user, name='logout_user' ),
    path('register/', views.register_user, name='register_user' ),
    path('delete_project/<str:pk>/', views.delete_project, name='delete_project'),
    path('tasks/<str:pk>/', views.tasks, name='tasks'),

]
