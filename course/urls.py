from django.urls import path
from rest_framework.routers import SimpleRouter

from course.apps import CourseConfig
from course.views import *

app_name = CourseConfig.name

router = SimpleRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lessons/', LessonListAPIView.as_view()),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view()),
    path('lessons/create/', LessonCreateAPIView.as_view()),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view()),
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view()),

    path('payment/', PaymentListAPIView.as_view())
] + router.urls
