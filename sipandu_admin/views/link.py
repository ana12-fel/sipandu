from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from sipandu_app.models import Data_link, Master_sekolah

def IndexLink(request):
    if request.method == 'POST':
        link_sekolah = request.POST.get('link_sekolah')
        nama_link = request.POST.get('nama_link')
        link = request.POST.get('link')

        Data_link.objects.create(
            link_sekolah=link_sekolah,
            nama_link=nama_link,
            link=link
        )

        print(link_sekolah, nama_link, link)
        return redirect('index_link')
    else:
        dt_link = Data_link.objects.all()
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/link_sekolah.html', {"data_link": dt_link, "data_sekolah": data_sekolah})

def TambahLink(request):
    if request.method == 'POST':
        link_sekolah = request.POST.get('link_sekolah')
        nama_link = request.POST.get('nama_link')
        link = request.POST.get('link')

        Data_link.objects.create(
            link_sekolah=link_sekolah,
            nama_link=nama_link,
            link=link
        )

        print(link_sekolah, nama_link, link)
        return redirect('index_link')
    else:
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/tambah_link.html', {"data_sekolah": data_sekolah})

def EditLink(request, id_data_link):
    dt_link = get_object_or_404(Data_link, pk=id_data_link)

    if request.method == 'POST':
        dt_link.link_sekolah = request.POST.get('link_sekolah')
        dt_link.nama_link = request.POST.get('nama_link')
        dt_link.link = request.POST.get('link')
        dt_link.save()

        print(dt_link.link_sekolah, dt_link.nama_link, dt_link.link)
        return redirect('index_link')
    else:
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/edit_link.html', {"data_link": dt_link, "data_sekolah": data_sekolah})

def DeleteLink(request, id_data_link):
    try:
        dt_link = get_object_or_404(Data_link, pk=id_data_link)
        dt_link.delete()
        
        data = {
            'status': 'success',
            'message': 'Data link berhasil dihapus'
        }
        return JsonResponse(data, status=200)
    except Data_link.DoesNotExist:
        data = {
            'status': 'error',
            'message': 'Data link tidak ditemukan'
        }
        return JsonResponse(data, status=400)
