from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from sipandu_app.models import Master_user, LEVEL_WILAYAH, ROLE_CHOICE
from django.contrib.auth.decorators import login_required

# @login_required(login_url='sipandu_admin:login_index')
def IndexUser(request):
    if request.method == 'POST':
        user_first_name = request.POST.get('first_name')
        user_last_name = request.POST.get('last_name')
        user_role = request.POST.get('role')
        user_password = request.POST.get('password')
        user_level = request.POST.get('level')
        user_email = request.POST.get('email')

    
        dt_user = Master_user.objects.create(
            user_first_name=user_first_name,
            user_last_name=user_last_name,
            user_level=user_level,
            user_email=user_email,
            user_role=user_role
        )

        dt_user.set_password(user_password)
        dt_user.save()
        
        print(user_first_name, user_last_name, user_password, user_level, user_email, user_role)

        return redirect('sipandu_admin:index_user')

    else:
        data_user = Master_user.objects.all()

        return render(request, 'admin/master/index_master_user.html', {"data_user" : data_user, 'level': LEVEL_WILAYAH, 'role_choices': ROLE_CHOICE})

# @login_required(login_url='sipandu_admin:login_index')
def edit_user(request, user_id):
    if request.method == 'POST':
        dt_user = Master_user.objects.get(user_id=user_id)

        user_first_name = request.POST.get('first_name')
        user_last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        user_level = request.POST.get('level')
        user_email = request.POST.get('email')
        user_role = request.POST.get('role')

        dt_user.user_first_name=user_first_name,
        dt_user.user_last_name=user_last_name,
        dt_user.password=password,
        dt_user.user_level=user_level,
        dt_user.user_email=user_email,
        dt_user.user_role=user_role

        dt_user.save()
        
        return redirect('sipandu_admin:index_user')
    
    else:
        user = Master_user.objects.get(user_id=user_id)
        return render(request, 'admin/master/edit_user.html', {"dt_user": user})

# @login_required(login_url='sipandu_admin:login_index')
def delete_user(request, user_id):
    try:
        dt_user = Master_user.objects.get(user_id=user_id)
        print(dt_user)
        dt_user.delete()

        data = {
                'status': 'success',
                'message': 'data sekolah berhasil dihapus'
        }
        return JsonResponse(data, status=200)

    except Master_user.DoesNotExist as e:
        print('Error delete user', e)
        data = {
                'status': 'error',
                'message': 'data sekolah gagal dihapus, data sekolah tidak ditemukan'
        }
        return JsonResponse(data, status=400)

