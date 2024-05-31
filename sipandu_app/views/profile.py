from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render,redirect, get_object_or_404
from sipandu_app.models import Data_konten as dt_konten, Transanksi_situs as dt_situs
# from support.support_function import JENJANG, TEMPLATE_NAME

def identitas(request):
   
   # tolong di admin ditamnbahkan kunci untuk menu sub kategori.
   data_sejarah = get_object_or_404(dt_konten, konten_sekolah = request.sekolah, judul = 'Sejarah singkat ' )
   data = {
      'data_sejarah' : data_sejarah,
   }
   return render(request, f'{request.jenjang}/{request.template_name}/profile/identitas.html', data)
def Visi(request):
   return render(request, f'{request.jenjang}/{request.template_name}/profile/Visi.html', )
def struktur(request):
   return render(request, f'{request.jenjang}/{request.template_name}/profile/struktur.html', )
def fasilitas(request):
   return render(request, f'{request.jenjang}/{request.template_name}/profile/fasilitas.html', )
def detail_fasilitas(request):
   return render(request, f'{request.jenjang}/{request.template_name}/profile/detail_fasilitas.html', )
def detail_fasilitas_smp(request):
   return render(request, f'{request.jenjang}/{request.template_name}/profile/detail_fasilitas_smp.html', )
def datagtk(request):
   return render(request, f'{request.jenjang}/{request.template_name}/profile/datagtk.html', )
def detail_guru(request):
   return render(request, f'{request.jenjang}/{request.template_name}/profile/detail_guru.html', )

def global_var(request):
    data_konten_nav = dt_konten.objects.filter(konten_sekolah = request.sekolah)
    

    if request.sekolah:
        data_sekolah_header = get_object_or_404(dt_situs, sekolah_id = request.sekolah)
    else:
        data_sekolah_header = ''
        
    # print('cekcok', request.sekolah, data_link_footer)
    print(data_sekolah_header)
    data = {
         'data_konten_nav': data_konten_nav,
         
      }
        
    return data
