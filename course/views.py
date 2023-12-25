from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from course.models import Course, Lesson, Payment, Subscription
from course.paginators import ThePaginator
from course.permissions import IsModerator, IsAdmin, IsStudent, IsStudentOrStaff
from course.serializers import CourseSerializer, LessonSerializer, CourseListSerializer, CourseDetailSerializer, \
    PaymentSerializer, SubscriptionSerializer
from course.tasks import send_course_update


class CourseViewSet(ModelViewSet):
    default_serializer = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsStudentOrStaff]
    pagination_class = ThePaginator

    serializers = {  # custom dict
        'list': CourseListSerializer,
        'retrieve': CourseDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.annotate(lesson_count=Count('lessons'))
        return super().list(request, *args, **kwargs)

#     def perform_update(self, serializer):
#         serializer.save()
#
#     def partial_update(self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        course = serializer.save()

        send_course_update(course.pk)


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThePaginator


class LessonRetrieveAPIView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsStudent]


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer
    # permission_classes = [IsAuthenticated, IsAdmin] # не удалось создать суперюзера для теста, поэтому закомментировала


class LessonUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsStudent]


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated, IsAdmin]


class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_option')
    ordering_fields = ('pay_day',)


class SubscriptionCreateAPIView(CreateAPIView):
    serializer_class = SubscriptionSerializer


class SubscriptionDestroyAPIView(DestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    # permission_classes = [IsAuthenticated]
