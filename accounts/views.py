from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe

from .forms import SignUpForm

# Create your views here.
def register(request):
    form = SignUpForm() 

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully')


    context = {'form': form}
    return render(request, 'accounts/register.html', context)



def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, mark_safe(f'You are already logged in as   <b>{request.user.username}<b>.'))
        return redirect('website:index')


    username = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me', False)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You are now logged in as {request.user.username} ')
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('website:index')    
            
        else:
            messages.error(request, 'Invalid username or password')
        
    return render(request, 'accounts/login.html', context={"username": username})




def logout_view(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('website:index')


