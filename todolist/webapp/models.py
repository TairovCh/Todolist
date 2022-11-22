from django.db import models


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
    status = models.ForeignKey('webapp.StatusTask', on_delete=models.PROTECT, related_name='tasks', verbose_name='Статус')
    type_task = models.ManyToManyField('webapp.TypeTask', related_name='tasks', blank=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    def __str__(self):
        return f"{self.pk}. {self.summary[:15]}"

