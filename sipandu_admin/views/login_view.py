from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_index(request):
    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')
        user = authenticate(request, user_email=user_email, user_password=user_password)
        if user is not None:
            if user.user_is_activate:
                login(request, user)
                # Redirect to a success page.
                return redirect('success_url')  # Ganti 'success_url' dengan nama URL halaman sukses login
            else:
                # Account is not active
                messages.error(request, 'Akun tidak aktif.')
        else:
            # Invalid login
            messages.error(request, 'Email atau kata sandi salah.')

    return render(request, 'admin/login/login.html')  # Ganti 'login.html' dengan nama template halaman login
