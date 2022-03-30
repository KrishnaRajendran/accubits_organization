from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=120, null=True, unique=True)
    # team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    # designation = models.ForeignKey(Designation, null=True, on_delete=models.CASCADE)
    # department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ", " + self.email
        # return self.name


class Team(models.Model):
    team = models.CharField(max_length=100, null=True, unique=True)
    members = models.ManyToManyField(Employee)

    def __str__(self):
        return self.team


class Department(models.Model):
    department = models.CharField(max_length=100, null=True, unique=True)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.department


class Designation(models.Model):
    designation = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return self.designation


class EmployeeDetail(models.Model):
    name = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE)
    # email = models.ForeignKey(Employee, null=True, related_name='emailID', on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, null=True, on_delete=models.SET_NULL)
    team = models.ForeignKey(Team, null=True, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.name)
