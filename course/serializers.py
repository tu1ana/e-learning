from rest_framework import serializers
from rest_framework.fields import IntegerField, SerializerMethodField

from course.models import Course, Lesson, Payment


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    # lesson_count = IntegerField()
    lesson_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = ('name', 'description', 'lesson_count')

    def get_lesson_count(self, instance):
        return instance.lessons.all().count()


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_list = SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_list(self, instance):
        return LessonSerializer(Lesson.objects.filter(course=instance), many=True).data


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
