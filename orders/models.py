from django.db import models

from orders.validators import validate_file_extension
from users.models import Account, Client


class ManagerBlank(models.Model):
    STATUS_CHOICES = (
        ('Обычный', 'Обычный'),
        ('Срочный', 'Срочный')
    )

    CONDITION_CHOICES = (
        ('Не начато', 'Не начато'),
        ('В процессе', 'В процессе'),
        ('Завершено', 'Завершено'),
        ('Отменено', 'Отменено'),
        ('На расмотрении', 'На расмотрении'),
    )

    WORKER_CHOICES = (
        ('Менеджер', 'Менеджер'),
        ('Дизайнер', 'Дизайнер'),
        ('Печать', 'Печать'),
        ('Станок', 'Станок'),
        ('Цех', 'Цех'),
        ('Цех и Печать', 'Цех и Печать'),
        ('Поставщик', 'Поставщик'),
    )

    ORDER_CHOICES = (
        ('Банер', 'Банер'),
        ('Вывезка', 'Вывезка'),
        ('Самоклейка', 'Самоклейка'),
        ('Фото-бумага', 'Фото-бумага'),
        ('Постер', 'Постер'),
        ('Буклетница', 'Буклетница'),
        ('Другое', 'Другое'),
    )

    files = models.FileField(upload_to='files/%Y/%m/%d', validators=[validate_file_extension], blank=True, null=True, verbose_name='Файл')
    title = models.CharField(max_length=50, verbose_name='Название', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL,
                               blank=True, null=True, verbose_name='Клиент')
    status = models.CharField(choices=STATUS_CHOICES, default='Обычный',
                               max_length=20, null=True, blank=True, verbose_name='Статус')
    price = models.FloatField(verbose_name='Цена')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(blank=True, null=True, verbose_name='Дедлайн')
    author = models.ForeignKey(Account, on_delete=models.SET_NULL,
                               blank=True, null=True)
    condition = models.CharField(choices=CONDITION_CHOICES, default='Не начато',
                                  max_length=20, blank=True, null=True, verbose_name='Состояние')
    worker = models.CharField(choices=WORKER_CHOICES, max_length=20,
                               blank=True, null=True, verbose_name='Отправить')
    order = models.CharField(choices=ORDER_CHOICES, max_length=20,
                              blank=True, null=True, verbose_name='Тип заказа')
    print = models.BooleanField(default=False)
    design = models.BooleanField(default=False)
    machine = models.BooleanField(default=False)

    def __str__(self):
        return self.title
