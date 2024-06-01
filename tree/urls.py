from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.show_tree_view, name='home'),
    path('populate', views.populate_db_view, name='populate_db'),
    path('progress/', views.progress_view, name='progress'),
    path('', views.show_hierarchy, name='show_hierarchy'),
    path('get_subordinates/<int:employee_id>/', views.get_subordinates, name='get_subordinates'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/edit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('employees/add/', views.employee_add, name='employee_add'),

]
