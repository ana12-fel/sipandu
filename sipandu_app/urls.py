from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'sipandu'
urlpatterns = [
    path('', home.index, name='home'),
    path('identitas/', profile.identitas, name='identitas'),
    path('visi/', profile.visi, name='visi'),
    # path('berita/', berita.beritasmp, name='berita'),
    path('struktur/', profile.struktur, name='struktur'),

    path('fasilitas/', profile.fasilitas, name='fasilitas'),
     path('detail_fasilitas/<str:id_data_konten>/', profile.detail_fasilitas, name='detail_fasilitas'),

    path('ipa/', jurusan.ipa, name='ipa'),
    path('ips/', jurusan.ips, name='ips'),
    path('bahasa/', jurusan.bahasa, name='bahasa'),
    
    path('kontak/', kontak.index_kontak, name='kontak'),

    path('prestasi/', prestasi.index_prestasi, name='prestasi'),
    path('detail_prestasi/<str:id_data_konten>/', prestasi.Detail_prestasi, name='detail_prestasi'),

    path('berita/', berita.index_berita, name='berita'),
    path('detail/<str:id_data_konten>/', berita.detail, name='detail'),

    path('bursa_kerja/', berita.BursaKerja, name='bursa_kerja'),
    path('detail_bursa_kerja/<str:id_data_konten>/', berita.detail_kerja, name='detail_bursa_kerja'),
   
    path('beasiswa/', berita.Beasiswa, name='beasiswa'),
    path('detail_beasiswa/<str:id_data_konten>/', berita.Detail_beasiswa, name='detail_beasiswa'),
   

    path('galeri/', galeri.galeri01, name='galeri'),

    path('pengumuman/', berita.pengumuman, name='pengumuman'),
    path('detail_pengumuman/<str:id_data_konten>/', berita.Detail_pengumuman, name='detail_pengumuman'),

    path('kegiatan/', berita.kegiatan, name='kegiatan'),
    path('detail_kegiatan/<str:id_data_konten>/', berita.Detail_kegiatan, name='detail_kegiatan'),

    # path('bursa/', berita.bursa, name='bursa'),
   
    path('ekstrakulikuler/', program.ekstrakulikuler, name='ekstrakulikuler'),
    path('detail_eksrakulikuler/<str:id_data_konten>/', program.detail_ekstrakulikuler, name='detail_ekstrakulikuler'),

    
    path('datagtk/', profile.datagtk, name='datagtk'),
    path('detail_guru/<uuid:id_data_guru>/', profile.detail_guru, name='detail_guru'),

    path('sambutan', profile.sambutan, name='sambutan'),
  
  
]