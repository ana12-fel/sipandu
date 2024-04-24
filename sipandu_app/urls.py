from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'sipandu'
urlpatterns = [
    path('', home.index, name='home'),
    path('identitas/', profile.identitas, name='identitas'),
    path('Visi/', profile.Visi, name='Visi'),
    path('berita/', berita.beritasmp, name='berita'),
    path('struktur/', profile.struktur, name='struktur'),
    path('fasilitas/', profile.fasilitas, name='fasilitas'),
    path('ipa/', jurusan.ipa, name='ipa'),
    path('ips/', jurusan.ips, name='ips'),
    path('bahasa/', jurusan.bahasa, name='bahasa'),
    path('ips/', jurusan.ips, name='ips'),
    path('ekstrakulikuler/', program.ekstrakulikuler, name='ekstrakulikuler'),
    path('kontak/', kontak.index_kontak, name='kontak'),
    path('prestasi/', prestasi.index_prestasi, name='prestasi'),
    path('berita/', berita.index_berita, name='berita'),
    path('bursa_kerja/', berita.BursaKerja, name='bursa_kerja'),
    path('detail/', berita.detail, name='detail'),
    path('galeri/', galeri.galeri01, name='galeri'),
    path('pengumuman/', berita.pengumuman, name='pengumuman'),
    path('kegiatan/', berita.kegiatan, name='kegiatan'),
    path('bursa/', berita.bursa, name='bursa'),
    path('detail_fasilitas/', profile.detail_fasilitas, name='detail_fasilitas'),
    path('detail_fasilitas_smp/', profile.detail_fasilitas_smp, name='detail_fasilitas_smp'),
  
  
]