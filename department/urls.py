from django.conf.urls import url
from . import views

app_name = 'department'

urlpatterns = [
    # /department/
    url(r'^$', views.index,name='index'),

    # /department/results/
    url(r'^results/$', views.results, name='results'),

    # /department/results/display
    url(r'^results/display$', views.display, name='display'),

    # /department/department_Name/
    url(r'^(?P<department_Name>[A-Za-z]+)/$', views.detail, name='detail'),

    # /department/department_Name/session/session_Start
    url(r'^(?P<department_Name>[A-Za-z]+)/session/(?P<session_Start>[0-9][0-9][0-9][0-9])/$', views.session, name='session'),
]
