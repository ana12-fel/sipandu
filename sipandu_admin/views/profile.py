from django.shortcuts import render, redirect
from django.contrib import messages
from sipandu_app.models import Master_user
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse




@login_required
def IndexProfile(request):
    user = request.user

    try:
        master_user = Master_user.objects.get(user_email=user.user_email)
        first_name = master_user.user_first_name
        last_name = master_user.user_last_name
        email = master_user.user_email
        last_login = master_user.last_login
        role = master_user.user_role
      

    except Master_user.DoesNotExist:
        master_user = None
        first_name = None
        last_name = None
        email = None
        last_login = None
        role = None
        

    context = {
        'master_user': master_user,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'last_login': last_login,
        'role': role,
    
    }

    

    return render(request, 'admin/profile/profile.html', context)

@login_required
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

        master_user.user_first_name = user_first_name
        master_user.user_last_name = user_last_name
        master_user.user_email = user_email

        master_user.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('sipandu_admin:index_profile')

    context = {
        'master_user': master_user,
    }

    return render(request, 'admin/profile/edit_profile.html', context)

@login_required
def change_password(request):
    user = request.user

    try:
        master_user = Master_user.objects.get(user_email=user.user_email)
    except Master_user.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    if request.method == 'POST':
        current_password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if current_password and new_password and confirm_password:
            if check_password(current_password, master_user.password):
                if new_password == confirm_password:
                    master_user.password = make_password(new_password)
                    master_user.save()
                    return JsonResponse({'success': 'Password updated successfully'})
                else:
                    return JsonResponse({'error': 'New password and confirm password do not match'}, status=400)
            else:
                return JsonResponse({'error': 'Current password is incorrect'}, status=400)
        else:
            return JsonResponse({'error': 'All fields are required'}, status=400)

    context = {
        'master_user': master_user,
    }

    return render(request, 'admin/profile/edit_profile.html', context)


