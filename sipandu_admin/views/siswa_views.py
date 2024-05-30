from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from sipandu_app.models import Data_siswa,Master_sekolah
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.http import require_POST

def IndexSiswa(request):
    if request.method == 'POST':
        siswa_sekolah = request.POST.get('siswa_sekolah')
        total_siswa = request.POST.get('total_siswa')
        keterangan_siswa = request.POST.get('keterangan_siswa')
        icon_siswa = request.POST.get('icon_siswa')

        if not total_siswa.isdigit():
            messages.error(request, 'Total Siswa harus berupa angka.')
            data_sekolah = Master_sekolah.objects.all()
            data_siswa = Data_siswa.objects.all()
            return render(request, 'admin/data/data_siswa.html', {'data_sekolah': data_sekolah, 'data_siswa': data_siswa})

        dt_siswa = Data_siswa.objects.create(
            siswa_sekolah=Master_sekolah.objects.get(sekolah_id=siswa_sekolah),
            total_siswa=int(total_siswa),  # Pastikan untuk mengkonversi ke integer
            keterangan_siswa=keterangan_siswa,
            icon_siswa=icon_siswa
        )

        return redirect('sipandu_admin:index_siswa')
    
    else:
        data_sekolah = Master_sekolah.objects.all()
        data_siswa = Data_siswa.objects.filter(deleted_at=None)
        data_arsip = Data_siswa.objects.filter(deleted_at__isnull=False)

        return render(request, 'admin/data/data_siswa.html', {'data_sekolah': data_sekolah, 'data_siswa': data_siswa, 'data_arsip':data_arsip})

def EditSiswa(request, id_data_siswa):
    dt_siswa = get_object_or_404(Data_siswa, id_data_siswa=id_data_siswa)
    if request.method == 'POST':
        siswa_sekolah = request.POST.get('siswa_sekolah')
        total_siswa = request.POST.get('edit_total_siswa')
        keterangan_siswa = request.POST.get('keterangan_siswa')
        icon_siswa = request.POST.get('icon_siswa')

        # Validate total_siswa
        try:
            total_siswa = int(total_siswa)
            if total_siswa < 0:
                raise ValueError("Total Siswa harus positif.")
        except ValueError:
            messages.error(request, 'Total Siswa harus berupa bilangan bulat positif.')
            data_sekolah = Master_sekolah.objects.all()
            return render(request, 'admin/data/edit_siswa.html', {
                'dt_siswa': dt_siswa,
                'data_sekolah': data_sekolah
            })

        dt_siswa.siswa_sekolah = Master_sekolah.objects.get(sekolah_id=siswa_sekolah)
        dt_siswa.total_siswa = total_siswa
        dt_siswa.keterangan_siswa = keterangan_siswa
        dt_siswa.icon_siswa = icon_siswa

        dt_siswa.save()

        return redirect('sipandu_admin:index_siswa')
    
    else:
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/edit_siswa.html', {
            'dt_siswa': dt_siswa,
            'data_sekolah': data_sekolah
        })
    
def DeleteSiswa (request, id_data_siswa):
    try:
        dt_siswa = get_object_or_404(Data_siswa, id_data_siswa=id_data_siswa)
        
        dt_siswa.delete()

        data = {
                'status': 'success',
                'message': 'data siswa berhasil dihapus'
        }
        return JsonResponse(data, status=200)

    except Data_siswa.DoesNotExist:
        data = {
                'status': 'error',
                'message': 'data siswa gagal dihapus, data tidak ditemukan'
        }
        return JsonResponse(data, status=400)
    
def archive_siswa(request, id_data_siswa):
    if request.method == "POST":
        siswa = get_object_or_404(Data_siswa, pk=id_data_siswa)
        siswa.archive()
        return JsonResponse({"message": "Data berhasil diarsipkan."})
    else:
        return JsonResponse({"error": "Metode HTTP tidak valid."}, status=405)
    
def unarchive_siswa(request, id_data_siswa):
    if request.method == 'POST':
        print('test')
        try:
            siswa = Data_siswa.objects.get(id_data_siswa=id_data_siswa)

            print(siswa)
            siswa.deleted_at = None
            siswa.save()
            return JsonResponse({'message': 'Data berhasil diunarsipkan'}, status=200)
        except Data_siswa.DoesNotExist:
            return JsonResponse({'error': 'Data jenjang tidak ditemukan'}, status=404)
    else:
        return JsonResponse({'error': 'Metode request tidak diizinkan'}, status=405)

