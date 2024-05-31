from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.show_tree, name='home'),
    path('populate', views.populate_db, name='populate_db'),
]
