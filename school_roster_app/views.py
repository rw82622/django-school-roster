from django.shortcuts import render
from .models import School
# from django.template import loader

my_school = School("Django School")

def index(request):
    my_data = {"school_name": my_school.name}
    return render(request, "index.html", my_data)


def list_staff(request):
    my_data = {"staff": my_school.staff, 'school_name': my_school.name}
    return render(request, 'staff.html', my_data)


def staff_detail(request, employee_id):
    my_data = {"staff": my_school.staff, 'id': employee_id}
    return render(request, 'staff_detail.html', my_data)


def list_students(request):
    my_data = {"students": my_school.students, 'school_name': my_school.name}
    return render(request, 'students.html', my_data)


def student_detail(request, student_id):
    my_data = {"student": my_school.students, 'id': student_id}
    return render(request, 'student_detail.html', my_data)
