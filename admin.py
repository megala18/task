from django.contrib import admin
from crudApp.models import Employee




class EmployeeAdmin(admin.ModelAdmin) :
    list = ['eno', 'ename', 'erole', 'esalary', 'eaddress']

admin.site.register(Employee , EmployeeAdmin)


