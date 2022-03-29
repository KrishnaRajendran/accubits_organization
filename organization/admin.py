from django.contrib import admin
from organization.models import Employee, Designation, Department, Team

# Register your models here.
admin.site.register(Employee)
admin.site.register(Designation)
admin.site.register(Department)
admin.site.register(Team)