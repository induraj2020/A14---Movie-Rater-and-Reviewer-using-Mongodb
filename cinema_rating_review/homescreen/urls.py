from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='homescreen-home-1'),
    path('contactus/', views.contact ,name='contact'),


]
