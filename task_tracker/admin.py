from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from task_tracker.models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(ImportExportModelAdmin):
    pass

