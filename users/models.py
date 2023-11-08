from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=150, unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='Номер телефона')
    city = models.CharField(max_length=255, **NULLABLE, verbose_name='Город')
    avatar = models.ImageField(upload_to='user_avatars/', **NULLABLE, verbose_name='Аватар')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username} ({self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


