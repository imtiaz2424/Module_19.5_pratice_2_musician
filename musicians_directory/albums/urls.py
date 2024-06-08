from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('add/', views.add_album, name='add_album'),
    path('add/', views.AddPostCreateView.as_view(), name='add_album'),   
]