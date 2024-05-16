from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from sipandu_app.models import Master_user, LEVEL_WILAYAH, ROLE_CHOICE,Master_wilayah,Master_sekolah
from django.contrib.auth.decorators import login_required

# @login_required(login_url='sipandu_admin:login_index')
def IndexUser(request):
    if request.method == 'POST':
        user_first_name = request.POST.get('first_name')
        user_last_name = request.POST.get('last_name')
        user_role = request.POST.get('role')
        user_password = request.POST.get('password')
        user_email = request.POST.get('email')
        user_status = request.POST.get('user_status')
        user_sekolah_id = request.POST.get('user_sekolah')  # Change to user_sekolah_id

        
        kab = request.POST.get('kab')
        
        print(user_sekolah_id)
        # Resolve user_kabupaten based on the user's role and location
        
        if  user_role == 'admin_kabupaten': 
            user_kabupaten = Master_wilayah.objects.get(wilayah_id=kab)
            user_sekolah = None
        elif user_role == 'admin_sekolah': 
            user_kabupaten = None
            user_sekolah = Master_sekolah.objects.get(sekolah_id=user_sekolah_id) # Change to user_sekolah_id
        else:
            user_kabupaten = None
            user_sekolah = None
            

        dt_user = Master_user.objects.create(
            user_first_name=user_first_name,
            user_last_name=user_last_name,
            user_email=user_email,
            user_role=user_role,
            password=user_password,
            user_status=user_status,
            user_kabupaten=user_kabupaten,
            user_sekolah=user_sekolah   # Change to user_sekolah_id
        )

        dt_user.set_password(user_password)
        dt_user.save()


        print(user_first_name, user_last_name, user_password, user_email, user_role, user_status, user_kabupaten, user_sekolah)  # Change to user_sekolah_id

        return redirect('sipandu_admin:index_user')

    else:
        data_user = Master_user.objects.all()
        data_wilayah = Master_wilayah.objects.all()
        data_prov = Master_wilayah.objects.filter(wilayah_level='1')
        data_sekolah = Master_sekolah.objects.all()  
        print (data_prov)
        return render(request, 'admin/master/index_master_user.html', {"data_user": data_user, 'role_choices': ROLE_CHOICE, 'wilayah': data_wilayah, 'prov': data_prov,'sekolah':data_sekolah})
        
# @login_required(login_url='sipandu_admin:login_index')


def edit_user(request, user_id):
    dt_user = get_object_or_404(Master_user, user_id=user_id)

    if request.method == 'POST':
        user_first_name = request.POST.get('first_name_edit')
        user_last_name = request.POST.get('last_name_edit')
        user_role = request.POST.get('role_edit')
        user_password = request.POST.get('password_edit')
        user_email = request.POST.get('email_edit')
        user_status = request.POST.get('user_status_edit')
        user_sekolah_id = request.POST.get('user_sekolah_edit')
        
        kab_edit = request.POST.get('kab_edit')
        print(user_role, kab_edit, user_sekolah_id)
        
        # Inisialisasi variabel dengan nilai default None
        user_kabupaten = None
        user_sekolah = None

        # Tentukan user_kabupaten atau user_sekolah berdasarkan peran dan lokasi pengguna
        if user_role == 'admin_kabupaten': 
            user_kabupaten = Master_wilayah.objects.filter(wilayah_id=kab_edit).first()
        elif user_role == 'admin_sekolah': 
            user_sekolah = Master_sekolah.objects.filter(sekolah_id=user_sekolah_id).first()

        # Update detail pengguna
        dt_user.user_first_name = user_first_name
        dt_user.user_last_name = user_last_name
        dt_user.user_email = user_email
        dt_user.user_role = user_role
        dt_user.password = user_password  # Sebaiknya hash password sebelum menyimpan
        dt_user.user_status = user_status
        dt_user.user_kabupaten = user_kabupaten
        dt_user.user_sekolah = user_sekolah

        dt_user.set_password(user_password)
        dt_user.save()

        return redirect('sipandu_admin:index_user')

    else:
        data_user = Master_user.objects.all()
        data_wilayah = Master_wilayah.objects.all()
        data_prov = Master_wilayah.objects.filter(wilayah_level='1')
        data_kab = Master_wilayah.objects.filter(wilayah_level='2')
        
        return render(request, 'admin/master/edit_user.html', {
            "data_user": data_user,
            'role_choices': ROLE_CHOICE,
            'wilayah': data_wilayah,
            'prov': data_prov,
            'kab': data_kab
        })


        

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
    

def get_user_by_level(request):
    if request.method == 'GET':
        level = request.GET.get('level')
        wilayah_id = request.GET.get('wilayah_id')

        print('level', level)
        if level == 'kecamatan':
            print('wilayah_id', wilayah_id)
            wilayah_list = Master_sekolah.objects.filter(sekolah_kecamatan_id=wilayah_id).values('sekolah_id', 'sekolah_nama')
        else:
            wilayah_list = Master_wilayah.objects.filter(wilayah_parent=wilayah_id).values('wilayah_id', 'wilayah_nama')
        # print(wilayah_list, level)
        
        return JsonResponse({"data_wilayah": list(wilayah_list)})
    return JsonResponse({'error': 'Invalid request'})

