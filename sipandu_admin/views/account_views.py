from django.shortcuts import render

def login_index(request):
    return render (request, f'login/account/login.html')
# Create your views here.
