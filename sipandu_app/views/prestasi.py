from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render,redirect, get_object_or_404
from sipandu_app.models import Data_konten as dt_konten, Transanksi_situs as dt_situs


def index_prestasi(request):

   data_prestasi = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Prestasi')
   data = {
      'data_prestasi' : data_prestasi,
   }
   return render(request, f'{request.jenjang}/{request.template_name}/prestasi/prestasi.html', data )
