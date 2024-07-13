
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    confirmation_code = models.CharField(
        max_length=25, editable=True, blank=True,
        unique=True, verbose_name='Код подтверждения email')
    phone = models.CharField(max_length=25, blank=True)
    middle_name = models.CharField(max_length=150, blank=True)
    t_nick = models.CharField(max_length=150, blank=True,
                              verbose_name='Telegram nickname')
    foto = models.ImageField(upload_to='media/users/', blank=True)

    def __str__(self):
        return f'{self.username}: {self.full_name}'

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name} '

    class Meta:
        ordering = ['-pk']
