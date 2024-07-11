from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404
from sipandu_app.models import Data_konten as dt_konten


def index_jurusan(request,nama_jurusan):
    # data_ipa = get_object_or_404(dt_konten, konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian__icontains='bahasa')
    data_ipa = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian__icontains=nama_jurusan, deleted_at=None, status=True)
    data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
    
    nm_jurusan = 'Nama Jurusan'
    for x in data_ipa:
        nm_jurusan = x.judul

    data = {
        'data_ipa': data_ipa,
        'data_berita_latest': data_berita_latest,
        'nm_jurusan':nm_jurusan
    }
    return render(request, f'{request.jenjang}/{request.template_name}/jurusan/index_jurusan.html', data)

def ipa(request):
    # Filter for content with specific criteria (e.g., title contains 'IPA')
    data_ipa = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='IPA')
    data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
    data = {
        'data_ipa': data_ipa,
        'data_berita_latest': data_berita_latest
    }
    return render(request, f'{request.jenjang}/{request.template_name}/jurusan/ipa.html', data)



def ips(request):
    # Filter for content with specific criteria (e.g., title contains 'IPS')
    data_ips = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='IPS')
    data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
    data = {
        'data_ips': data_ips,
        'data_berita_latest': data_berita_latest
    }
    return render(request, f'{request.jenjang}/{request.template_name}/jurusan/ips.html', data)

def bahasa(request):
   data_bahasa = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='bahasa').first()
   data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
   data = {
      'data_bahasa': data_bahasa,
      'data_berita_latest': data_berita_latest
   }
   return render(request, f'{request.jenjang}/{request.template_name}/jurusan/bahasa.html', data)
