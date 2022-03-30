from django.contrib import admin
from organization.models import Employee, Designation, Department, Team, EmployeeDetail

# Register your models here.
admin.site.register(Employee)
admin.site.register(Designation)
admin.site.register(Department)
admin.site.register(Team)
admin.site.register(EmployeeDetail)