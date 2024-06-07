from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse, HttpResponse
from sipandu_app.models import Data_galeri,Master_sekolah
from django.urls import reverse

def Indexgaleri(request):
    if request.method == 'POST':
        galeri_sekolah = request.POST.get('galeri_sekolah')
        gambar = request.FILES.get('image_galeri')
        video = request.POST.get('video_galeri')

        print(galeri_sekolah)
        dt_galeri = Data_galeri.objects.create(
                                                galeri_sekolah_id=galeri_sekolah, 
                                                gambar=gambar, 
                                                video=video)
        
        print(galeri_sekolah,gambar,video)


        return redirect('sipandu_admin:index_galeri')
    
    else:
        data_sekolah = Master_sekolah.objects.all()
        data_galeri = Data_galeri.objects.all()
        
        return render(request, 'admin/data/galeri.html', {"data_galeri" : data_galeri, "data_sekolah" : data_sekolah})

def Tambahgaleri(request):
    if request.method == 'POST':
        galeri_sekolah = request.POST.get('galeri_sekolah')
        gambar = request.FILES.get('image_galeri')
        video = request.POST.get('video_galeri')
        print(request.POST,request.FILES)

        print(galeri_sekolah)
        dt_galeri = Data_galeri.objects.create( 
                                                galeri_sekolah_id=galeri_sekolah, 
                                                gambar=gambar, 
                                                video=video)
                                            
        dt_galeri.save()

        return redirect('sipandu_admin:index_galeri')

    else:
        dt_galeri = Data_galeri.objects.all()
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/tambah_galeri.html', {"data_galeri": dt_galeri, "data_sekolah" : data_sekolah})

def Editgaleri(request, id_data_galeri):
    dt_galeri = get_object_or_404(Data_galeri, id_data_galeri=id_data_galeri)
    if request.method == 'POST':
        galeri_sekolah = request.POST.get('galeri_sekolah')
        gambar = request.FILES.get('image_galeri')
        video = request.POST.get('video_galeri')

        # Mengambil objek yang sudah ada dan mengubah nilainya
        dt_galeri.galeri_sekolah_id = galeri_sekolah
        dt_galeri.gambar = gambar
        dt_galeri.video = video

        # Menyimpan perubahan pada objek yang sudah ada
        dt_galeri.save()
        
        return redirect('sipandu_admin:index_galeri')

    else:
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/edit_galeri.html', {"dt_galeri": dt_galeri, "data_sekolah" : data_sekolah})


def Deletegaleri(request, id_data_galeri):
    try:
        dt_galeri = get_object_or_404(Data_galeri, id_data_galeri=id_data_galeri)
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
