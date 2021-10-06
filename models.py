from django.db import models

class Employee(models.Model):
    eno =  models.IntegerField()
    ename = models.CharField(max_length=30)
    erole = models.CharField(max_length=30)
    esalary = models.IntegerField()
    eaddress = models.CharField(max_length=100)


