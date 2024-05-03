from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from sipandu_app.models import Master_wilayah, LEVEL_WILAYAH
from django.urls import reverse

def IndexWilayah(request):
    if request.method == 'POST':
        wilayah_id = request.POST.get('wilayah_id')
        wilayah_kode = request.POST.get('wilayah_kode') 
        wilayah_nama = request.POST.get('wilayah_nama')
        wilayah_level = request.POST.get('wilayah_level')
        wilayah_status = request.POST.get('wilayah_status')
        
        prov = request.POST.get('prov')
        kab = request.POST.get('kab')
        kec = request.POST.get('kec')

        if wilayah_level == '1': #prov
            wilayah_parent = None
        elif wilayah_level == '2': #kab
            wilayah_parent = Master_wilayah.objects.get(wilayah_id = prov)
        elif wilayah_level == '3': #kec
            wilayah_parent = Master_wilayah.objects.get(wilayah_id = kab)
        else:
            wilayah_parent = Master_wilayah.objects.get(wilayah_id = kec)

        dt_wilayah = Master_wilayah.objects.create(
            wilayah_kode=wilayah_kode,
            wilayah_nama=wilayah_nama,
            wilayah_level=wilayah_level,
            wilayah_parent=wilayah_parent
        )

        print(wilayah_id, wilayah_kode, wilayah_status, wilayah_parent, wilayah_level)

        return redirect('sipandu_admin:index_wilayah')
    
    else:
        data_wilayah = Master_wilayah.objects.all()
        data_prov = Master_wilayah.objects.filter(wilayah_level='1')
        return render(request, 'admin/master/index_master_wilayah.html', {'data_wilayah': data_wilayah, 'wilayah_level': LEVEL_WILAYAH,
            "data_prov": data_prov})

def get_wilayah_by_level(request):
    if request.method == 'GET':
        level = request.GET.get('level')
        wilayah_id = request.GET.get('wilayah_id')
        
        wilayah_list = Master_wilayah.objects.filter(wilayah_parent=wilayah_id).values('wilayah_id', 'wilayah_nama')
        
        return JsonResponse({"data_wilayah": list(wilayah_list)})
    return JsonResponse({'error': 'Invalid request'})

    
def edit_wilayah(request, wilayah_id):
    if request.method == 'POST':
        print(request.POST)
        dt_wilayah = Master_wilayah.objects.get(wilayah_id=wilayah_id)
        wilayah_status=request.POST.get('wilayah_status')
        wilayah_kode=request.POST.get('wilayah_kode')
        wilayah_provinsi = request.POST.get('wilayah_provinsi')
        wilayah_kabupaten = request.POST.get('wilayah_kabupaten')
        wilayah_distrik = request.POST.get('wilayah_distrik')
        
        
        dt_wilayah.wilayah_provinsi=wilayah_provinsi
        dt_wilayah.wilayah_kode=wilayah_kode
        dt_wilayah.wilayah_status=wilayah_status
        dt_wilayah.wilayah_kabupaten = wilayah_kabupaten
        dt_wilayah.wilayah_distrik = wilayah_distrik
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
