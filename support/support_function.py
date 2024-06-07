# globals.py

from django.shortcuts import get_object_or_404
from sipandu_app.models import (Data_link as dt_link, Data_kontak as dt_kontak, 
                                Data_siswa as dt_siswa, Transanksi_situs as dt_situs, 
                                Data_konten as dt_konten, Sub_kategori as sub_kat, 
                                Data_galeri as dt_galeri, Data_slider as dt_slider)

def global_var(request):
    # Data untuk footer
    data_link_footer = dt_link.objects.filter(link_sekolah=request.sekolah)
    data_kontak_footer = dt_kontak.objects.filter(kontak_sekolah=request.sekolah)
    data_siswa = dt_siswa.objects.filter(siswa_sekolah=request.sekolah)
    data_konten_nav = sub_kat.objects.filter(kategori_id__kategori_uraian='PROFILE')
    
    # Data galeri
    galeri = dt_galeri.objects.filter(galeri_sekolah=request.sekolah)
    
    # Data slider
    if request.sekolah:
        sliders = dt_slider.objects.filter(slider_sekolah=request.sekolah, slider_status=True)
    else:
        sliders = dt_slider.objects.none()  # Jika tidak ada sekolah yang dipilih, kembalikan queryset kosong
    
    # Data sekolah header
    if request.sekolah:
        data_sekolah_header = get_object_or_404(dt_situs, sekolah_id=request.sekolah)
    else:
        data_sekolah_header = ''

    # Paket data yang akan dikembalikan
    data = {
        'data_link_footer': data_link_footer,
        'data_kontak_footer': data_kontak_footer,
        'data_siswa': data_siswa,
        'data_sekolah_header': data_sekolah_header,
        'data_konten_nav': data_konten_nav,
        'galeri': galeri,
        'sliders': sliders,  # Menggunakan nama variabel 'sliders' untuk membedakannya dari model 'Data_slider'
    }
    
    return data
