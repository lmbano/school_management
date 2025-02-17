"""
URL configuration for school_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from  blessings_junior_school import views_old

urlpatterns = [
    # Student URLs
    path('blessings_junior_school/', views_old.student_list, name='student_list'),
    path('blessings_junior_school/create/', views_old.student_create, name='student_create'),
    path('blessings_junior_school/update/<int:student_id>/', views_old.student_update, name='student_update'),
    path('blessings_junior_school/delete/<int:student_id>/', views_old.student_delete, name='student_delete'),
    
    # Contact URLs
    path('blessings_junior_school/<int:student_id>/contacts/', views_old.contact_list, name='contact_list'),
    path('blessings_junior_school/<int:student_id>/contact/create/', views_old.contact_create, name='contact_create'),
    path('blessings_junior_school/<int:student_id>/contact/update/<int:contact_id>/', views_old.contact_update, name='contact_update'),
    path('blessings_junior_school/<int:student_id>/contact/delete/<int:contact_id>/', views_old.contact_delete, name='contact_delete'),

    # Medical Record URLs
    path('blessings_junior_school/<int:student_id>/medical_records/', views_old.medical_record_list, name='medical_record_list'),
    path('blessings_junior_school/<int:student_id>/medical_record/create/', views_old.medical_record_create, name='medical_record_create'),
    path('blessings_junior_school/<int:student_id>/medical_record/update/<int:medical_record_id>/', views_old.medical_record_update, name='medical_record_update'),
    path('blessings_junior_school/<int:student_id>/medical_record/delete/<int:medical_record_id>/', views_old.medical_record_delete, name='medical_record_delete'),
    
    # Other models...
]
