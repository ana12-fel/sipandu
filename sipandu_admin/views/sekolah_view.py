from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from sipandu_app.models import Master_sekolah, Master_wilayah, Master_jenjang

def IndexSekolah(request):
    if request.method == 'POST':
        sekolah_nama = request.POST.get('sekolah_nama') 
        sekolah_npsn = request.POST.get('sekolah_npsn')
        sekolah_jenis = request.POST.get('sekolah_jenis')
        sekolah_wilayah = request.POST.get ('sekolah_provinsi')
        sekolah_jenjang = request.POST.get('sekolah_jenjang')
        
        print (sekolah_jenjang)
        dt_sekolah = Master_sekolah.objects.create(
            sekolah_nama=sekolah_nama,
            sekolah_npsn=sekolah_npsn,
            sekolah_jenis=sekolah_jenis,
            sekolah_wilayah_id=sekolah_wilayah,
            sekolah_jenjang=Master_jenjang.objects.get(jenjang_id = sekolah_jenjang),
        )

        print(sekolah_nama, sekolah_npsn, sekolah_jenis, sekolah_jenjang,sekolah_wilayah)

        return redirect('sipandu_admin:index_sekolah')
    
    else:
        data_jenjang = Master_jenjang.objects.all()
        data_sekolah = Master_sekolah.objects.all()
        data_wilayah = Master_wilayah.objects.all()
        return render(request, 'admin/master/index_master_sekolah.html', {'data_sekolah': data_sekolah, 'data_wilayah': data_wilayah, "data_jenjang": data_jenjang})
    
def edit_sekolah(request, sekolah_id):
    if request.method == 'POST':
        dt_sekolah = Master_sekolah.objects.get(sekolah_id=sekolah_id)

        sekolah_nama = request.POST.get('sekolah_nama')
        sekolah_npsn = request.POST.get('sekolah_npsn')
        sekolah_jenis = request.POST.get('sekolah_jenis')
        sekolah_jenjang = request.POST.get('sekolah_jenjang')

        dt_sekolah.sekolah_nama=sekolah_nama
        dt_sekolah.sekolah_npsn=sekolah_npsn
        dt_sekolah.sekolah_jenis=sekolah_jenis
        dt_sekolah.sekolah_jenjang=Master_jenjang.objects.get(jenjang_id__icontains = sekolah_jenjang)

        dt_sekolah.save()
        
        return redirect('sipandu_admin:index_sekolah')
    
    else:
        dt_sekolah = Master_sekolah.objects.get(sekolah_id=sekolah_id)
        return render(request, 'admin/master/edit_sekolah.html', {"dt_sekolah": dt_sekolah, "id_sekolah": sekolah_id })

    
def delete_sekolah(request, sekolah_id):
    try:
        dt_sekolah = get_object_or_404(Master_sekolah, sekolah_id=sekolah_id)
        
        dt_sekolah.delete()

        data = {
                'status': 'success',
                'message': 'data sekolah berhasil dihapus'
        }
        return JsonResponse(data, status=200)

    except Master_sekolah.DoesNotExist:
        data = {
                'status': 'error',
                'message': 'data sekolah gagal dihapus, data sekolah tidak ditemukan'
        }
        return JsonResponse(data, status=400)
    


