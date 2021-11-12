from django.db import models

from users.models import Account, Client


class Status(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status


class Condition(models.Model):
    condition = models.CharField(max_length=20)

    def __str__(self):
        return self.condition


class Worker(models.Model):
    worker = models.CharField(max_length=20)

    def __str__(self):
        return self.worker


class Order(models.Model):
    order = models.CharField(max_length=100)

    def __str__(self):
        return self.order


class ManagerBlank(models.Model):
    files = models.FileField(upload_to='files/', blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.SET_NULL,
                               blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL,
                                 blank=True, null=True,)
    price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    author = models.ForeignKey(Account, on_delete=models.SET_NULL,
                               blank=True, null=True)
    condition = models.ForeignKey(Condition, on_delete=models.SET_NULL,
                                 blank=True, null=True)
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL,
                                 blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,
                                 blank=True, null=True)
    print = models.BooleanField(default=False)
    design = models.BooleanField(default=False)
    machine = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Order_file(models.Model):
    order = models.ForeignKey(ManagerBlank, null=True, on_delete=models.SET_NULL)
    files = models.FileField(upload_to='files/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.order.title + 'files'