from django.contrib import admin
from webapp.models import Task, StatusTask, TypeTask, ProjectTask

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'status', "create_time", 'update_time', 'project_task']
    list_filter = ['status']
    search_fields = ['summary']
    exclude = []


admin.site.register(Task, TaskAdmin)

class StatusTaskAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(StatusTask, StatusTaskAdmin)

class TypeTaskAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(TypeTask, TypeTaskAdmin)


class ProjectTaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'start_date', 'end_date']

admin.site.register(ProjectTask, ProjectTaskAdmin)