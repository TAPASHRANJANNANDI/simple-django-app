from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
  path ('', views.index, name='index'),
  path ('about/', views.about, name='about'),
  path ('contact/', views.contact, name='contact'),
  path ('add_student/', views.add_student, name='add_student'),
  path ('delete_student/<str:rollno>/', views.delete_student, name='delete_student'),
  path ('update_student/<str:rollno>/', views.update_student, name='update_student'),
  path ('search/', views.search, name='search'),
]
