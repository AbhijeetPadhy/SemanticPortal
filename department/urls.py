from django.conf.urls import url
from . import views

app_name = 'department'

urlpatterns = [
    # /department/
    url(r'^$', views.index,name='index'),
    # /department/department_Name/
    url(r'^(?P<department_Name>[A-Za-z]+)/$', views.detail, name='detail'),
]
