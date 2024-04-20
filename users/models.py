from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULL_PARAM


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(upload_to='media/avatars/',**NULL_PARAM, verbose_name='avatar')
    number_tel = models.CharField(max_length=11, unique=True, **NULL_PARAM, verbose_name='telephone_number', help_text="Введите номер телефона")
    country = models.CharField(max_length=12, **NULL_PARAM, verbose_name='country', help_text="Введите страну")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email