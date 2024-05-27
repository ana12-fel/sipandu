from django.shortcuts import render, redirect,get_object_or_404
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
        data_kab = Master_wilayah.objects.filter(wilayah_level='2')
        return render(request, 'admin/master/index_master_wilayah.html', {'data_wilayah': data_wilayah, 'wilayah_level': LEVEL_WILAYAH,
            "data_prov": data_prov, "kab" : data_kab})

def get_wilayah_by_level(request):
    if request.method == 'GET':
        level = request.GET.get('level')
        wilayah_id = request.GET.get('wilayah_id')
        
        wilayah_list = Master_wilayah.objects.filter(wilayah_parent=wilayah_id).values('wilayah_id', 'wilayah_nama')
        
        return JsonResponse({"data_wilayah": list(wilayah_list)})
    return JsonResponse({'error': 'Invalid request'})


def edit_wilayah(request, wilayah_id):
    # Mengambil objek wilayah yang akan diedit
    dt_wilayah = get_object_or_404(Master_wilayah, wilayah_id=wilayah_id)
  
    if request.method == 'POST':
        wilayah_kode = request.POST.get('wilayah_kode_edit') 
        wilayah_nama = request.POST.get('wilayah_nama_edit')
        wilayah_level = request.POST.get('wilayah_level_edit')
        wilayah_status = request.POST.get('wilayah_status_edit')
        
        prov = request.POST.get('prov_edit')
        kab = request.POST.get('kab_edit')
        kec = request.POST.get('kec_edit')
        
        # Menentukan wilayah parent berdasarkan level yang dipilih
        if wilayah_level == '1': #prov
            wilayah_parent = None
        elif wilayah_level == '2': #kab
            wilayah_parent = get_object_or_404(Master_wilayah, wilayah_id=prov)
        elif wilayah_level == '3': #kec
            wilayah_parent = get_object_or_404(Master_wilayah, wilayah_id=kab)
        else:
            wilayah_parent = get_object_or_404(Master_wilayah, wilayah_id=kec)

        # Memperbarui atribut wilayah yang ada
        dt_wilayah.wilayah_kode = wilayah_kode
        dt_wilayah.wilayah_nama = wilayah_nama
        dt_wilayah.wilayah_level = wilayah_level
        dt_wilayah.wilayah_parent = wilayah_parent

        # Menyimpan perubahan
        dt_wilayah.save()

        return redirect('sipandu_admin:index_wilayah')
    
    else:
        data_wilayah = Master_wilayah.objects.all()
        data_prov = Master_wilayah.objects.filter(wilayah_level='1')
        return render(request, 'admin/master/edit_wilayah.html', {'dt_wilayah': dt_wilayah, 'data_wilayah': data_wilayah, 'wilayah_level': LEVEL_WILAYAH, "data_prov": data_prov})


def delete_wilayah(request, wilayah_id):      
    try:
        # Mengambil objek wilayah berdasarkan wilayah_id
        dt_wilayah = Master_wilayah.objects.get(wilayah_id=wilayah_id)
        
        # Hapus objek wilayah
        dt_wilayah.delete()

        # Beri respons JSON bahwa objek wilayah berhasil dihapus
        data = {
            'status': 'success',
            'message': 'Wilayah berhasil dihapus'
        }
        return JsonResponse(data, status=200)
    
    except Master_wilayah.DoesNotExist:
        # Jika wilayah tidak ditemukan, kembalikan respons 404
        data = {
            'status': 'error',
            'message': 'Wilayah tidak ditemukan'
        }
        return JsonResponse(data, status=404)
    

def cek_kode_wilayah(request):
    kode = request.GET.get('kode', None)
    data = {
        'is_unique': not Master_wilayah.objects.filter(wilayah_kode=kode).exists()
    }
    return JsonResponse(data)

