from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from sipandu_app.models import Data_konten, Master_kategori, Sub_kategori
from django.urls import reverse

def IndexKonten(request):
    if request.method == 'POST':
        konten_kategori = request.POST.get ('konten_kategori')
        konten_sub_kategori = request.POST.get ('konten_sub_kategori')
        judul = request.POST.get ('judul')
        status = request.POST.get ('status')

        print(konten_kategori, konten_sub_kategori)
        dt_konten = Data_konten.objects.create(
                                             konten_kategori=Master_kategori.objects.get(kategori_id = konten_kategori),
                                             konten_sub_kategori=Sub_kategori.objects.get(sub_kategori_id = konten_sub_kategori),
                                             judul=judul,
                                             status=status)

        print(konten_kategori,konten_sub_kategori,judul,status)

        return redirect('sipandu_admin:index_konten')
    
    else:
        data_sub_kategori = Sub_kategori.objects.all()
        data_kategori = Master_kategori.objects.all()
        data_konten = Data_konten.objects.all()
        
        return render(request, 'admin/data/konten.html', {"data_sub_kategori" : data_sub_kategori, "data_kategori": data_kategori, "data_konten" : data_konten})
    
def TambahKonten(request):
    if request.method == 'POST':
        konten_kategori = request.POST.get ('konten_kategori')
        konten_sub_kategori = request.POST.get ('konten_sub_kategori')
        judul = request.POST.get ('judul')
        status = request.POST.get ('status')

        print(konten_kategori, konten_sub_kategori)
        dt_konten = Data_konten.objects.create(
                                             konten_kategori=Master_kategori.objects.get(kategori_id = konten_kategori),
                                             konten_sub_kategori=Sub_kategori.objects.get(sub_kategori_id = konten_sub_kategori),
                                             judul=judul,
                                             status=status)

        print(konten_kategori,konten_sub_kategori,judul,status)
        dt_konten.save()

        return redirect('sipandu_admin:index_konten')

    else:
        data_kategori = Master_kategori.objects.all()
        data_sub_kategori = Sub_kategori.objects.all()
        data_konten = Data_konten.objects.all()
        return render(request, 'admin/data/tambah_konten.html', {'data_kategori': data_kategori, 'data_sub_kategori': data_sub_kategori, 'data_konten': data_konten})
       
def EditKonten(request, id_data_konten):
    if request.method == 'POST':
        dt_konten = Data_konten.objects.get(id_data_konten=id_data_konten)

        konten_kategori = request.POST.get ('konten_kategori')
        konten_sub_kategori = request.POST.get ('konten_sub_kategori')
        judul = request.POST.get('judul')
        status = request.POST.get('status')

        dt_konten.konten_kategori=Master_kategori.objects.get(kategori_id = konten_kategori)
        dt_konten.konten_sub_kategori=Sub_kategori.objects.get(sub_kategori_id = konten_sub_kategori)
        dt_konten.judul=judul
        dt_konten.status=status

        dt_konten.save()

        return redirect('sipandu_admin:index_konten')
    else:
        dt_konten = Data_konten.objects.get(id_data_konten=id_data_konten)
        return render(request, 'admin/data/edit_konten.html', {"dt_konten": dt_konten, "id_data_konten": id_data_konten })
    

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
    



