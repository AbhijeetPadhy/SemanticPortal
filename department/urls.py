from django.conf.urls import url
from . import views

app_name = 'department'

urlpatterns = [
    # /music/
    url(r'^$', views.index,name='index'),
]
