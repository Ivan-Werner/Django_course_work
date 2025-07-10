from django.db import models
from users.models import User


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Имя клиента')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients', blank=True, null=True,
                              verbose_name='Владелец')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.email
