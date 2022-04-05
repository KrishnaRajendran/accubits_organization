from rest_framework import serializers
from organization.models import Employee, Team, Department, Designation


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):
    # watchlist = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Team
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"

class DesignationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Designation
        fields = "__all__"