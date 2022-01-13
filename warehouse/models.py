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
    receive_quantity = models.IntegerField(default='0', blank=True, null=True, verbose_name='Добавить материал')
    issue_quantity = models.IntegerField(default='0', blank=True, null=True, verbose_name='Отнять материал')
    date_created = models.DateTimeField(auto_now_add=True)
    # color = models.CharField(choices=COLOR_CHOICES, blank=True, null=True, max_length=20, verbose_name='Цвет')

    def __str__(self):
        return self.title
