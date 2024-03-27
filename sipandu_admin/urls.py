from django.urls import path, include
from .views import base_views,account_views
from django.contrib.auth import views as auth_views


app_name = 'sipandu_admin'
urlpatterns = [
    path('', base_views.admin_index, name='admin_index'),
    path('login/', account_views.login_index, name='login_index'),

]