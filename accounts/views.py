from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import SignUpForm

# Create your views here.
def register(request):
    form = SignUpForm() 

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully')
            user.refresh_from_db()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)



def login_view(request):
    context = {'form': forms}
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    return redirect('accounts:login')


