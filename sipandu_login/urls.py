from django.urls import path
from .views import account_views
from django.contrib.auth import views as auth_views


app_name = 'sipandu_login'
urlpatterns = [
    path('', account_views.login_index, name='login_index'),

]