from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from sipandu_app.models import Master_wilayah
from django.urls import reverse

def IndexWilayah(request):
    if request.method == 'POST':
        wilayah_id = request.POST.get('wilayah_id')
        wilayah_kode = request.POST.get('wilayah_kode') 
        wilayah_parent = request.POST.get ('wilayah_parent')
        wilayah_nama = request.POST.get('wilayah_nama')
        wilayah_status = request.POST.get('wilayah_status')

        dt_wilayah = Master_wilayah.objects.create(
            wilayah_id=wilayah_id,
            wilayah_kode=wilayah_kode,
            wilayah_parent=wilayah_parent,
            wilayah_nama=wilayah_nama,
            wilayah_status=wilayah_status,
        )

        print(wilayah_id,wilayah_kode,wilayah_parent,wilayah_nama,wilayah_status)

        return redirect('sipandu_admin:index_wilayah')
    
    else:
        data_wilayah = Master_wilayah.objects.all()
        return render(request, 'admin/master/index_master_wilayah.html', {'data_wilayah': data_wilayah})
    
def edit_wilayah(request, wilayah_id):
    if request.method == 'POST':
        print(request.POST)
        dt_wilayah = Master_wilayah.objects.get(wilayah_id=wilayah_id)
        wilayah_status=request.POST.get('wilayah_status')
        wilayah_kode=request.POST.get('wilayah_kode')
        wilayah_nama = request.POST.get('wilayah_nama')
        
        
        dt_wilayah.wilayah_nama=wilayah_nama
        dt_wilayah.wilayah_kode=wilayah_kode
        dt_wilayah.wilayah_status=wilayah_status
        # Lakukan perubahan yang diperlukan pada objek dt_wilayah
        dt_wilayah.save()
        return redirect('sipandu_admin:index_wilayah')  # Redirect ke halaman edit_wilayah dengan menyertakan wilayah_id
    
    else:
        dt_wilayah = Master_wilayah.objects.get(wilayah_id=wilayah_id)
        return render(request, 'admin/master/edit_wilayah.html', {"dt_wilayah": dt_wilayah,"id_wilayah": wilayah_id})


def delete_wilayah(request, wilayah_id):      
    try:
        # Mengambil objek wilayah berdasarkan wilayah_id
        dt_wilayah = get_object_or_404(Master_wilayah, wilayah_id=wilayah_id)
        
        # Hapus objek wilayah
        dt_wilayah.delete()

        # Redirect ke halaman indeks wilayah menggunakan nama URL
        data = {
                'status': 'success',
                'message': 'wilayah berhasil dihapus'
        }
        return JsonResponse(data, status=200)
    
    except Master_wilayah.DoesNotExist:
        # Jika jenjang tidak ditemukan, kembalikan respons 404
        data = {
                'status': 'error',
                'message': 'Jenjang gagal dihapus, jenjang tidak ditemukan'
        }
        return JsonResponse(data, status=400)
