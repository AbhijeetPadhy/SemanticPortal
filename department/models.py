from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Department(models.Model):
    Name = models.CharField(max_length = 250)
    Professor_file = models.FileField()

class Session(models.Model):
    Start = models.IntegerField()
    End = models.IntegerField()
    Student_file = models.FileField()
    Department = models.ForeignKey(Department, on_delete = models.CASCADE)

class Result(models.Model):
    Session = models.ForeignKey(Session, on_delete = models.CASCADE)
    Department = models.ForeignKey(Department, on_delete = models.CASCADE)
    Semester = models.CharField(max_length = 3)
    Result_file = models.FileField()
