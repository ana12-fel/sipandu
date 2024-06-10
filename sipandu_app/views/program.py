

from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render,redirect, get_object_or_404
from sipandu_app.models import Data_konten as dt_konten, Transanksi_situs as dt_situs
# from support.support_function import JENJANG, TEMPLATE_NAME


   


def ekstrakulikuler(request):
   
   # data_fasilitas = get_object_or_404(dt_konten, konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian__icontains='Fasilitas' )
   # print(data_fasilitas)
   ekstrakulikuler_list = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Ekstrakulikuler')
   data = {
      'ekstrakulikuler_list' : ekstrakulikuler_list,
   }
   return render(request, f'{request.jenjang}/{request.template_name}/program/ekstrakulikuler.html', data )

def detail_ekstrakulikuler(request, id_data_konten):

   data_detail_ekstrakulikuler = get_object_or_404(dt_konten, konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian__icontains='Ekstrakulikuler', id_data_konten=id_data_konten )
   # print(data_detail_fasilitas)
   data = {
      'data_detail_ekstrakulikuler' : data_detail_ekstrakulikuler,
   }
   return render(request, f'{request.jenjang}/{request.template_name}/program/detail_ekstrakulikuler.html', data)
