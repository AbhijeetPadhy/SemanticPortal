from django.shortcuts import render, get_object_or_404
from .models import Department

# Create your views here.
def index(request):
    all_departments = Department.objects.all()
    context = { 'all_departments' : all_departments }
    return render(request, 'department/index.html', context)

def detail(request, department_Name):
    dep = get_object_or_404(Department, Name=department_Name)
    context = { 'dep' : dep }
    return render(request, 'department/detail.html', context)
