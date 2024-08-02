from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Event(models.Model):
    from apps.bot.models import GroupBot
    """
        События
        имеют связь с приглашенными на событие пользователями
    """
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=2000, verbose_name='Описание')
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               verbose_name='Автор события',
                               related_name='author_event')
    bot = models.ForeignKey(GroupBot, on_delete=models.PROTECT,
                            verbose_name='Телеграмм бот, обслуживающий событие',
                            related_name='event',
                            null=True)
    place = models.CharField(max_length=255)
    start = models.DateTimeField(verbose_name='Начало события')
    stop = models.DateTimeField(verbose_name='Окончание события')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    foto = models.ImageField(upload_to='media/events/', blank=True)
    guest = models.ManyToManyField(User, blank=True,
                                   related_name='guest_event',
                                   through="EventGuest",
                                   through_fields=("event", "guest"),
                                   verbose_name='Участвники события',)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['-pk']


class EventGuest(models.Model):
    """
        Приглашенные на событие пользователи
        связь с событием и пользователями
    """
    event = models.ForeignKey(Event, on_delete=models.PROTECT,
                              verbose_name='Событие')
    guest = models.ForeignKey(User, on_delete=models.PROTECT,
                              verbose_name='Участник')

    def __str__(self):
        return f'{self.event.name}: {self.guest.full_name} '

    class Meta:
        verbose_name = 'Приглашенный на событие'
        verbose_name_plural = 'Приглашенные на событие'
        ordering = ['-pk']
        constraints = [
            models.UniqueConstraint(fields=['event', 'guest'],
                                    name='event_guest_index')
        ]


class SamplePeriod(models.Model):
    """
        Модель для хранения периодов выборки в чате телеграмма
        для конкретного события
    """
    event = models.ForeignKey(Event, on_delete=models.PROTECT,
                              verbose_name='Событие')
    t_start = models.DateTimeField(

        verbose_name='Начало выборки в чате телеграмма')
    t_stop = models.DateTimeField(

        verbose_name='Конец выборки в чате телеграмма')

    def __str__(self):
        return f'{self.event.name}: {self.t_start} - {self.t_stop} '

    class Meta:
        verbose_name = 'Период выборки'
        verbose_name_plural = 'Периоды выборки'
        ordering = ['-pk']
