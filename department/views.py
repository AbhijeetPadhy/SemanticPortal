from django.shortcuts import render, get_object_or_404
from .models import Department, Session

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
    sessions = dep.session_set.all()
    rdfextras.registerplugins()
    g=rdflib.Graph()
    g.parse(dep.Professor_file)
    res1 = g.query("""
    PREFIX nit: <http://nitdgp.ac.in/>

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
                'sessions' : sessions,
     }
    return render(request, 'department/detail.html', context)

def session(request,department_Name,session_Start):
    dep = get_object_or_404(Department, Name=department_Name)
    session = get_object_or_404(Session, Start=session_Start, Department= dep)
    rdfextras.registerplugins()
    g=rdflib.Graph()
    g.parse(session.Student_file)
    g.parse(dep.Professor_file)
    res1 = g.query("""
    PREFIX nit: <http://nitdgp.ac.in/>

    SELECT ?fname ?lname ?email ?roll ?dept ?regno ?address ?prof_fname ?prof_lname ?bgroup ?height ?weight
    WHERE {
            ?x nit:fname ?fname.
            ?x nit:lname ?lname.
            ?x nit:email ?email.
            ?x nit:roll ?roll.
            ?x nit:dept ?dept.
            ?x nit:regno ?regno.
            ?x nit:address ?address.
            ?x nit:email ?email.
            ?x nit:researchUnder ?researchUnder.
            ?x nit:bgroup ?bgroup.
            ?x nit:height ?height.
            ?x nit:weight ?weight.
            ?researchUnder nit:fname ?prof_fname.
            ?researchUnder nit:lname ?prof_lname
        }
    """)
    context = { 'dep' : dep,
                'res1' : res1,
                'session' : session,
     }
    return render(request, 'department/session.html', context)
