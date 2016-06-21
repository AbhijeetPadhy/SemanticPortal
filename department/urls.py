from django.conf.urls import url
from . import views

app_name = 'department'

urlpatterns = [
    # /department/
    url(r'^$', views.index,name='index'),

    # /department/department_Name/
    url(r'^(?P<department_Name>[A-Za-z]+)/$', views.detail, name='detail'),

    # /department/session/
    url(r'^(?P<department_Name>[A-Za-z]+)/(?P<session_Start>[0-9][0-9][0-9][0-9])/$', views.session, name='session'),
]
