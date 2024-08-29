from rest_framework import serializers
from student.models import Passout, Branch

class DashboardBranchList(serializers.ModelSerializer):
    count = serializers.CharField(max_length = 10)
    class Meta:
        model = Branch
        fields = ['id', 'name', 'alias', 'count']

class DashboardPassoutSerializer(serializers.ModelSerializer):
    branchList = DashboardBranchList(many = True)
    class Meta:
        model = Passout
        fields = ['id', 'status', 'name','branchList']


class StudentDashboardSerializer(serializers.Serializer):
    allStudentsCount = serializers.CharField(max_length= 10)
    pursuingStudentsCount = serializers.CharField(max_length= 10)
    regularStudentsCount = serializers.CharField(max_length= 10)
    lateralStudentsCount = serializers.CharField(max_length= 10)
    regularStudentsID = serializers.CharField(max_length= 5)
    lateralStudentsID = serializers.CharField(max_length= 5)
    pursuingPassoutList = DashboardPassoutSerializer(many= True)
    regularPassoutList = DashboardPassoutSerializer(many = True)
    lateralPassoutList = DashboardPassoutSerializer(many = True)
