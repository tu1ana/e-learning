from django.db.models import Count
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from course.models import Course, Lesson
from course.serializers import CourseSerializer, LessonSerializer, CourseListSerializer, CourseDetailSerializer


class CourseViewSet(ModelViewSet):
    default_serializer = CourseSerializer
    queryset = Course.objects.all()

    serializers = {  # custom dict
        'list': CourseListSerializer,
        'retrieve': CourseDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.annotate(lesson_count=Count('lessons'))
        return super().list(request, *args, **kwargs)


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer


class LessonUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
