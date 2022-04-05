from django.db import models


# Create your models here.
class Team(models.Model):
    team = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField('Employee', related_name='team_members')

    def __str__(self):
        return self.team


class Department(models.Model):
    department = models.CharField(max_length=100, unique=True)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.department


class Designation(models.Model):
    designation = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.designation


# class Employee(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=120, unique=True)
#     team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
#     designation = models.ForeignKey(Designation, null=True, on_delete=models.CASCADE)
#     department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name