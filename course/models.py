from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    thumbnail = models.ImageField(upload_to='courses/', **NULLABLE, verbose_name='Превью изображения')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    thumbnail = models.ImageField(upload_to='lessons/', **NULLABLE, verbose_name='Превью изображения')
    link_to_vid = models.CharField(max_length=75, **NULLABLE, verbose_name='Ссылка на видео')

    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

