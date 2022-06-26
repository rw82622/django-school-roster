from django.shortcuts import render, redirect, reverse
from .models import School, Student, Staff
from django.http import HttpResponse
import os

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
    print(student_id)
    return render(request, 'student_detail.html', my_data)

def add_student(request):
    if request.method == "POST":
        my_student = {
            'name': request.POST.get('name'),
            'age': request.POST.get('age'),
            'role': request.POST.get('role'),
            'school_id': int(request.POST.get('id')),
            'password': request.POST.get('password')
            }
        my_school.add_student(my_student)
        return redirect(reverse('list_students'))
    elif request.method == 'GET':
        return render(request, 'add_student.html')

def add_staff(request):
    if request.method == "POST":
        my_staff = {
            'name': request.POST.get('name'),
            'age': request.POST.get('age'),
            'role': request.POST.get('role'),
            'employee_id': int(request.POST.get('id')),
            'password': request.POST.get('password')
            }
        my_school.add_staff(my_staff)
        return redirect(reverse('list_staff'))
    elif request.method == 'GET':
        return render(request, 'add_staff.html')
