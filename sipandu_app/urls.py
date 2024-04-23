from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'sipandu'
urlpatterns = [
    path('', home.index, name='home'),
    path('identitas/', profile.identitas, name='identitas'),
    path('Visi/', profile.Visi, name='Visi'),
    path('smp/', smp.indexsmp, name='smp'),
    path('berita/', berita.beritasmp, name='berita'),
]