from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.show_tree_view, name='home'),
    path('populate', views.populate_db_view, name='populate_db'),
    path('progress/', views.progress_view, name='progress'),
]
