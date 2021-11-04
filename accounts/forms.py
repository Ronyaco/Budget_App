from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    
    
    first_name = forms.Field(widget=forms.TextInput(attrs={'class':'form-gp', 'placeholder':'First Name'}),label="")
    last_name = forms.Field(widget=forms.TextInput(attrs={'class':'form-gp', 'placeholder':'Last Name'}),label="")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-gp', 'placeholder':'Email'}),label="")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-gp', 'placeholder':'Password'}),label="")
    password2 = forms.CharField(widget=forms.PasswordInput( attrs={'class':'form-gp', 'placeholder':'Confirm Password'}),label="")


    def save(self, commit=True):
        instance = super(SignUpForm, self).save(commit=False)
        instance.username = self.cleaned_data['email']
        if commit:
            instance.save()
        return instance

