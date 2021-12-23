from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название категории')

    def __str__(self):
        return self.title


class Material(models.Model):
    COLOR_CHOICES = (
        ('Белый', 'Белый'),
        ('Черный', 'Черный'),
        ('Серый', 'Серый'),
        ('Красный', 'Красный'),
        ('Розовый', 'Розовый'),
        ('Фиолетовый', 'Фиолетовый'),
        ('Оранжевый', 'Оранжевый'),
        ('Зеленый', 'Зеленый'),
        ('Синий', 'Синий'),
        ('Голубой', 'Голубой'),
        ('Бирюзовый', 'Бирюзовый'),
        ('Желтый', 'Желтый'),
        ('Коричневый', 'Коричневый'),
    )

    category_choice = (
        ('Акрил', 'Акрил'),
        ('Форекс', 'Форекс'),
        ('Самоклеящаяся пленка.', 'Самоклеящаяся пленка.'),
        ('Светодиоды', 'Светодиоды'),
        ('Метал ', 'Метал'),
        ('Другое', 'Другое'),
    )
    category = models.CharField(max_length=50, blank=True, null=True, choices=category_choice, verbose_name='Категория')
    title = models.CharField(default=' ', max_length=100, blank=True, null=True)
    remainder = models.FloatField(default=0, verbose_name='Остаток')
    amount = models.IntegerField(default=0, verbose_name='Количество')
    date_created = models.DateTimeField(auto_now_add=True)
    color = models.CharField(choices=COLOR_CHOICES, blank=True, null=True, max_length=20, verbose_name='Цвет')
    shade = models.CharField(max_length=10, verbose_name='Оттенок', blank=True, null=True)

    def __str__(self):
        return self.title