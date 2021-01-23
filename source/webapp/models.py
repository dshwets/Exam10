from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class Messages(models.Model):
    sender: AbstractUser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                             related_name='messages_sender', verbose_name='Пользователь')
    reciver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                related_name='messages_reciver', verbose_name='Пользователь')
    message_text = models.TextField(max_length=400, verbose_name='Текст сообщения')

    def __str__(self):
        return str(self.pk) + "'s message"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
