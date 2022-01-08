from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    POSITION_CHOICES = (
        ('Менеджер', 'Менеджер'),
        ('Дизайнер', 'Дизайнер'),
        ('Печать', 'Печать'),
        ('Станок', 'Станок'),
        ('Цех', 'Цех'),
        ('Цех и Печать', 'Цех и Печать'),
        ('Поставщик', 'Поставщик'),
    )
    first_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='Фамилия')
    email = models.EmailField(unique=True, blank=True, null=True, verbose_name='Почта')
    phone = models.CharField(max_length=30, unique=True, blank=True, null=True, verbose_name='Номер телефона')
    position = models.CharField(choices=POSITION_CHOICES, max_length=20, blank=True, null=True, verbose_name='Должность')


class Client(models.Model):

    STATUS_CHOICES = (
        ('Юр.лицо', 'Юр.лицо'),
        ('Физ.лицо', 'Физ.лицо'),
    )

    first_name = models.CharField(max_length=20, unique=True, verbose_name='Имя')
    last_name = models.CharField(max_length=20, blank=True,null=True, verbose_name='Фамилия')
    organization = models.CharField(max_length=50, blank=True, null=True, verbose_name='Организация')
    adress = models.CharField(max_length=50, blank=True, null=True, verbose_name='Адрес')
    IDN = models.CharField(max_length=50, blank=True, null=True, verbose_name='ИНН')
    UGNS = models.CharField(max_length=50, blank=True, null=True, verbose_name='УГНС')
    bank = models.CharField(max_length=50, blank=True, null=True, verbose_name='Банк')
    payment_account = models.CharField(max_length=50, blank=True, null=True, verbose_name='Расчтный-счет')
    BIK = models.CharField(max_length=50, blank=True, null=True, verbose_name='БИК')
    phone = models.CharField(max_length=50, verbose_name='Номер')
    status = models.CharField(choices=STATUS_CHOICES,  blank=True, null=False, max_length=20, verbose_name='Статус')
    amount_orders = models.IntegerField(default=0, verbose_name='Кол-во заказов')

    def __str__(self):
        return self.first_name