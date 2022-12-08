from django.contrib import admin
from django.urls import path, include
from .views import Create, Home

urlpatterns = [
    path('', Create, name='create'),
    path('<str:token>', Home, name="Home"),


]