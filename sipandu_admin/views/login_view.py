from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

def login_index(request):
    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')

        user = authenticate(username=user_email, password=user_password)
        if user is not None:
            if user.is_active:  # Perhatikan penggunaan user.is_active
                login(request, user)
                return redirect('sipandu_admin:admin_index') 
            else:
                # Akun tidak aktif
                messages.error(request, 'Akun tidak aktif.')
        else:
            # Login tidak valid
            messages.error(request, 'Email atau kata sandi salah.')

    return render(request, 'admin/login/login.html')  # Ganti 'admin/login/login.html' dengan nama template halaman login


# Halaman untuk logout
def logout_views(request):
    logout(request)
    return redirect('sipandu_admin:admin_index')  # Ganti 'login' dengan nama fungsi login Anda