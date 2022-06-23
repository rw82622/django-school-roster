from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_staff/', views.list_staff, name='list_staff'),
    path("list_staff/staff_detail/<int:employee_id>/", views.staff_detail, name="staff_detail"),
    path('list_students/', views.list_students, name='list_students'),
    path("list_students/student_detail/<int:student_id>/", views.student_detail, name="student_detail")
]