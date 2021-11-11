from django.urls import path
from  . import  views

app_name = 'website'

urlpatterns = [
    path('', views.base, name='base'),
    path('dashboard', views.dashboard, name='dashboard'),
      
    
]
