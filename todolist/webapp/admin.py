from django.contrib import admin
from webapp.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'deadline']
    list_filter = ['status']
    search_fields = ['title']
    exclude = []


admin.site.register(Task, TaskAdmin)