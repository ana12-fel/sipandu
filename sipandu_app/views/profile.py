from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render,redirect, get_object_or_404
from sipandu_app.models import Data_konten as dt_konten
# from support.support_function import JENJANG, TEMPLATE_NAME

def identitas(request):
   return render(request, f'{request.jenjang}/{request.template_name}/profile/identitas.html', )
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
    data_konten_nav = dt_konten.objects.filter()
    data_link_footer = dt_link.objects.filter(link_sekolah = request.sekolah)
    data_kontak_footer = dt_kontak.objects.filter(kontak_sekolah = request.sekolah)
    data_siswa_foooter = dt_siswa.objects.filter(siswa_sekolah = request.sekolah)

    if request.sekolah:
        data_sekolah_header = get_object_or_404(dt_situs, sekolah_id = request.sekolah)
    else:
        data_sekolah_header = ''
    # print('cekcok', request.sekolah, data_link_footer)
    print(data_sekolah_header)
    data = {
         'data_link_footer': data_link_footer,
         'data_kontak_footer':data_kontak_footer,
         'data_siswa_footer':data_siswa_foooter,
         'data_sekolah_header':data_sekolah_header, 
          }
