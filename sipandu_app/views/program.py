

from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render,redirect, get_object_or_404
from sipandu_app.models import Data_konten as dt_konten, Transanksi_situs as dt_situs
# from support.support_function import JENJANG, TEMPLATE_NAME
from django.core.paginator import Paginator

   


def ekstrakulikuler(request):
   
   # data_fasilitas = get_object_or_404(dt_konten, konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian__icontains='Fasilitas' )
   # print(data_fasilitas)
   ekstrakulikuler_list = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Ekstrakulikuler')
   data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]

   paginator = Paginator(ekstrakulikuler_list, 8)  # 3 berita per halaman
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)

   data = {
      'page_obj': page_obj,
      'data_berita_latest' : data_berita_latest,
   }
   return render(request, f'{request.jenjang}/{request.template_name}/program/ekstrakulikuler.html', data )

def detail_ekstrakulikuler(request, id_data_konten):

   data_detail_ekstrakulikuler = get_object_or_404(dt_konten, konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian__icontains='Ekstrakulikuler', id_data_konten=id_data_konten )
   data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
   # print(data_detail_fasilitas)
   data = {
      'data_detail_ekstrakulikuler' : data_detail_ekstrakulikuler,
      'data_berita_latest' :data_berita_latest,
   }
   return render(request, f'{request.jenjang}/{request.template_name}/program/detail_ekstrakulikuler.html', data)
