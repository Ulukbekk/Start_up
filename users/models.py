from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.position


class Account(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, blank=True, null=True)


class Client(models.Model):

    STATUS_CHOICES = (
        ('Юр.лицо', 'Юр.лицо'),
        ('Физ.лицо', 'Физ.лицо'),
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    organization = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    org_phone = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS_CHOICES,  blank=True, null=False, max_length=20)
    amount_orders = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name


