from django.shortcuts import render, get_object_or_404
from .models import Department, Session, Result

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

    SELECT ?fname ?lname ?email ?research ?designation
    WHERE {
            ?x nit:fname ?fname.
			?x nit:lname ?lname.
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

def results(request):
    return render(request, 'department/results.html')

def display(request):
    dept_P = request.GET['dept']
    session_P = request.GET['session']
    regno_P = request.GET['regno']
    sem_P = request.GET['sem']

    dep = get_object_or_404(Department, Name=dept_P)
    session = get_object_or_404(Session, Start=session_P, Department= dep)
    result = get_object_or_404(Result, Session=session, Department=dep, Semester=sem_P)

    rdfextras.registerplugins()
    g=rdflib.Graph()
    g.parse(result.Result_file)
    S = """
    PREFIX nit: <http://nitdgp.ac.in/>

    SELECT ?fname ?lname ?roll ?regno ?cgpa ?sgpa ?BT501LG ?BT502LG ?BT503LG ?OELG ?BT551LG ?BT552LG ?CH581LG
    WHERE {
            ?x nit:fname ?fname.
            ?x nit:lname ?lname.
            ?x nit:regno """+"'"+regno_P+"'"+""".
            ?x nit:roll ?roll.
            ?x nit:regno ?regno.
            ?x nit:cgpa ?cgpa.
            ?x nit:sgpa ?sgpa.
            ?x nit:BT501LG ?BT501LG.
            ?x nit:BT502LG ?BT502LG.
            ?x nit:BT503LG ?BT503LG.
            ?x nit:OELG ?OELG.
            ?x nit:BT551LG ?BT551LG.
            ?x nit:BT552LG ?BT552LG.
            ?x nit:CH581LG ?CH581LG
        }
    """
    res1 = g.query(S)

    context = { 'dep' : dep,
                'res1' : res1,
                'session' : session,
                'sem' : sem_P,
     }

    return render(request, 'department/display.html',context)
