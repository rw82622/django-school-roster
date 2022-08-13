from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('staff/', views.list_staff, name='list_staff'),
    path("staff/<int:employee_id>/", views.staff_detail, name="staff_detail"),
    path('students/', views.list_students, name='list_students'),
    path("students/<int:student_id>/", views.student_detail, name="student_detail"),
    path('addStudent/', views.add_student, name= 'add_student'),
    path('addStaff/', views.add_staff, name= 'add_staff')
]