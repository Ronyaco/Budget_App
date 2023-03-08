from django.db import models

class Task(models.Model):
    client_name = models.CharField(max_length=100)
    job_description = models.CharField(max_length=100)
    reoccurring = models.CharField(max_length=100,null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    job_address = models.CharField(max_length=100, null=True, blank=True)  
    frequency = models.CharField(max_length=100)
    case_manager = models.CharField(max_length=100)
    contractor = models.CharField(max_length=100)
    assign_to = models.CharField(max_length=100)
    last_booking_date = models.CharField(null=True, blank=True,max_length=100)
    new_booking_date = models.CharField(null=True, blank=True,max_length=100)
    time_confirmed = models.CharField(null=True, blank=True,max_length=100)
    status = models.CharField(max_length=100)
    comments = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.job_description
