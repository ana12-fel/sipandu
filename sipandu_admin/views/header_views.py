from django.shortcuts import render, redirect
from django.contrib import messages
from sipandu_app.models import Master_user



def IndexHeader(request):
    user = request.user

    try:
        master_user = Master_user.objects.get(user_email=user.user_email)
        first_name = master_user.user_first_name
        role = master_user.user_role
      

    except Master_user.DoesNotExist:
        master_user = None
        first_name = None
        role = None
        

    context = {
        'master_user': master_user,
        'first_name': first_name,
        'role': role,
    
    }

    return render(request, 'admin/base/header.html', context)