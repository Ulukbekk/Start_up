# Generated by Django 3.2.7 on 2021-12-06 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20211206_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='condition',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='managerblank',
            name='condition',
            field=models.ForeignKey(blank=True, default=[0], null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.condition'),
        ),
        migrations.AlterField(
            model_name='managerblank',
            name='status',
            field=models.ForeignKey(blank=True, default=[0], null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.status'),
        ),
    ]
