from django.db import models

from orders.validators import validate_file_extension
from users.models import Account, Client
from warehouse.models import Material


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

    title = models.CharField(max_length=50, verbose_name='Название', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL,
                               blank=True, null=True, verbose_name='Клиент')
    status = models.CharField(choices=STATUS_CHOICES, default='Обычный',
                               max_length=20, null=True, blank=True, verbose_name='Статус')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(blank=True, null=True, verbose_name='Дедлайн')
    amount = models.IntegerField(blank=True, null=True, verbose_name='Кол-во')
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

    wasted_material_one = models.ForeignKey(Material, on_delete=models.SET_NULL,
                                        blank=True, null=True, verbose_name='Затраченый материал1', related_name='wasted_material_one')
    amount_wasted_material_one = models.IntegerField(default=0 , blank=True, null=True, verbose_name='Кол-во')
    wasted_material_two = models.ForeignKey(Material, on_delete=models.SET_NULL,
                                        blank=True, null=True, verbose_name='Затраченый материал2', related_name='wasted_material_two')
    amount_wasted_material_two = models.IntegerField(default=0 , blank=True, null=True, verbose_name='Кол-во')
    wasted_material_three = models.ForeignKey(Material, on_delete=models.SET_NULL,
                                        blank=True, null=True, verbose_name='Затраченый материал3', related_name='wasted_material_three')
    amount_wasted_material_three = models.IntegerField(default=0 , blank=True, null=True, verbose_name='Кол-во')
    wasted_material_four = models.ForeignKey(Material, on_delete=models.SET_NULL,
                                        blank=True, null=True, verbose_name='Затраченый материал4', related_name='wasted_material_four')
    amount_wasted_material_four = models.IntegerField(default=0 , blank=True, null=True, verbose_name='Кол-во')
    wasted_material_five = models.ForeignKey(Material, on_delete=models.SET_NULL,
                                        blank=True, null=True, verbose_name='Затраченый материал5', related_name='wasted_material_five')
    amount_wasted_material_five = models.IntegerField(default=0 , blank=True, null=True, verbose_name='Кол-во')
    wasted_material_six = models.ForeignKey(Material, on_delete=models.SET_NULL,
                                        blank=True, null=True, verbose_name='Затраченый материал6', related_name='wasted_material_six')
    amount_wasted_material_six = models.IntegerField(default=0 , blank=True, null=True, verbose_name='Кол-во')
    wasted_material_seven = models.ForeignKey(Material, on_delete=models.SET_NULL,
                                        blank=True, null=True, verbose_name='Затраченый материал7', related_name='wasted_material_seven')
    amount_wasted_material_seven = models.IntegerField(default=0 , blank=True, null=True, verbose_name='Кол-во')
    wasted_material_eight = models.ForeignKey(Material, on_delete=models.SET_NULL,
                                        blank=True, null=True, verbose_name='Затраченый материал8', related_name='wasted_material_eight')
    amount_wasted_material_eight = models.IntegerField(default=0 , blank=True, null=True, verbose_name='Кол-во')

    def __str__(self):
        return self.title


class ManagerBlankFiles(models.Model):
    order = models.ForeignKey(ManagerBlank, default=None, on_delete=models.CASCADE)
    files = models.FileField(upload_to='files/', validators=[validate_file_extension], blank=True, null=True, verbose_name='Файл')

    def __str__(self):
        return self.files