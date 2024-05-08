from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from sipandu_app.models import Data_konten, Master_kategori,Master_sekolah, Sub_kategori
from django.urls import reverse

def IndexKonten(request):
    if request.method == 'POST':
        konten_sekolah = request.POST.get('konten_sekolah')
        konten_kategori = request.POST.get ('konten_kategori')
        konten_sub_kategori = request.POST.get ('konten_sub_kategori')
        judul = request.POST.get ('judul')
        status = request.POST.get ('status')
        isi_konten = request.POST.get('isi_konten')
        konten_deskripsi = request.POST.get('konten_deskripsi')
        konten_image = request.FILES.get('konten_image')
        konten_tag = request.POST.get('konten_tag')


        print(konten_kategori, konten_sub_kategori, konten_sekolah)
        dt_konten = Data_konten.objects.create(
                                            konten_sekolah=Master_sekolah.objects.get(sekolah_id = konten_sekolah), 
                                            konten_kategori=Master_kategori.objects.get(kategori_id = konten_kategori),
                                            konten_sub_kategori=Sub_kategori.objects.get(sub_kategori_id = konten_sub_kategori),
                                            judul=judul,
                                            status=status,
                                            isi_konten=isi_konten,
                                            konten_deskripsi=konten_deskripsi,
                                            konten_image=konten_image,
                                            konten_tag=konten_tag)
        
        print(konten_sekolah,konten_kategori,konten_sub_kategori,judul,status,isi_konten,konten_deskripsi,konten_image,konten_tag)


        return redirect('sipandu_admin:index_konten')
    
    else:
        data_sekolah = Master_sekolah.objects.all()
        data_sub_kategori = Sub_kategori.objects.all()
        data_kategori = Master_kategori.objects.all()
        data_konten = Data_konten.objects.all()
        
        return render(request, 'admin/data/konten.html', {"data_sub_kategori" : data_sub_kategori, "data_kategori": data_kategori, "data_konten" : data_konten, "data_sekolah" : data_sekolah})
    
def TambahKonten(request):
    if request.method == 'POST':
        konten_sekolah = request.POST.get('konten_sekolah')
        konten_kategori = request.POST.get ('konten_kategori')
        konten_sub_kategori = request.POST.get ('konten_sub_kategori')
        judul = request.POST.get ('judul')
        status = request.POST.get ('status')
        isi_konten = request.POST.get('isi_konten')
        konten_deskripsi = request.POST.get('konten_deskripsi')
        konten_image = request.FILES.get('konten_image')
        konten_tag = request.POST.get('konten_tag')
        print(request.POST)


        print(konten_kategori, konten_sub_kategori, konten_sekolah, isi_konten)
        dt_konten = Data_konten.objects.create(
                                            konten_sekolah_id=konten_sekolah, 
                                            konten_kategori=Master_kategori.objects.get(kategori_id = konten_kategori),
                                            konten_sub_kategori=Sub_kategori.objects.get(sub_kategori_id = konten_sub_kategori),
                                            judul=judul,
                                            status=status,
                                            isi_konten=isi_konten,
                                            konten_deskripsi=konten_deskripsi,
                                            konten_image=konten_image,
                                            konten_tag=konten_tag)

       
        dt_konten.save()

        return redirect('sipandu_admin:index_konten')

    else:
        data_sekolah = Master_sekolah.objects.all()
        data_kategori = Master_kategori.objects.all()
        data_sub_kategori = Sub_kategori.objects.all()
        data_konten = Data_konten.objects.all()
        return render(request, 'admin/data/tambah_konten.html', {'data_kategori': data_kategori, 'data_sub_kategori': data_sub_kategori, 'data_konten': data_konten, 'data_sekolah' : data_sekolah})
       
def EditKonten(request, id_data_konten):
    if request.method == 'POST':
        dt_konten = Data_konten.objects.get(id_data_konten=id_data_konten)

        id_data_konten = request.POST.get('id_data_konten')
        konten_sekolah = request.POST.get('konten_sekolah')
        konten_kategori = request.POST.get ('konten_kategori')
        konten_sub_kategori = request.POST.get ('konten_sub_kategori')
        judul = request.POST.get ('judul')
        status = request.POST.get ('status')
        isi_konten = request.POST.get('isi_konten')
        konten_deskripsi = request.POST.get('konten_deskripsi')
        konten_image = request.FILES.get('konten_image')
        konten_tag = request.POST.get('konten_tag')
        print(request.POST)

        dt_konten.konten_sekolah=Master_sekolah.objects.get(sekolah_id = konten_sekolah)
        dt_konten.konten_kategori=Master_kategori.objects.get(kategori_id = konten_kategori)
        dt_konten.konten_sub_kategori=Sub_kategori.objects.get(sub_kategori_id = konten_sub_kategori)
        dt_konten.judul=judul
        dt_konten.status=status
        dt_konten.isi_konten=isi_konten
        dt_konten.konten_deskripsi=konten_deskripsi
        dt_konten.konten_image=konten_image
        dt_konten.konten_tag=konten_tag

        dt_konten.save()

        return redirect('sipandu_admin:index_konten')
    else:
        dt_konten = get_object_or_404( Data_konten , id_data_konten=id_data_konten)
        data_sekolah = Master_sekolah.objects.all()
        data_kategori = Master_kategori.objects.all()
        data_sub_kategori = Sub_kategori.objects.all()
        return render(request, 'admin/data/edit_konten.html', {"dt_konten": dt_konten, "id_data_konten": id_data_konten, "data_sekolah" : data_sekolah, "data_kategori" : data_kategori, "data_sub_kategori" : data_sub_kategori})


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
    



