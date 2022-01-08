# Generated by Django 3.2.7 on 2021-12-25 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0005_alter_material_shade'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='material',
            name='color',
        ),
        migrations.RemoveField(
            model_name='material',
            name='shade',
        ),
        migrations.AlterField(
            model_name='material',
            name='category',
            field=models.CharField(blank=True, choices=[('Листовой', 'Листовой'), ('Рулон', 'Рулон'), ('Электро', 'Электро'), ('Металл ', 'Металл'), ('Расходный', 'Расходный'), ('Другое', 'Другое')], max_length=50, null=True, verbose_name='Категория'),
        ),
    ]
