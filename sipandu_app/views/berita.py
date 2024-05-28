from django.shortcuts import render
from django.shortcuts import render,redirect
# from support.support_function import JENJANG, TEMPLATE_NAME

def beritasmp(request):
   return render(request, f'{request.jenjang}/{request.template_name}/berita/berita.html', )
def index_berita(request):
   return render(request, f'{request.jenjang}/{request.template_name}/berita/berita.html', )
def BursaKerja(request):
   return render(request, f'{request.jenjang}/{request.template_name}/berita/bursa_kerja.html', )
def detail(request):
   return render(request, f'{request.jenjang}/{request.template_name}/berita/detail.html', )
def pengumuman(request):
   return render(request, f'{request.jenjang}/{request.template_name}/berita/pengumuman.html', )
def kegiatan(request):
   return render(request, f'{request.jenjang}/{request.template_name}/berita/kegiatan.html', )
def bursa(request):
   return render(request, f'{request.jenjang}/{request.template_name}/berita/bursa_kerja.html', )
