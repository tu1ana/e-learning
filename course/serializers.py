from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import IntegerField, SerializerMethodField

from course.models import Course, Lesson, Payment, Subscription
from course.services import checkout_link
from course.validators import youtube_validator


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


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
    is_subscribed = SerializerMethodField(read_only=True, source='subscription')

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_list(self, instance):
        return LessonSerializer(Lesson.objects.filter(course=instance), many=True).data

    def get_is_subscribed(self, instance):
        if instance.subscription.filter(is_active=True):
            return True
        return False


class LessonSerializer(serializers.ModelSerializer):
    link_to_vid = serializers.CharField(validators=[youtube_validator])

    class Meta:
        model = Lesson
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    checkout_link = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = '__all__'

    def get_checkout_link(self, instance):
        return checkout_link(instance)
