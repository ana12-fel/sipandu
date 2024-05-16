from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from sipandu_app.models import Master_jenjang
from django.urls import reverse

def IndexJenjang(request):
    if request.method == 'POST':
        jenjang_nama = request.POST.get('jenjang_nama')
        jenjang_status = request.POST.get('jenjang_status')
        data = {}
        try:
            dt_jenjang = Master_jenjang.objects.create(jenjang_nama=jenjang_nama, jenjang_status=jenjang_status)
            # Lakukan sesuatu jika penyimpanan berhasil
            print(jenjang_nama, jenjang_status)
            # return redirect('sipandu_admin:index_jenjang')
            return JsonResponse(data, status = 201)
        except IntegrityError:
            # Tangani kasus ketika data sudah ada di dalam basis data
            print("Data dengan nama jenjang tersebut sudah ada")
            return JsonResponse(data, status = 400)

    else:
        data_jenjang = Master_jenjang.objects.all()
        return render(request, 'admin/master/index_master_jenjang.html', {"data_jenjang": data_jenjang})


def edit_jenjang(request, jenjang_id):
    if request.method == 'POST':
        dt_jenjang = Master_jenjang.objects.get(jenjang_id=jenjang_id)
        jenjang_nama = request.POST.get('jenjang_nama')
        is_active = request.POST.get('jenjang_status')  
        
        dt_jenjang.jenjang_nama=jenjang_nama
        dt_jenjang.jenjang_status=is_active
        dt_jenjang.save()
        return redirect('sipandu_admin:index_jenjang') 
    
    else:
        dt_jenjang = Master_jenjang.objects.get(jenjang_id=jenjang_id)
        return render(request, 'admin/master/edit_jenjang.html', {'is_active': is_active,"dt_jenjang": dt_jenjang,"id_jenjang": jenjang_id})
    
def delete_jenjang(request, jenjang_id):
    try:
       
        dt_jenjang = get_object_or_404(Master_jenjang, jenjang_id=jenjang_id)
        
        dt_jenjang.delete()

        data = {
                'status': 'success',
                'message': 'Jenjang berhasil dihapus'
        }
        return JsonResponse(data, status=200)

    except Master_jenjang.DoesNotExist:
        data = {
                'status': 'error',
                'message': 'Jenjang gagal dihapus, jenjang tidak ditemukan'
        }
        return JsonResponse(data, status=400)
