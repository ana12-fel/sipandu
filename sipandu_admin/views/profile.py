from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from sipandu_app.models import Master_user


@login_required
def IndexProfile(request):
    user = request.user

    if not user.is_anonymous:
        try:
            master_user = Master_user.objects.get(user_email=user.user_email)
            first_name = master_user.user_first_name
            last_name = master_user.user_last_name
            email = master_user.user_email
            last_login = master_user.user_last_login
            role = master_user.user_role
            password = master_user.password

        except Master_user.DoesNotExist:
            master_user = None
            first_name = None
            last_name = None
            email = None
            last_login = None
            role = None
            password = None
    else:
        master_user = None
        first_name = None
        last_name = None
        email = None
        last_login = None
        role = None
        password = None

    context = {
        'master_user': master_user,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'last_login': last_login,
        'role': role,
        'password': password,
    }

    return render(request, 'admin/profile/profile.html', context)


# @login_required
def edit_profile(request):
    user = request.user

    try:
        master_user = Master_user.objects.get(user_email=user.user_email)
    except Master_user.DoesNotExist:
        return redirect('sipandu_admin:index_profile')

    if request.method == 'POST':
        user_first_name = request.POST.get('user_first_name')
        user_last_name = request.POST.get('user_last_name')
        user_email = request.POST.get('user_email')
        user_phone = request.POST.get('user_phone')
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        master_user.user_first_name = user_first_name
        master_user.user_last_name = user_last_name
        master_user.user_email = user_email
        master_user.user_phone = user_phone

        if password and new_password and confirm_password:
            if master_user.check_password(password):
                if new_password == confirm_password:
                    master_user.password = make_password(new_password)
                    messages.success(request, 'Password updated successfully.')
                else:
                    messages.error(request, 'New password and confirm password do not match.')
            else:
                messages.error(request, 'Current password is incorrect.')

        master_user.save()

        messages.success(request, 'Profile updated successfully.')
        return redirect('sipandu_admin:index_profile')

    context = {
        'master_user': master_user,
    }

    return render(request, 'admin/profile/edit_profile.html', context)