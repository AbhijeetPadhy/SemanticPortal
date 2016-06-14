from django.contrib import admin
from .models import Department, Session, Result

# Register your models here.
admin.site.register(Department)
admin.site.register(Session)
admin.site.register(Result)
