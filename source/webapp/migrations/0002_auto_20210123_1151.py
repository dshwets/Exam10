# Generated by Django 2.2.13 on 2021-01-23 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='reciver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_reciver', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_sender', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]