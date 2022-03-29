from django.db import models


# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return self.department_name


class Team(models.Model):
    team_name = models.CharField(max_length=100, null=True, unique=True)
    department_name = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name


class Designation(models.Model):
    employee_designation = models.CharField(max_length=100, null=True, unique=True)
    team_name = models.ManyToManyField(Team)

    def __str__(self):
        return self.employee_designation


class Employee(models.Model):
    employee_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=120, null=True, unique=True)
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_name
