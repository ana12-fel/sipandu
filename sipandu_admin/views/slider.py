from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from sipandu_app.models import Data_slider, Master_sekolah
from django.contrib.auth.decorators import login_required

@login_required(login_url='sipandu_admin:login_index')
def Indexslider(request):
    if request.method == 'POST':
        slider_sekolah = request.POST.get('slider_sekolah')
        gambar = request.FILES.get('image_slider1')
        judul = request.POST.get('judul')
        slider_status = request.POST.get('status')
        print(slider_status)

        dt_slider = Data_slider.objects.create(
            slider_sekolah_id=slider_sekolah,
            gambar=gambar,
            judul=judul,
            slider_status=slider_status
        )

        return redirect('sipandu_admin:index_slider')
    else:
        data_sekolah = Master_sekolah.objects.all()
        dt_slider = Data_slider.objects.by_hakakses(request.user).all()

        return render(request, 'admin/data/slider.html', {"data_slider": dt_slider, "data_sekolah": data_sekolah})

@login_required(login_url='sipandu_admin:login_index')
def Tambahslider(request):
    if request.method == 'POST':
        slider_sekolah = request.POST.get('slider_sekolah')
        gambar = request.FILES.get('image_slider1')
        judul = request.POST.get('judul')
        slider_status = request.POST.get('status')

        dt_slider = Data_slider.objects.create(
            slider_sekolah_id=slider_sekolah,
            gambar=gambar,
            judul=judul,
            slider_status=slider_status
        )

        return redirect('sipandu_admin:index_slider')
    else:
        data_sekolah = Master_sekolah.objects.by_hakakses(request.user).all()
        return render(request, 'admin/data/tambah_slider.html', {"data_sekolah": data_sekolah})

@login_required(login_url='sipandu_admin:login_index')
def Editslider(request, id_data_slider):
    dt_slider = get_object_or_404(Data_slider, id_data_slider=id_data_slider)
    if request.method == 'POST':
        slider_sekolah = request.POST.get('slider_sekolah')
        gambar = request.FILES.get('image_slider1')
        judul = request.POST.get('judul')
        slider_status = request.POST.get('status') 

        dt_slider.slider_sekolah_id = slider_sekolah
        dt_slider.gambar = gambar
        dt_slider.judul = judul
        dt_slider.slider_status = slider_status

        dt_slider.save()

        return redirect('sipandu_admin:index_slider')
    else:
        data_sekolah = Master_sekolah.objects.by_hakakses(request.user).all()
        return render(request, 'admin/data/edit_slider.html', {"dt_slider": dt_slider, "data_sekolah": data_sekolah})

@login_required(login_url='sipandu_admin:login_index')
def Deleteslider(request, id_data_slider):
    dt_slider = get_object_or_404(Data_slider, id_data_slider=id_data_slider)
    dt_slider.delete()

    data = {
        'status': 'success',
        'message': 'Data slider berhasil dihapus'
    }
    return JsonResponse(data, status=200)
