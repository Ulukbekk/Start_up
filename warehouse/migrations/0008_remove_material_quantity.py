# Generated by Django 3.2.7 on 2021-12-28 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0007_auto_20211228_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='quantity',
        ),
    ]