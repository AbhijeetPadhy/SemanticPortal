from django.shortcuts import render, get_object_or_404
from .models import Department

#for rdf
import rdflib
import rdflib.graph as g
import rdfextras

# Create your views here.
def index(request):
    all_departments = Department.objects.all()
    context = { 'all_departments' : all_departments }
    return render(request, 'department/index.html', context)

def detail(request, department_Name):
    dep = get_object_or_404(Department, Name=department_Name)
    rdfextras.registerplugins()
    g=rdflib.Graph()
    g.parse(dep.Professor_file)
    res1 = g.query("""
    PREFIX nit: <http://semanticportal/department/Biotechnology/prof/>

    SELECT ?name ?email ?research ?designation
    WHERE {
            ?x nit:name ?name.
            ?x nit:email ?email.
            ?x nit:designation ?designation.
            ?x nit:research ?research
        }
    """)

    context = { 'dep' : dep,
                'res1' : res1,
     }
    return render(request, 'department/detail.html', context)
