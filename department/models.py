from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Department(models.Model):
    Name = models.CharField(max_length = 250)
    Professor_file = models.FileField()

    def __str__(self):
        return self.Name

class Session(models.Model):
    Start = models.IntegerField()
    End = models.IntegerField()
    Student_file = models.FileField()
    Department = models.ForeignKey(Department, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.Start) + "-" + str(self.End) + "-" + str(self.Department)

class Result(models.Model):
    Session = models.ForeignKey(Session, on_delete = models.CASCADE)
    Department = models.ForeignKey(Department, on_delete = models.CASCADE)
    Semester = models.CharField(max_length = 3)
    Result_file = models.FileField()

    def __str__(self):
        return str(self.Session) + "-" + str(self.Department) + "-" + str(self.Semester)
