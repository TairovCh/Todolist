from django.contrib import admin
from webapp.models import Task, StatusTask, TypeTask

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'status', "create_time", 'update_time']
    list_filter = ['status']
    search_fields = ['summary']
    exclude = []


admin.site.register(Task, TaskAdmin)

class StatusTaskAdmin(admin.ModelAdmin):
    list_display: ['title']

admin.site.register(StatusTask, StatusTaskAdmin)

class TypeTaskAdmin(admin.ModelAdmin):
    list_display: ['title']

admin.site.register(TypeTask, TypeTaskAdmin)