from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class ProjectTask(models.Model):
    name = models.CharField(max_length=25, verbose_name = 'Название')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    start_date = models.DateField(default=timezone.now, verbose_name='Дата начала')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    user = models.ManyToManyField(get_user_model(), related_name='projecttasks', verbose_name='Пользователь')

    class Meta:
        permissions = [
            ('сan_add_user', 'Может добавлять пользователя'),
            ('сan_change_user', 'Может изменять пользователя'),
            ('сan_delete_user', 'Может удалять пользователя'),
        ]

    def __str__(self):
        return f"{self.pk}. {self.name}"


class TypeTask(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название')

    def __str__(self):
        return f"{self.pk}. {self.title}"


class StatusTask(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название')

    def __str__(self):
        return f"{self.pk}. {self.title}"


class Task(models.Model):
    summary = models.CharField(max_length=60, verbose_name='Краткое описание')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Полное описание")
    project_task = models.ForeignKey("webapp.ProjectTask", verbose_name=("Проект"), related_name='tasks', on_delete=models.CASCADE)
    status = models.ForeignKey('webapp.StatusTask', on_delete=models.PROTECT, related_name='tasks', verbose_name='Статус')
    type_task = models.ManyToManyField('webapp.TypeTask', related_name='tasks', blank=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    def __str__(self):
        return f"{self.pk}. {self.summary[:15]}"

