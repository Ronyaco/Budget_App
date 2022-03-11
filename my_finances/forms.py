from django import forms
from datetime import date

from my_finances.models import Income

class DateInput(forms.DateInput):
    input_type = 'date'


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['name','value','date','category','repetitive','repetition_interval','repetition_time','details','user_id', 'comment_char', 'comment_text' ]



       # widgets = {
        #    'date' : DateInput()
        #}

    value = forms.DecimalField(initial=0)
    date = forms.DateField(widget = DateInput, initial = date.today())
    category = forms.ChoiceField(choices=Income.IncomeTypes.choices, initial=4)
    repetitive = forms.BooleanField(required=False)
    repetition_interval = forms.ChoiceField(choices=Income.RepetitionInterval.choices, initial=1)
    repetition_time = forms.IntegerField(initial = 0)
    details = forms.CharField(max_length=64)
    comment_char = forms.CharField(max_length=255, required=False)
    comment_text = forms.CharField(required=False, widget = forms.Textarea)
