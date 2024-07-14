from django.db import models

from apps.core.models import User


class Event(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=2000, verbose_name='Описание')
    place = models.CharField(max_length=255)
    start = models.DateTimeField(verbose_name='Начало события')
    stop = models.DateTimeField(verbose_name='Окончание события')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    foto = models.ImageField(upload_to='media/events/', blank=True)
    guest = models.ManyToManyField(User, blank=True, through="EventGuest",
                                   through_fields=("event", "guest"),
                                   verbose_name='Участвники события',)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['-pk']


class EventGuest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT,
                              verbose_name='Событие')
    guest = models.ForeignKey(User, on_delete=models.PROTECT,
                              verbose_name='Участник')

    def __str__(self):
        return f'{self.event.name}: {self.guest.full_name} '

    class Meta:
        verbose_name = 'Приглашенные'
        verbose_name_plural = 'Приглашенные'
        ordering = ['-pk']


class SamplePeriod(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT,
                              verbose_name='Событие')
    start = models.TimeField(verbose_name='Начало выборки')
    stop = models.TimeField(verbose_name='Окончание выборки')

    def __str__(self):
        return f'{self.event.name}: {self.start} - {self.stop} '

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['-pk']
