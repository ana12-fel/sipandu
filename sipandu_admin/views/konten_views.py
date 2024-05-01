from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from sipandu_app.models import Data_konten, Master_kategori, Sub_kategori
from django.urls import reverse

def IndexKonten(request):
    if request.method == 'POST':
        created_at = request.POST.get ('created_at')
        kategori_id_id = request.POST.get ('kategori_id_id')
        sub_kategori_id_id = request.POST.get ('sub_kategori_id_id')
        judul = request.POST.get ('judul')
        status = request.POST.get ('status')

        dt_konten = Data_konten.objects.create(
                                             created_at=created_at,
                                             kategori_id_id=kategori_id_id,
                                             sub_kategori_id_id=sub_kategori_id_id,
                                             judul=judul,
                                             status=status)

        print(created_at,kategori_id_id,sub_kategori_id_id,judul,status)

        return redirect('sipandu_admin:index_konten')
    
    else:
        data_sub_kategori = Sub_kategori.objects.all()
        data_kategori = Master_kategori.objects.all()
        data_konten = Data_konten.objects.all()
        
        return render(request, 'admin/data/konten.html', {"data_sub_kategori" : data_sub_kategori, "data_kategori": data_kategori, "data_konten" : data_konten})
    
def TambahKonten(request):
    if request.method == 'POST':
        # Ambil data yang di-post dari form
        created_at = request.POST('created_at')
        kategori_id_id = request.POST('kategori_uraian')
        sub_kategori_id_id = request.POST('sub_kategori_uraian')
        judul = request.POST('judul')
        status = request.POST('status')

        # Buat objek konten baru
        dt_konten = Data_konten.objects.create(
                                             created_at=created_at,
                                             kategori_id_id=kategori_id_id,
                                             sub_kategori_id_id=sub_kategori_id_id,
                                             judul=judul,
                                             status=status)

        # Simpan objek konten baru ke database
        dt_konten.save()

        # Redirect ke halaman yang sesuai setelah berhasil menambahkan konten
        return redirect('sipandu_admin:index_konten')

    else:
        # Jika bukan metode POST, tampilkan form tambah konten
        data_kategori = Master_kategori.objects.all()
        data_sub_kategori = Sub_kategori.objects.all()
        data_konten = Data_konten.objects.all()
        return render(request, 'admin/data/tambah_konten.html', {'data_kategori': data_kategori, 'data_sub_kategori': data_sub_kategori, 'data_konten': data_konten})
       
def EditKonten(request, id_data_konten):
    if request.method == 'GET':
        data_kategori = Master_kategori.objects.all()
        data_sub_kategori = Sub_kategori.objects.all()
        
        return render(request, 'admin/data/edit_konten.html', {'dt_konten': dt_konten, 'data_kategori': data_kategori, 'data_sub_kategori': data_sub_kategori})
    
    if request.method == 'POST':
        try:
            dt_konten = Data_konten.objects.get(id_data_konten=id_data_konten)
            
            created_at = request.POST.get('created_at')
            kategori_id = request.POST.get('kategori_id')
            sub_kategori_id = request.POST.get('sub_kategori_id')
            judul = request.POST.get('judul')
            status = request.POST.get('status')

            # Perbarui nilai atribut konten
            dt_konten.created_at = created_at
            dt_konten.kategori_id = kategori_id
            dt_konten.sub_kategori_id = sub_kategori_id
            dt_konten.judul = judul
            dt_konten.status = status

            # Simpan perubahan
            dt_konten.save()

            return redirect('sipandu_admin:index_konten')
        except Data_konten.DoesNotExist:
            pass
    

    

def DeleteKonten(request, id_data_konten):
    try:
        dt_konten = get_object_or_404(Data_konten, id_data_konten=id_data_konten)
        dt_konten.delete()

        Data = {
                'status': 'success',
                'message': 'data konten berhasil dihapus'   
        }
        return JsonResponse(data, status=200)
    
    except Data_konten.DoesNotExist:
        data = {
                'status': 'success',
                'message': 'data konten gagal di hapus, data konten tidak ditemukan'   
        }
        return JsonResponse(data, status=400)
    



