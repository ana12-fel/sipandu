from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from sipandu_app.models import Data_konten, Master_kategori,Master_sekolah, Sub_kategori
from django.urls import reverse
from django.conf import settings
import os
from django.utils import timezone

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
        data_konten = Data_konten.objects.all()
        
        return render(request, 'admin/data/konten.html', {"data_sub_kategori": data_sub_kategori, "data_kategori": data_kategori, "data_konten": data_konten, "data_sekolah": data_sekolah})

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
        data_sekolah = Master_sekolah.objects.all()
        data_kategori = Master_kategori.objects.all()
        data_sub_kategori = Sub_kategori.objects.all()
        data_konten = Data_konten.objects.all()
        return render(request, 'admin/data/tambah_konten.html', {'data_kategori': data_kategori, 'data_sub_kategori': data_sub_kategori, 'data_konten': data_konten, 'data_sekolah' : data_sekolah})
       
def EditKonten(request, id_data_konten):
    if request.method == 'POST':
        dt_konten = get_object_or_404(Data_konten, id_data_konten=id_data_konten)
        
        konten_sekolah = request.POST.get('konten_sekolah')
        konten_kategori = request.POST.get('konten_kategori')
        konten_sub_kategori = request.POST.get('konten_sub_kategori')
        judul = request.POST.get('judul')
        is_active = request.POST.get('status') == 'True'
        isi_konten = request.POST.get('isi_konten')
        konten_image = request.FILES.get('konten_image')
        konten_tag = request.POST.get('konten_tag')
        
        dt_konten.konten_sekolah = Master_sekolah.objects.get(sekolah_id=konten_sekolah)
        dt_konten.konten_kategori = Master_kategori.objects.get(kategori_id=konten_kategori)
        dt_konten.konten_sub_kategori = Sub_kategori.objects.get(sub_kategori_id=konten_sub_kategori)
        dt_konten.judul = judul
        dt_konten.status = is_active
        dt_konten.isi_konten = isi_konten
        if konten_image:
            dt_konten.konten_image = konten_image
        dt_konten.konten_tag = konten_tag

        dt_konten.save()

        return redirect('sipandu_admin:index_konten')
    else:
        dt_konten = get_object_or_404(Data_konten, id_data_konten=id_data_konten)
        data_sekolah = Master_sekolah.objects.all()
        data_kategori = Master_kategori.objects.all()
        data_sub_kategori = Sub_kategori.objects.all()
        return render(request, 'admin/data/edit_konten.html', {
            "dt_konten": dt_konten,
            "id_data_konten": id_data_konten,
            "data_sekolah": data_sekolah,
            "data_kategori": data_kategori,
            "data_sub_kategori": data_sub_kategori
        })

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
    



