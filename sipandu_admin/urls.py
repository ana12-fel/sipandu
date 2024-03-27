from django.urls import path, include
from .views import base_views
from django.contrib.auth import views as auth_views


app_name = 'sipandu_admin'
urlpatterns = [
    path('', base_views.admin_index, name='admin_index'),

]