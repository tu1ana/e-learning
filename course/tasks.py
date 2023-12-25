from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from course.models import Subscription


@shared_task
def send_course_update(pk):
    """ Функция отправки рассылкы уведомлений об обновлении материалов курса пользователям """
    email_list = []
    subbed_course_list = Subscription.objects.filter(course=pk)

    for obj in subbed_course_list:
        email_list.append(obj.student.email)

    send_mail(
        subject='Обновление курса',
        message='Посмотрите, что нового в курсе!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=email_list
    )
