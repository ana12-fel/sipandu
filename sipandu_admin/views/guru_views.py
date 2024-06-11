from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from sipandu_app.models import Data_guru,Master_sekolah


def IndexGuru(request):
    if request.method == 'POST':
        guru_sekolah = request.POST.get('guru_sekolah')
        nama_guru = request.POST.get('nama_guru')
        nip_guru = request.POST.get('nip_guru')
        mata_pelajaran = request.POST.get('mata_pelajaran')
        pendidikan = request.POST.get('pendidikan')
        status_kepegawaian = request.POST.get('status_kepegawaian')
        tahun_guru = request.POST.get('tahun_guru')
        guru_image = request.FILES.get('guru_image')



        print(guru_sekolah)

        dt_guru = Data_guru.objects.create(guru_sekolah=Master_sekolah.objects.get(sekolah_id=guru_sekolah),
                                           nama_guru=nama_guru,
                                           nip_guru=nip_guru,
                                           mata_pelajaran=mata_pelajaran,
                                           pendidikan=pendidikan,
                                           status_kepegawaian=status_kepegawaian,
                                           tahun_guru=tahun_guru,
                                           guru_image=guru_image
                                            )
        
        print(guru_sekolah,nama_guru,nip_guru,mata_pelajaran,pendidikan,status_kepegawaian,tahun_guru,guru_image)

        return redirect('sipandu_admin:index_guru')
    
    else:
        data_sekolah = Master_sekolah.objects.by_hakakses(request.user).all()
        data_guru = Data_guru.objects.filter(deleted_at=None)
        data_arsip_guru = Data_guru.objects.filter(deleted_at__isnull=False)

        return render(request, 'admin/data/data_guru.html', {'data_sekolah' : data_sekolah, 'data_guru' : data_guru, 'data_arsip_guru':data_arsip_guru})
    
def EditGuru(request, id_data_guru):
    dt_guru = get_object_or_404(Data_guru, id_data_guru=id_data_guru)

    if request.method == 'POST':
        guru_sekolah_id = request.POST.get('guru_sekolah')
        nama_guru = request.POST.get('nama_guru')
        nip_guru = request.POST.get('nip_guru')
        mata_pelajaran = request.POST.get('mata_pelajaran')
        pendidikan = request.POST.get('pendidikan')
        status_kepegawaian = request.POST.get('edit_status_kepegawaian')
        tahun_guru = request.POST.get('edit_tahun_guru')
        guru_image = request.FILES.get('guru_image')

        if status_kepegawaian == 'guru':
            dt_guru.tahun_guru = None
            dt_guru.mata_pelajaran = mata_pelajaran
        else:
            dt_guru.tahun_guru = tahun_guru
            dt_guru.mata_pelajaran = None
            # try:
            #     guru_sekolah = Master_sekolah.objects.get(sekolah_id=guru_sekolah_id)
            #     dt_guru.guru_sekolah = guru_sekolah
            # except Master_sekolah.DoesNotExist:
            #     return render(request, 'admin/data/edit_guru.html', {
            #         'data_sekolah': Master_sekolah.objects.all(),
            #         'dt_guru': dt_guru,
            #         'error': 'Sekolah tidak ditemukan'
            #     })

        dt_guru.nama_guru = nama_guru
        dt_guru.nip_guru = nip_guru
        
        dt_guru.pendidikan = pendidikan
        dt_guru.status_kepegawaian = status_kepegawaian
        

        if guru_image:
            dt_guru.guru_image = guru_image

        dt_guru.save()
        return redirect('sipandu_admin:index_guru')

    else:
        data_sekolah = Master_sekolah.objects.by_hakakses(request.user).all()
        return render(request, 'admin/data/edit_guru.html', {
            'data_sekolah': data_sekolah,
            'dt_guru': dt_guru
        })
    
def DeleteGuru (request, id_data_guru):
    try:
        dt_guru = get_object_or_404(Data_guru, id_data_guru=id_data_guru)
        
        dt_guru.delete()

        data = {
                'status': 'success',
                'message': 'data guru berhasil dihapus'
        }
        return JsonResponse(data, status=200)

    except Data_guru.DoesNotExist:
        data = {
                'status': 'error',
                'message': 'data guru gagal dihapus, data tidak ditemukan'
        }
        return JsonResponse(data, status=400)
    
def archive_guru(request, id_data_guru):
    if request.method == "POST":
        guru = get_object_or_404(Data_guru, pk=id_data_guru)
        guru.archive()
        return JsonResponse({"message": "Data berhasil diarsipkan."})
    else:
        return JsonResponse({"error": "Metode HTTP tidak valid."}, status=405)

    
def unarchive_guru(request, id_data_guru):
    if request.method == 'POST':
        try:
            guru = Data_guru.objects.get(id_data_guru=id_data_guru)
            guru.deleted_at = None
            guru.save()
            return JsonResponse({'message': 'Data berhasil diunarsipkan'}, status=200)
        except Data_guru.DoesNotExist:
            return JsonResponse({'error': 'Data jenjang tidak ditemukan'}, status=404)
    else:
        return JsonResponse({'error': 'Metode request tidak diizinkan'}, status=405)
