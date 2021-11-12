from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title or ' '


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='sub_category', blank=True, null=True)
    title = models.CharField(max_length=50)

    class MPTTMeta:
        order_insertion_by = ['title']

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

    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                    related_name='material_category', blank=True, null=True)
    size = models.FloatField(default=0)
    amount = models.IntegerField(default=0)
    color = models.CharField(choices=COLOR_CHOICES, blank=True, null=True, max_length=20)
    shade = models.CharField(max_length=10, default=0)

    def __str__(self):
        return self.category.__str__()