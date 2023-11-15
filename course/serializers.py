from rest_framework import serializers
from rest_framework.fields import IntegerField

from course.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    lesson_count = IntegerField()

    class Meta:
        model = Course
        fields = ('name', 'description', 'lesson_count')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
