from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from sipandu_app.models import Data_slider, Master_sekolah

def Indexslider(request):
    if request.method == 'POST':
        slider_sekolah = request.POST.get('slider_sekolah')
        gambar = request.FILES.get('image_slider1')
        judul = request.POST.get('judul')
        slider_status = request.POST.get('slider_status') == 'True'

        dt_slider = Data_slider.objects.create(
            slider_sekolah_id=slider_sekolah,
            gambar=gambar,
            judul=judul,
            slider_status=slider_status
        )

        return redirect('sipandu_admin:index_slider')
    else:
        data_sekolah = Master_sekolah.objects.all()
        dt_slider = Data_slider.objects.all()

        return render(request, 'admin/data/slider.html', {"data_slider": dt_slider, "data_sekolah": data_sekolah})

def Tambahslider(request):
    if request.method == 'POST':
        slider_sekolah = request.POST.get('slider_sekolah')
        gambar = request.FILES.get('image_slider1')
        judul = request.POST.get('judul')
        slider_status = request.POST.get('slider_status') == 'True'

        dt_slider = Data_slider.objects.create(
            slider_sekolah_id=slider_sekolah,
            gambar=gambar,
            judul=judul,
            slider_status=slider_status
        )

        return redirect('sipandu_admin:index_slider')
    else:
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/tambah_slider.html', {"data_sekolah": data_sekolah})

def Editslider(request, id_data_slider):
    dt_slider = get_object_or_404(Data_slider, id_data_slider=id_data_slider)
    if request.method == 'POST':
        slider_sekolah = request.POST.get('slider_sekolah')
        gambar = request.FILES.get('image_slider1')
        judul = request.POST.get('judul')
        slider_status = request.POST.get('slider_status') == 'True'

        dt_slider.slider_sekolah_id = slider_sekolah
        dt_slider.gambar = gambar
        dt_slider.judul = judul
        dt_slider.slider_status = slider_status

        dt_slider.save()

        return redirect('sipandu_admin:index_slider')
    else:
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/edit_slider.html', {"dt_slider": dt_slider, "data_sekolah": data_sekolah})

def Deleteslider(request, id_data_slider):
    dt_slider = get_object_or_404(Data_slider, id_data_slider=id_data_slider)
    dt_slider.delete()

    data = {
        'status': 'success',
        'message': 'Data slider berhasil dihapus'
    }
    return JsonResponse(data, status=200)
