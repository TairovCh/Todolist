from django.db import models

TYPE_CHOICES = [('task', 'Задача'), ('bug', 'Ошибка'),  ('enhancement', 'Улучшение')]
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
# Create your models here.

class TypeTask(models.Model):
    type_task = models.CharField(max_length=25,choices=TYPE_CHOICES, default=TYPE_CHOICES[0][0], verbose_name='Тип')
    def __str__(self):
        return f"{self.pk}. {self.type_task}"

class StatusTask(models.Model):
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name='Cтaтус')
    def __str__(self):
        return f"{self.pk}. {self.status}"

class Task(models.Model):
    summary = models.CharField(max_length=60, verbose_name='Краткое описание')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Полное описание")
    status = models.ForeignKey('webapp.Task', on_delete=models.PROTECT, related_name='statuses', verbose_name='Статус')
    type_task = models.ForeignKey('webapp.Task', on_delete=models.PROTECT, related_name='type_tasks', verbose_name='Тип')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    def __str__(self):
        return f"{self.pk}. {self.title}"

