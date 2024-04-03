from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from sipandu_app.models import Master_jenjang
from django.urls import reverse

def IndexJenjang(request):
    if request.method == 'POST':
        jenjang_id = request.POST.get ('jenjang_id')
        jenjang_nama = request.POST.get('jenjang_nama')
        jenjang_status = request.POST.get('jenjang_status')

        dt_jenjang = Master_jenjang.objects.create(jenjang_id=jenjang_id,jenjang_nama=jenjang_nama, jenjang_status=jenjang_status)
        
        print(jenjang_id,jenjang_nama, jenjang_status)

        return redirect('sipandu_admin:index_jenjang')

    else:
        data_jenjang = Master_jenjang.objects.all()

        return render(request, 'admin/master/index_master_jenjang.html', {"data_jenjang" : data_jenjang})


def edit_jenjang(request, jenjang_id):
    if request.method == 'POST':
        dt_jenjang = Master_jenjang.objects.get(jenjang_id=jenjang_id)
        jenjang_nama = request.POST.get('jenjang_nama')
        
        dt_jenjang.jenjang_nama=jenjang_nama
        # Lakukan perubahan yang diperlukan pada objek dt_jenjang
        dt_jenjang.save()
        return redirect('sipandu_admin:index_jenjang')  # Redirect ke halaman edit_jenjang dengan menyertakan jenjang_id
    
    else:
        dt_jenjang = Master_jenjang.objects.get(jenjang_id=jenjang_id)
        return render(request, 'admin/master/edit_jenjang.html', {"dt_jenjang": dt_jenjang,"id_jenjang": jenjang_id})
    
def delete_jenjang(request, jenjang_id):
    try:
        # Mengambil objek jenjang berdasarkan jenjang_id
        dt_jenjang = get_object_or_404(Master_jenjang, jenjang_id=jenjang_id)
        
        # Hapus objek jenjang
        dt_jenjang.delete()

        # Redirect ke halaman indeks jenjang menggunakan nama URL
        data = {
                'status': 'success',
                'message': 'Jenjang berhasil dihapus'
        }
        return JsonResponse(data, status=200)

    except Master_jenjang.DoesNotExist:
        # Jika jenjang tidak ditemukan, kembalikan respons 404
        data = {
                'status': 'error',
                'message': 'Jenjang gagal dihapus, jenjang tidak ditemukan'
        }
        return JsonResponse(data, status=400)
