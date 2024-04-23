from django.shortcuts import render
from django.shortcuts import render,redirect
from support.support_function import JENJANG, TEMPLATE_NAME

<<<<<<< HEAD
def beritasmp(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/berita/berita.html', )
=======
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
>>>>>>> 0406747ed168ec3b8846a292e9325f0564a80c6f
