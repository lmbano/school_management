# school/urls.py
from django.urls import path
from blessings_junior_school import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    # ... define other URLs as needed
]