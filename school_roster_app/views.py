from django.shortcuts import render
from .models import School
from django.template import loader

my_school = School("Django School")

def index(request):
    my_data = {"school_name": my_school.name}
    template = loader.get_template('index.html')
    return render(request, "index.html", my_data)


def list_staff(request):
    pass # implement


def staff_detail(request, employee_id):
    pass # implement


def list_students(request):
    pass # implement


def student_detail(request, student_id):
    pass # implement
