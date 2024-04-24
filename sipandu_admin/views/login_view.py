from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from flask import Flask, render_template, request, redirect, url_for, session


def login_index(request):
    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')

        user = authenticate(request, user_email=user_email, password=user_password)
        print(authenticate(request, user_email=user_email, password=user_password), user_email, user_password)
        if user is not None:
            if user.user_is_activate:
                login(request, user)
                # Redirect to a success page.
                return redirect('sipandu_admin:admin_index')  # Ganti 'success_url' dengan nama URL halaman sukses login
            else:
                # Account is not active
                messages.error(request, 'Akun tidak aktif.')
        else:
            # Invalid login
            messages.error(request, 'Email atau kata sandi salah.')

    return render(request, 'admin/login/login.html')  # Ganti 'login.html' dengan nama template halaman login

def logout():
    session.pop('user_email', None)
    return redirect(url_for('login_index'))

    if __name__ == '__main__':
        app.run(debug=True)
