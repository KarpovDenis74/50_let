from django.db import models
from django.contrib.auth import get_user_model
from apps.bot.tasks import start_bot, stop_bot

User = get_user_model()


class GroupBot(models.Model):
    """
        Телеграмм бот, имеющий статус администратора в группе телеграмм
        Бот привязан к событию и обслуживает его
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

    def save(self, force_insert=False, force_update=False,
             using=None, update_fields=None):
        new_bot = self.pk is None
        if new_bot:
            super().save(force_insert, force_update, using, update_fields)
            start_bot.delay_on_commit(self.pk)
            return None
        else:
            current_bot_active = GroupBot.objects.get(pk=self.pk).active
            print(f'{current_bot_active=}')
            if not current_bot_active and self.active:
                print('Здесь')
                super().save(force_insert, force_update, using, update_fields)
                start_bot.delay_on_commit(self.pk)
                return None
            elif current_bot_active and not self.active:
                print('Здесь 2')
                stop_bot.delay_on_commit(self.pk)
                super().save(force_insert, force_update, using, update_fields)
                return None
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = 'Телеграмм бот'
        verbose_name_plural = 'Телеграмм боты'
        ordering = ['-pk']
