from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class GroupBot(models.Model):
    """
        Телеграмм бот, имеющий статус администратора в группе телеграмм
    """
    name = models.CharField(max_length=100,
                            verbose_name='Имя телеграмм бота')
    description = models.TextField(verbose_name='Описание телеграмм бота')
    token = models.CharField(max_length=200,
                             verbose_name='Токен телеграмм бота')
    group_id = models.CharField(
        max_length=200,
        verbose_name='id группы в телеграмме, к которой поключен бот')
    active = models.BooleanField(verbose_name='Признак активации бота',
                                 default=True)

    def __str__(self):
        return f'{self.name} - active: {self.active}'

    class Meta:
        verbose_name = 'Телеграмм бот'
        verbose_name_plural = 'Телеграмм боты'
        ordering = ['-pk']
