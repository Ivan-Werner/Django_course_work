from django.db import models

from users.models import User


class Message(models.Model):
    topic = models.CharField(max_length=100, verbose_name='Тема сообщения')
    links = models.TextField(verbose_name='Текст сообщения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания сообщения')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meddages', blank=True, null=True,
                              verbose_name='Владелец')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.topic
