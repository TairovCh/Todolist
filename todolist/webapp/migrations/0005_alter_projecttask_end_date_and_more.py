# Generated by Django 4.1.3 on 2022-12-05 22:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_projecttask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttask',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата начала'),
        ),
    ]