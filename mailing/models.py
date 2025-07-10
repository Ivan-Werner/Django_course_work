from django.db import models

from client.models import Client
from messeges.models import Message
from users.models import User


class Mailing(models.Model):
    STATUS_CHOISE = [
        ('created', 'создана'),
        ('launched', 'запущена'),
        ('finished', 'завершена'),
    ]
    first_send_time = models.DateTimeField(blank=True, null=True, verbose_name='Начало рассылки')
    end_time = models.DateTimeField(blank=True, null=True, verbose_name='Окончание рассылки')
    status = models.CharField(max_length=30, choices=STATUS_CHOISE, default='created', verbose_name='Статус')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    client = models.ManyToManyField(Client, verbose_name='Клиенты')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mailings', blank=True, null=True, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Рассылка',
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return f'Рассылка: {self.message} {self.status}'


class MailingAttempt(models.Model):
    STATUS_CHOICE = [
        ('good', 'успешно'),
        ('not_good', 'не успешно')
    ]
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время попытки')
    status = models.CharField(max_length=30, choices=STATUS_CHOICE, verbose_name='Статус')
    server_response = models.TextField(verbose_name='Ответ сервера')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='attemts', verbose_name='Рассылка')

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'

    def __str__(self):
        return f'{self.timestamp} - {self.status}'