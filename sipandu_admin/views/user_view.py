from django.shortcuts import render, redirect, HttpResponse
from sipandu_app.models import Master_user, LEVEL_WILAYAH, ROLE_CHOICE

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
            user_password=user_password,
            user_level=user_level,
            user_email=user_email,
            user_role=user_role
        )
        
        print(user_first_name, user_last_name, user_password, user_level, user_email, user_role)

        return redirect('sipandu_admin:index_user')

    else:
        data_user = Master_user.objects.all()

        return render(request, 'admin/master/index_master_user.html', {"data_user" : data_user, 'level': LEVEL_WILAYAH, 'role_choices': ROLE_CHOICE})
    
def edit_user(request, user_id):
    if request.method == 'POST':
        user = Master_user.objects.get(user_id=user_id)
        user.user_first_name = request.POST.get('first_name')
        user.user_last_name = request.POST.get('last_name')
        user.user_password = request.POST.get('password')
        user.user_level = request.POST.get('level')
        user.user_email = request.POST.get('email')
        user.user_role = request.POST.get('role')


        user.save()
        
        return redirect('sipandu_admin:index_user')
    
    else:
        user = Master_user.objects.get(user_id=user_id)
        return render(request, 'admin/master/edit_user.html', {"dt_user": user})
    
def delete_user(request, user_id):
    try:
        user = Master_user.objects.get(user_id=user_id)
        user.delete()
        return redirect('sipandu_admin:index_user')
    except Master_user.DoesNotExist:
        return HttpResponse("Pengguna tidak ditemukan", status=404)
