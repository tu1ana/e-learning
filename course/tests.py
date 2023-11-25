from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory, APIClient

from course import views
from course.models import Lesson, Course
from course.views import LessonListAPIView
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.course = Course.objects.create(
            name='TestCourse'
        )
        self.lesson = Lesson.objects.create(
            name='TestLesson',
            course=self.course
        )
        self.user = User.objects.create(
            email='test@example.com'
        )

    def test_authentication(self):
        user = User.objects.create(email='test@site.com', password='1one2two')
        self.client.force_authenticate(user=user)
        user.save()

    def test_get_list(self):
        self.test_authentication()
        response = self.client.get(reverse('course:lesson_list'))
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

        # print(response.json())

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {'id': 2,
                     'link_to_vid': None,
                     'name': 'TestLesson',
                     'description': None,
                     'thumbnail': None,
                     'course': self.course.id,
                     'student': self.lesson.student_id}
                ]
            }
        )

    # def create_superuser(self, username, password, **kwargs):
    #     user = User(email=username, is_superuser=True, is_staff=True, **kwargs)
    #     user.set_password(password)
    #     user.save()

    def test_lesson_create(self):
        data = {
            'name': 'TestLessonCreate',
            'course': self.course.id,
            'link_to_vid': 'www.youtube.com',
        }
        response = self.client.post(
            reverse('course:lesson_create'),
            data=data
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )

    def test_lesson_update(self):
        data = {
            # 'id': self.lesson.id,
            'name': 'TestLessonUpdate',
            'course': self.course.id,
            'link_to_vid': 'www.youtube.com',
        }
        response = self.client.post(
            reverse('course:lesson_update', args=[self.lesson.pk]),
            data
        )

        # print(response.json)

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

        self.lesson.refresh_from_db()

    def test_lesson_delete(self):
        data = {
            'id': self.lesson.id,
            'name': 'TestLessonCreate',
            'course': self.course.id,
            'link_to_vid': 'www.youtube.com',
        }
        response = self.client.delete(
            reverse('course:lesson_delete', args=[self.lesson.id]),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_if_student_subbed_to_course(self):
        data = {
            'course': self.course.id,
            'student': self.user.id,
            'is_active': True
        }

        response = self.client.post(
            reverse('course:sub_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

# {'count': 1,
# 'next': None,
# 'previous': None,
# 'results':
# [{'id': 1,
# 'link_to_vid': None,
# 'name': 'TestLesson',
# 'description': None,
# 'thumbnail': None,
# 'course': 1,
# 'student': None}]}
