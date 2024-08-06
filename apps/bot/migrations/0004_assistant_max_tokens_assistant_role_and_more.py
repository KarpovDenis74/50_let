# Generated by Django 5.0.6 on 2024-08-06 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_groupbot_assistant'),
    ]

    operations = [
        migrations.AddField(
            model_name='assistant',
            name='max_tokens',
            field=models.IntegerField(default=200, verbose_name='Максимальное количество токенов'),
        ),
        migrations.AddField(
            model_name='assistant',
            name='role',
            field=models.TextField(default='Ассистент', verbose_name='Описание роли ассистента'),
        ),
        migrations.AddField(
            model_name='assistant',
            name='temperature',
            field=models.FloatField(default=0.7, verbose_name='Температорура чуствительности ассистента'),
        ),
    ]
