from django import forms
from task_tracker.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Client_Name', 'Job_Description', 'Reocurring', 'Phone_Number', 'Job_address', 'Frequency', 'Case_Manager', 'Contractor', 'Assign_to', 'Last_Booking_Date', 'New_Booking_Date', 'Time_confirmed', 'Status', 'Comments']

        widgets = {
            'Client_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Job_Description': forms.TextInput(attrs={'class': 'form-control'}),
            'Reocurring': forms.Select(choices=[('Yes', 'Yes'), ('No', 'No')], attrs={'class': 'form-control'}),
            'Phone_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'Job_address': forms.TextInput(attrs={'class': 'form-control'}),
            'Frequency': forms.TextInput(attrs={'class': 'form-control'}),
            'Case_Manager': forms.TextInput(attrs={'class': 'form-control'}),
            'Contractor': forms.TextInput(attrs={'class': 'form-control'}),
            'Assign_to': forms.TextInput(attrs={'class': 'form-control'}),
            'Last_Booking_Date': forms.TextInput(attrs={'class': 'form-control'}),
            'New_Booking_Date': forms.TextInput(attrs={'class': 'form-control'}),
            'Time_confirmed': forms.Select(choices=[('Yes', 'Yes'), ('No', 'No')], attrs={'class': 'form-control'}),
            'Status': forms.TextInput(attrs={'class': 'form-control'}),
            'Comments': forms.TextInput(attrs={'class': 'form-control'}),
        }
