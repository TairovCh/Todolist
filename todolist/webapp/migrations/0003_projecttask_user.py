# Generated by Django 4.1.3 on 2022-12-23 05:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0002_alter_task_project_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttask',
            name='user',
            field=models.ManyToManyField(related_name='projecttasks', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
