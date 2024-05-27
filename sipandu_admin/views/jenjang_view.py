from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from sipandu_app.models import Master_jenjang
from django.urls import reverse
from django.views.decorators.http import require_POST


def IndexJenjang(request):
    if request.method == 'POST':
        jenjang_nama = request.POST.get('jenjang_nama')
        jenjang_status = request.POST.get('jenjang_status')
        data = {}
        try:
            dt_jenjang = Master_jenjang.objects.create(jenjang_nama=jenjang_nama, jenjang_status=jenjang_status)
            print(jenjang_nama, jenjang_status)
            return JsonResponse(data, status = 201)
        except IntegrityError:
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
    
def archive_jenjang(request, jenjang_id):
    if request.method == "POST":
        jenjang = get_object_or_404(Master_jenjang, pk=jenjang_id)
        jenjang.archive()
        return JsonResponse({"message": "Data berhasil diarsipkan."})
    else:
        return JsonResponse({"error": "Metode HTTP tidak valid."}, status=405)