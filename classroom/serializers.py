from rest_framework import serializers
from .models import Subject, Batch, Student, User, Parent, Teacher, Homework, Attendance, Notification, Timetable, Marks, Test, Remark, Request

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ("__all__")

class BatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Batch
        fields = ("__all__")
        
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ("__all__")

class ParentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parent
        fields = ("__all__")

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ("__all__")

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ("__all__")

class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = ("__all__")

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ("__all__")

class RemarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remark
        fields = ("__all__")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")


class NotifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("__all__")


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ("__all__")

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ("__all__")

class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = ("__all__")