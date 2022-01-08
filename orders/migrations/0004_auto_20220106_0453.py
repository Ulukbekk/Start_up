# Generated by Django 3.2.7 on 2022-01-06 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0010_invoice'),
        ('orders', '0003_managerblank_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='managerblank',
            name='amount_wasted_material',
        ),
        migrations.RemoveField(
            model_name='managerblank',
            name='wasted_material',
        ),
        migrations.AddField(
            model_name='managerblank',
            name='amount_wasted_material_eight',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Кол-во'),
        ),
        migrations.AddField(
            model_name='managerblank',
            name='amount_wasted_material_five',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Кол-во'),
        ),
        migrations.AddField(
            model_name='managerblank',
            name='amount_wasted_material_four',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Кол-во'),
        ),
        migrations.AddField(
            model_name='managerblank',
            name='amount_wasted_material_one',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Кол-во'),
        ),
        migrations.AddField(
            model_name='managerblank',
            name='amount_wasted_material_seven',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Кол-во'),
        ),
        migrations.AddField(
            model_name='managerblank',
            name='amount_wasted_material_six',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Кол-во'),
        ),
        migrations.AddField(
            model_name='managerblank',
            name='amount_wasted_material_three',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Кол-во'),
        ),
        migrations.AddField(
            model_name='managerblank',
            name='amount_wasted_material_two',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Кол-во'),
        ),
        migrations.AddField(
            model_name='managerblank',
            name='wasted_material_eight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wasted_material_eight', to='warehouse.material', verbose_name='Затраченый материал8'),
        ),
        migrations.AddField(
            model_name='managerblank',
            name='wasted_material_five',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wasted_material_five', to='warehouse.material', verbose_name='Затраченый материал5'),
        ),
        migrations.AddField(
            model_name='managerblank',
            name='wasted_material_four',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wasted_material_four', to='warehouse.material', verbose_name='Затраченый материал4'),
        ),
        migrations.AddField(
            model_name='managerblank',
            name='wasted_material_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wasted_material_one', to='warehouse.material', verbose_name='Затраченый материал1'),
        ),
        migrations.AddField(
            model_name='managerblank',
            name='wasted_material_seven',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wasted_material_seven', to='warehouse.material', verbose_name='Затраченый материал7'),
        ),
        migrations.AddField(
            model_name='managerblank',
            name='wasted_material_six',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wasted_material_six', to='warehouse.material', verbose_name='Затраченый материал6'),
        ),
        migrations.AddField(
            model_name='managerblank',
            name='wasted_material_three',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wasted_material_three', to='warehouse.material', verbose_name='Затраченый материал3'),
        ),
        migrations.AddField(
            model_name='managerblank',
            name='wasted_material_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wasted_material_two', to='warehouse.material', verbose_name='Затраченый материал2'),
        ),
    ]