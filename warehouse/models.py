from django.db import models


class Material(models.Model):
    # COLOR_CHOICES = (
    #     ('Белый', 'Белый'),
    #     ('Черный', 'Черный'),
    #     ('Серый', 'Серый'),
    #     ('Красный', 'Красный'),
    #     ('Розовый', 'Розовый'),
    #     ('Фиолетовый', 'Фиолетовый'),
    #     ('Оранжевый', 'Оранжевый'),
    #     ('Зеленый', 'Зеленый'),
    #     ('Синий', 'Синий'),
    #     ('Голубой', 'Голубой'),
    #     ('Бирюзовый', 'Бирюзовый'),
    #     ('Желтый', 'Желтый'),
    #     ('Коричневый', 'Коричневый'),
    # )

    category_choice = (
        ('Листовой', 'Листовой'),
        ('Рулон', 'Рулон'),
        ('Электро', 'Электро'),
        ('Металл ', 'Металл'),
        ('Расходный', 'Расходный'),
        ('Другое', 'Другое'),
    )
    category = models.CharField(max_length=50, blank=True, null=True, choices=category_choice, verbose_name='Категория')
    title = models.CharField(default=' ', max_length=100, blank=True, null=True)
    remainder = models.FloatField(default=0, verbose_name='Остаток')
    amount = models.IntegerField(default=0, verbose_name='Количество')
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    # color = models.CharField(choices=COLOR_CHOICES, blank=True, null=True, max_length=20, verbose_name='Цвет')

    def __str__(self):
        return self.title


class Invoice(models.Model):
    comments = models.TextField(max_length=3000, default='', blank=True, null=True)
    invoice_number = models.IntegerField(blank=True, null=True)
    invoice_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    name = models.CharField('Customer Name', max_length=120, default='', blank=True, null=True)

    line_one = models.CharField('Line 1', max_length=120, default='', blank=True, null=True)
    line_one_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_one_unit_price = models.IntegerField('Unit Price (D)', default=0, blank=True, null=True)
    line_one_total_price = models.IntegerField('Line Total (D)', default=0, blank=True, null=True)

    phone_number = models.CharField(max_length=120, default='', blank=True, null=True)
    total = models.IntegerField(default='0', blank=True, null=True)
    balance = models.IntegerField(default='0', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
    paid = models.BooleanField(default=False)
    invoice_type_choice = (
        ('Receipt', 'Receipt'),
        ('Proforma Invoice', 'Proforma Invoice'),
        ('Invoice', 'Invoice'),
    )
    invoice_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=invoice_type_choice)

    def __unicode__(self):
        return self.invoice_number