from django.contrib import admin 
from django.urls import path 
from SIH import views
urlpatterns = {
    path('',views.index),
}