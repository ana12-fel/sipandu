from django.shortcuts import render
from django.shortcuts import render,redirect
from support.support_function import JENJANG, TEMPLATE_NAME

def beritasmp(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/berita/berita.html', )
def index_berita(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/berita/berita.html', )
def BursaKerja(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/berita/bursa_kerja.html', )
def detail(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/berita/detail.html', )
def pengumuman(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/berita/pengumuman.html', )
def kegiatan(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/berita/kegiatan.html', )
def bursa(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/berita/bursa_kerja.html', )
