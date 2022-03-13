from django import forms
from datetime import date

from my_finances.models import Income, Outcome , Balance

class DateInput(forms.DateInput):
    input_type = 'date'


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['name','value','date','category','repetitive','repetition_interval','repetition_time','details', 'comment_char', 'comment_text' ]

    
    value = forms.DecimalField(initial=0)
    date = forms.DateField(widget = DateInput, initial = date.today())
    category = forms.ChoiceField(choices=Income.IncomeTypes.choices, initial=4)
    repetitive = forms.BooleanField(required=False)
    repetition_interval = forms.ChoiceField(choices=Income.RepetitionInterval.choices, initial=1)
    repetition_time = forms.IntegerField(initial = 0)
    details = forms.CharField(max_length=64)
    comment_char = forms.CharField(max_length=255, required=False)
    comment_text = forms.CharField(required=False, widget = forms.Textarea)


def save(self, commit=True):
    instance = super(IncomeForm, self).save(commit=False)
    if commit:
        instance.save()
    return instance


class OutcomeForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = ['name','value','date','category','repetition_interval','repetition_time','details' ]

  

    date = forms.DateField(widget = DateInput, initial = date.today())

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ['value', 'date', 'type', 'comments' ]

        date = forms.DateField(widget = DateInput, initial = date.today())



