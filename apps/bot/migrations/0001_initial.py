# Generated by Django 5.0.6 on 2024-08-14 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('token', models.CharField(max_length=100)),
                ('folder', models.CharField(max_length=100)),
                ('temperature', models.FloatField(default=0.7, verbose_name='Температорура чуствительности ассистента')),
                ('max_tokens', models.IntegerField(default=200, verbose_name='Максимальное количество токенов')),
                ('role', models.TextField(default='Ассистент', verbose_name='Описание роли ассистента')),
            ],
            options={
                'verbose_name': 'Ассистент',
                'verbose_name_plural': 'Ассистенты',
            },
        ),
        migrations.CreateModel(
            name='TypeGPT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GroupBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя телеграмм бота')),
                ('description', models.TextField(verbose_name='Описание телеграмм бота')),
                ('token', models.CharField(max_length=200, verbose_name='Токен телеграмм бота')),
                ('group_id', models.CharField(max_length=200, verbose_name='id группы в телеграмме, к которой поключен бот')),
                ('active', models.BooleanField(default=True, verbose_name='Признак активации бота')),
                ('assistant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_bot', to='bot.assistant', verbose_name='Ассистент')),
            ],
            options={
                'verbose_name': 'Телеграмм бот',
                'verbose_name_plural': 'Телеграмм боты',
                'ordering': ['-pk'],
            },
        ),
        migrations.AddField(
            model_name='assistant',
            name='type_gpt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assistant', to='bot.typegpt', verbose_name='Тип ассистента'),
        ),
    ]
