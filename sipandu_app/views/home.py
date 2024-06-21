from django.shortcuts import render
from django.shortcuts import render,redirect
from sipandu_app.models import Data_konten as dt_konten, Sub_kategori as sub_kat
# from support.support_function import JENJANG, TEMPLATE_NAME




def index(request):
   # data_ipa = dt_konten.objects.filter(konten_sekolah=request.sekolah,konten_sub_kategori__sub_kategori_uraian='IPA')
   data_ipa = dt_konten.objects.filter(konten_sekolah=request.sekolah,konten_kategori_id__kategori_uraian__icontains='Jurusan', status=True)
   # data_ipa = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Jurusan')
   print(data_ipa.__dict__)
   data ={
      'data_ipa' : data_ipa,

   }

   return render(request, f'{request.jenjang}/{request.template_name}/base/index.html', data)