from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    school = serializers.ReadOnlyField(source = 'school.username')  #We coudld have used CharField too
    class Meta:
        model = Student
        fields = ('name', 'age', 'std', 'school')

class SchoolSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())
    class Meta:
        model = User
        fields=('id', 'username', 'students')
