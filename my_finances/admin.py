from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from my_finances.models import Income, Outcome, Balance
from task_tracker.models import Task

# Register your models here.

admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'job_description', 'reoccurring', 'phone_number', 'job_address', 'frequency', 'case_manager', 'contractor', 'assign_to', 'last_booking_date', 'new_booking_date', 'time_confirmed', 'status', 'comments']


@admin.register(Income)
class IncomeAdmin(ImportExportModelAdmin):
    pass

@admin.register(Outcome)
class OutcomeAdmin(ImportExportModelAdmin):
    pass

@admin.register(Balance)
class BalanceAdmin(ImportExportModelAdmin):
    pass