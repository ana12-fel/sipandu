from django.shortcuts import render,redirect
from sipandu_app.models import Master_jenjang
  
def IndexWilayah(request):
    if request.method == 'GET':
        data = {}
        return render(request, 'admin/master/index_master_wilayah.html', data)
    
def IndexSekolah(request):
    if request.method == 'GET':
        data = {}
        return render(request, 'admin/master/index_master_sekolah.html', data)
    
def TransanksiSitus(request):
    if request.method == 'GET':
        data = {}
        return render(request, 'admin/tema/transanksi_situs.html', data)
    
def DataSekolah(request):
    if request.method == 'GET':
        data = {}
        return render(request, 'admin/data/data_sekolah.html', data)
    
def Konten(request):
    if request.method == 'GET':
        data = {}
        return render(request, 'admin/data/konten.html', data)
    
def LaporanDataSekolah(request):
    if request.method == 'GET':
        data = {}
        return render(request, 'admin/laporan/laporan_data_sekolah.html', data)
    
# Create your views here.
