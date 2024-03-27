from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect user to dashboard or any other page upon successful login
            return redirect('dashboard')
        else:
            # Handle invalid login credentials
            return render(request, 'admin/login/account/login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'admin/login/account/login.html')
