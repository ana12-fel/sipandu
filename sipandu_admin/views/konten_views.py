from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from sipandu_app.models import Data_konten, Master_kategori,Master_sekolah, Sub_kategori, Transanksi_situs
from django.urls import reverse
from django.utils.timezone import now
from django.conf import settings
import os
from django.utils import timezone
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


@login_required(login_url='sipandu_admin:login_index')
def upload_and_save_image(request):
    konten_image = request.FILES.get('konten_image')
    
    if konten_image:
        file_name, file_extension = os.path.splitext(konten_image.name)
        current_time = timezone.now()
        formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
        new_file_name = f"{file_name}_{formatted_time}{file_extension}"
        
        with open(os.path.join(settings.MEDIA_ROOT, new_file_name), 'wb+') as destination:
            for chunk in konten_image.chunks():
                destination.write(chunk)
        
        return new_file_name  
    else:
        return None  

@login_required(login_url='sipandu_admin:login_index')
def IndexKonten(request):
    if request.method == 'POST':
        konten_sekolah = request.POST.get('konten_sekolah')
        konten_kategori = request.POST.get('konten_kategori')
        konten_sub_kategori = request.POST.get('konten_sub_kategori')
        judul = request.POST.get('judul')
        is_active = request.POST.get('status') == 'True'
        isi_konten = request.POST.get('isi_konten')
        konten_tag = request.POST.get('konten_tag')

        konten_image = upload_and_save_image(request)  

        if konten_image:
            dt_konten = Data_konten.objects.create(
                konten_sekolah=Master_sekolah.objects.get(sekolah_id=konten_sekolah), 
                konten_kategori=Master_kategori.objects.get(kategori_id=konten_kategori),
                konten_sub_kategori=Sub_kategori.objects.get(sub_kategori_id=konten_sub_kategori),
                judul=judul,
                status=is_active,
                isi_konten=isi_konten,
                konten_image=konten_image,  
                konten_tag=konten_tag
            )

            return redirect('sipandu_admin:index_konten')
        else:
            return HttpResponse("Gagal mengunggah gambar.", status=400)
    
    else:
        data_sekolah = Master_sekolah.objects.all()
        data_sub_kategori = Sub_kategori.objects.all()
        data_kategori = Master_kategori.objects.all()
        data_konten = Data_konten.objects.by_hakakses(request.user).filter(deleted_at=None)
        data_arsip_konten = Data_konten.objects.filter(deleted_at__isnull=False)        
        return render(request, 'admin/data/konten.html', {"data_sub_kategori": data_sub_kategori, "data_kategori": data_kategori, "data_konten": data_konten, "data_sekolah": data_sekolah, "data_arsip_konten": data_arsip_konten})

@login_required(login_url='sipandu_admin:login_index')
@require_GET
@csrf_exempt
def get_kategori_by_sekolah(request):
    sekolah_id = request.GET.get('sekolah_id')
    
    try:
        kategori_list = Master_kategori.objects.filter(
            kategori_tema=Transanksi_situs.objects.get(sekolah_id = sekolah_id).tema_id
        ).values('kategori_id', 'kategori_uraian')
        
        # Tambahkan debug log
        print(f"sub_kategori_list: {list(kategori_list)}")
        
        return JsonResponse({"data_kategori": list(kategori_list)})
    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({'error': str(e)}, status=500)
        
    return JsonResponse({'error': 'Invalid request'}, status=400)
 
@login_required(login_url='sipandu_admin:login_index')
@require_GET
@csrf_exempt
def get_sub_kategori(request):
    kategori_id = request.GET.get('kategori_id') 
    
    try:
        sub_kategori_list = Sub_kategori.objects.filter(
            kategori_id=kategori_id
        ).values('sub_kategori_id', 'sub_kategori_uraian')
        
        # Tambahkan debug log        
        return JsonResponse({"data_sub_kategori": list(sub_kategori_list)})
    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({'error': str(e)}, status=500)
        
    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required(login_url='sipandu_admin:login_index')
def TambahKonten(request):
    if request.method == 'POST':
        konten_sekolah = request.POST.get('konten_sekolah')
        konten_kategori = request.POST.get('konten_kategori')
        konten_sub_kategori = request.POST.get('konten_sub_kategori')
        judul = request.POST.get('judul')
        is_active = request.POST.get('status') == 'True'
        isi_konten = request.POST.get('isi_konten')
        konten_tag = request.POST.get('konten_tag')

        konten_image = upload_and_save_image(request)  

        dt_konten = Data_konten.objects.create(
            konten_sekolah=Master_sekolah.objects.get(sekolah_id=konten_sekolah), 
            konten_kategori=Master_kategori.objects.get(kategori_id=konten_kategori),
            konten_sub_kategori=Sub_kategori.objects.get(sub_kategori_id=konten_sub_kategori),
            judul=judul,
            status=is_active,
            isi_konten=isi_konten,
            konten_image=konten_image,  
            konten_tag=konten_tag
        )

        return redirect('sipandu_admin:index_konten')

    else:
        data_sekolah = Master_sekolah.objects.by_hakakses(request.user).all()
        data_kategori = Master_kategori.objects.all()
        data_sub_kategori = Sub_kategori.objects.all()
        data_konten = Data_konten.objects.all()

        return render(request, 'admin/data/tambah_konten.html', {'data_kategori': data_kategori, 'data_sub_kategori': data_sub_kategori, 'data_konten': data_konten, 'data_sekolah' : data_sekolah})


@login_required(login_url='sipandu_admin:login_index')
     
def EditKonten(request, id_data_konten):
    dt_konten = get_object_or_404(Data_konten, id_data_konten=id_data_konten)
    
    if request.method == 'POST':
        konten_sekolah = request.POST.get('konten_sekolah')
        konten_kategori = request.POST.get('konten_kategori')
        konten_sub_kategori = request.POST.get('konten_sub_kategori')
        judul = request.POST.get('judul')
        is_active = request.POST.get('status') == 'True'
        isi_konten = request.POST.get('isi_konten')
        konten_image = request.FILES.get('konten_image')
        konten_tag = request.POST.get('konten_tag')
        
        dt_konten.konten_sekolah = get_object_or_404(Master_sekolah, sekolah_id=konten_sekolah)
        dt_konten.konten_kategori = get_object_or_404(Master_kategori, kategori_id=konten_kategori)
        dt_konten.konten_sub_kategori = get_object_or_404(Sub_kategori, sub_kategori_id=konten_sub_kategori)
        dt_konten.judul = judul
        dt_konten.status = is_active
        dt_konten.isi_konten = isi_konten
        dt_konten.konten_tag = konten_tag

        if konten_image:
            # Mengubah nama file dengan menambahkan timestamp
            current_time = now()
            formatted_time = current_time.strftime("%Y-%m-%d_at_%H.%M.%S")
            file_extension = konten_image.name.split('.')[-1]
            new_file_name = f"{konten_image.name.split('.')[0]}_{formatted_time}.{file_extension}"
            konten_image.name = new_file_name
            dt_konten.konten_image = konten_image

        dt_konten.save()
        return redirect('sipandu_admin:index_konten')
    else:
        data_sekolah = Master_sekolah.objects.by_hakakses(request.user).all()
        data_kategori = Master_kategori.objects.all()
        data_sub_kategori = Sub_kategori.objects.all()
        
        context = {
            "dt_konten": dt_konten,
            "id_data_konten": id_data_konten,
            "data_sekolah": data_sekolah,
            "data_kategori": data_kategori,
            "data_sub_kategori": data_sub_kategori,
        }
        return render(request, 'admin/data/edit_konten.html', context)

@login_required(login_url='sipandu_admin:login_index')
def DeleteKonten(request, id_data_konten):
    try:
        dt_konten = get_object_or_404(Data_konten, id_data_konten=id_data_konten)
        
        dt_konten.delete()

        data = {
                'status': 'success',
                'message': 'data konten berhasil dihapus'
        }
        return JsonResponse(data, status=200)

    except Data_konten.DoesNotExist:
        data = {
                'status': 'error',
                'message': 'data konten gagal dihapus, data tidak ditemukan'
        }
        return JsonResponse(data, status=400)

@login_required(login_url='sipandu_admin:login_index')
def archive_konten(request, id_data_konten):
    if request.method == "POST":
        konten = get_object_or_404(Data_konten, pk=id_data_konten)
        konten.archive()
        return JsonResponse({"message": "Data berhasil diarsipkan."})
    else:
        return JsonResponse({"error": "Metode HTTP tidak valid."}, status=405)

@login_required(login_url='sipandu_admin:login_index')
def unarchive_konten(request, id_data_konten):
    if request.method == 'POST':
        print('test')
        try:
            konten = Data_konten.objects.get(id_data_konten=id_data_konten)
            konten.status = True  # Ubah status menjadi aktif

            # print(konten)
            konten.deleted_at = None
            konten.save()
            return JsonResponse({'message': 'Data berhasil diunarsipkan'}, status=200)
        except Data_konten.DoesNotExist:
            return JsonResponse({'error': 'Data jenjang tidak ditemukan'}, status=404)
    else:
        return JsonResponse({'error': 'Metode request tidak diizinkan'}, status=405)
    



