from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse, HttpResponse
from sipandu_app.models import Data_galeri,Master_sekolah
from django.urls import reverse

def Indexgaleri(request):
    if request.method == 'POST':
        galeri_sekolah = request.POST.get('galeri_sekolah')
        galeri_image = request.FILES.get('galeri_image')
        video = request.FILES.get('video_konten')
        dt_galeri = Data_galeri.objects.create( galeri=galeri_image)

        print(video, galeri_image, galeri_sekolah)

        dt_galeri = Data_galeri.objects.create(
                                                galeri_sekolah=Master_sekolah.objects.get(sekolah_id=galeri_sekolah),
                                                gambar=galeri_image,
                                                video=video)

        return redirect('sipandu_admin:index_galeri')
    else:
        dt_galeri = Data_galeri.objects.all()
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/galeri.html', {"data_galeri": dt_galeri, "data_sekolah" : data_sekolah})

def Tambahgaleri(request):
    if request.method == 'POST':
        galeri_sekolah = request.POST.get('galeri_sekolah')
        galeri_image = request.FILES.get('galeri_image')
        video = request.FILES.get('video_konten')
        dt_galeri = Data_galeri.objects.create( galeri=galeri_image)

        

        dt_galeri = Data_galeri.objects.create(
                                                 galeri_sekolah=Master_sekolah.objects.get(sekolah_id = galeri_sekolah),
                                                 gambar=galeri_image,
                                                 video=video)
                                            
        dt_galeri.save()

        return redirect('sipandu_admin:index_galeri')

    else:
        dt_galeri = Data_galeri.objects.all()
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/tambah_galeri.html', {"data_galeri": dt_galeri, "data_sekolah" : data_sekolah})

def Editgaleri(request):
    if request.method == 'POST':
        galeri_sekolah = request.POST.get('galeri_sekolah')
        galeri_image = request.FILES.get('galeri_image')
        video = request.FILES.get('video_konten')
        dt_galeri = Data_galeri.objects.create( galeri=galeri_image)


        dt_galeri = Data_galeri.objects.create(
                                                 galeri_sekolah=Master_sekolah.objects.get(sekolah_id = galeri_sekolah),
                                                 gambar=galeri_image,
                                                 video=video)
                                            
        dt_galeri.save()

        return redirect('sipandu_admin:index_galeri')

    else:
        dt_galeri = Data_galeri.objects.all()
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/galeri.html', {"data_galeri": dt_galeri, "data_sekolah" : data_sekolah})
    

def Deletegaleri(request, id_data_galeri):
    try:
        dt_galeri = get_object_or_404(Data_galeri, galeri_id=id_data_galeri)
        dt_galeri.delete()
        
        data = {
            'status': 'success',
            'message': 'Data galeri berhasil dihapus'
        }
        return JsonResponse(data, status=200)
    except Data_galeri.DoesNotExist:
        data = {
            'status': 'error',
            'message': 'Data galeri gagal dihapus, data galeri tidak ditemukan'
        }
        return JsonResponse(data, status=400)
