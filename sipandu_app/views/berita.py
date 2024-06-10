from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render,redirect, get_object_or_404
from sipandu_app.models import Data_konten as dt_konten, Transanksi_situs as dt_situs
# from support.support_function import JENJANG, TEMPLATE_NAME


def index_berita(request):
   
   # data_fasilitas = get_object_or_404(dt_konten, konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian__icontains='Fasilitas' )
   # print(data_fasilitas)
   data_berita = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita')
   data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
   
   data = {
      'data_berita' : data_berita,
      'data_berita_latest' : data_berita_latest,
   }
   return render(request, f'{request.jenjang}/{request.template_name}/berita/berita.html', data )

def detail(request, id_data_konten):

   detail_berita = get_object_or_404(dt_konten, konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian__icontains='Berita', id_data_konten=id_data_konten )
   data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
   
   data = {
      'detail_berita' : detail_berita,
      'data_berita_latest' : data_berita_latest,
   }
   return render(request, f'{request.jenjang}/{request.template_name}/berita/detail.html', data )

def BursaKerja(request):
   bursa_kerja = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Bursa Kerja')
   data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
   data = {
      'bursa_kerja' : bursa_kerja,
      'data_berita_latest' : data_berita_latest,
   }

   return render(request, f'{request.jenjang}/{request.template_name}/berita/bursa_kerja.html', data )

def detail_kerja(request, id_data_konten):

   data_detail_kerja = get_object_or_404(dt_konten, konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian__icontains='Bursa Kerja', id_data_konten=id_data_konten )
   data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
   
   data = {
      'data_detail_kerja' : data_detail_kerja,
      'data_berita_latest' : data_berita_latest,
   }
   return render(request, f'{request.jenjang}/{request.template_name}/berita/detail_kerja.html', data )

def Beasiswa(request):
   data_beasiswa = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Beasiswa')
   print(data_beasiswa)
   data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
   data = {
      'data_beasiswa' : data_beasiswa,
      'data_berita_latest' : data_berita_latest,
   }

   return render(request, f'{request.jenjang}/{request.template_name}/berita/beasiswa.html', data )

def Detail_beasiswa(request, id_data_konten):

   data_detail_beasiswa = get_object_or_404(dt_konten, konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian__icontains='Beasiswa', id_data_konten=id_data_konten )
   
   data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
   
   data = {
      'data_detail_beasiswa' : data_detail_beasiswa,
      'data_berita_latest' : data_berita_latest,
   }
   return render(request, f'{request.jenjang}/{request.template_name}/berita/detail_beasiswa.html', data )

def kegiatan(request):
   data_kegiatan = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Kegiatan')
   
   data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
   data = {
      'data_kegiatan' : data_kegiatan,
      'data_berita_latest' : data_berita_latest,
   }

   return render(request, f'{request.jenjang}/{request.template_name}/berita/kegiatan.html', data)

def Detail_kegiatan(request, id_data_konten):

   data_detail_kegiatan = get_object_or_404(dt_konten, konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian__icontains='Kegiatan', id_data_konten=id_data_konten )
   data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
   
   data = {
      'data_detail_kegiatan' : data_detail_kegiatan,
      'data_berita_latest' : data_berita_latest,
      
   }
   return render(request, f'{request.jenjang}/{request.template_name}/berita/detail_kegiatan.html', data )








def beritasmp(request):
   return render(request, f'{request.jenjang}/{request.template_name}/berita/berita.html', )
def pengumuman(request):
   return render(request, f'{request.jenjang}/{request.template_name}/berita/pengumuman.html', )
def bursa(request):
   return render(request, f'{request.jenjang}/{request.template_name}/berita/bursa_kerja.html', )
