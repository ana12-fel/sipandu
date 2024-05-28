from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse, HttpResponse
from sipandu_app.models import Data_slider,Master_sekolah
from django.urls import reverse

def Indexslider(request):
    if request.method == 'POST':
        slider_sekolah = request.POST.get('slider_sekolah')
        gambar1 = request.FILES.get('image_slider1')
        gambar2 = request.FILES.get('image_slider2')
        gambar3 = request.FILES.get('image_slider3')
        judul1 = request.POST.get('judul1')
        judul2 = request.POST.get('judul2')
        judul3 = request.POST.get('judul3')

        print(slider_sekolah)
        dt_slider = Data_slider.objects.create(
                                                slider_sekolah_id=slider_sekolah, 
                                                gambar1=gambar1, 
                                                gambar2=gambar2,
                                                gambar3=gambar3,
                                                judul1=judul1,
                                                judul2=judul2,
                                                judul3=judul3)
        
        print(slider_sekolah,gambar1,gambar2,gambar3,judul1,judul2,judul3)


        return redirect('sipandu_admin:index_slider')
    
    else:
        data_sekolah = Master_sekolah.objects.all()
        dt_slider = Data_slider.objects.all()
        
        return render(request, 'admin/data/slider.html', {"data_slider" : dt_slider, "data_sekolah" : data_sekolah})

def Tambahslider(request):
    if request.method == 'POST':
        slider_sekolah = request.POST.get('slider_sekolah')
        gambar1 = request.FILES.get('image_slider1')
        gambar2 = request.FILES.get('image_slider2')
        gambar3 = request.FILES.get('image_slider3')
        judul1 = request.POST.get('judul1')
        judul2 = request.POST.get('judul2')
        judul3 = request.POST.get('judul3')
        print(request.POST,request.FILES)

        print(slider_sekolah)
        dt_slider = Data_slider.objects.create( 
                                                slider_sekolah_id=slider_sekolah, 
                                                gambar1=gambar1, 
                                                gambar2=gambar2,
                                                gambar3=gambar3,
                                                judul1=judul1,
                                                judul2=judul2,
                                                judul3=judul3)
                                            
        dt_slider.save()

        return redirect('sipandu_admin:index_slider')

    else:
        dt_slider = Data_slider.objects.all()
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/tambah_slider.html', {"data_slider": dt_slider, "data_sekolah" : data_sekolah})

def Editslider(request, id_data_slider):
    dt_slider = get_object_or_404(Data_slider, id_data_slider=id_data_slider)
    if request.method == 'POST':
        slider_sekolah = request.POST.get('slider_sekolah')
        gambar1 = request.FILES.get('image_slider1')
        gambar2 = request.FILES.get('image_slider2')
        gambar3 = request.FILES.get('image_slider3')
        judul1 = request.POST.get('judul1')
        judul2 = request.POST.get('judul2')
        judul3 = request.POST.get('judul3')
        

        # Mengambil objek yang sudah ada dan mengubah nilainya
        dt_slider.slider_sekolah_id = slider_sekolah
        dt_slider.gambar1 = gambar1
        dt_slider.gambar2 = gambar2
        dt_slider.gambar3 = gambar3
        dt_slider.judul1 = judul1
        dt_slider.judul2 = judul2
        dt_slider.judul3 = judul3

        # Menyimpan perubahan pada objek yang sudah ada
        dt_slider.save()
        
        return redirect('sipandu_admin:index_slider')

    else:
        dt_slider = get_object_or_404(Data_slider, id_data_slider=id_data_slider)
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/edit_slider.html', {"dt_slider": dt_slider, "data_sekolah" : data_sekolah})


def Deleteslider(request, id_data_slider):
    try:
        dt_slider = get_object_or_404(Data_slider, id_data_slider=id_data_slider)
        dt_slider.delete()
        
        data = {
            'status': 'success',
            'message': 'Data slider berhasil dihapus'
        }
        return JsonResponse(data, status=200)
    except Data_slider.DoesNotExist:
        data = {
            'status': 'error',
            'message': 'Data slider gagal dihapus, data galeri tidak ditemukan'
        }
        return JsonResponse(data, status=400)
