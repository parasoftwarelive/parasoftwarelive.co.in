from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('services', views.services, name='Services'),
    path('projects', views.projects, name='Projects'),
    path('contactus', views.contactus, name='contactus')
]
