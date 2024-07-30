# Generated by Django 5.0.6 on 2024-07-30 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_eventguest_event_guest_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampleperiod',
            name='t_start',
            field=models.DateTimeField(verbose_name='Начало выборки в чате телеграмма'),
        ),
        migrations.AlterField(
            model_name='sampleperiod',
            name='t_stop',
            field=models.DateTimeField(verbose_name='Конец выборки в чате телеграмма'),
        ),
    ]
