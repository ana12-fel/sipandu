# globals.py

from django.shortcuts import get_object_or_404
from sipandu_app.models import (Data_link as dt_link, Data_kontak as dt_kontak, 
                                Data_siswa as dt_siswa, Transanksi_situs as dt_situs, 
                                Data_konten as dt_konten, Sub_kategori as sub_kat, 
                                Data_galeri as dt_galeri, Data_slider as dt_slider, Data_guru as dt_guru, Master_sekolah as dt_sekolah )

def global_var(request):
    # Data untuk footer
    data_link_footer = dt_link.objects.filter(link_sekolah=request.sekolah)
    data_kontak_footer = dt_kontak.objects.filter(kontak_sekolah=request.sekolah)
    data_siswa = dt_siswa.objects.filter(siswa_sekolah=request.sekolah)
    nav_profil_sma = sub_kat.objects.filter(kategori_id__kategori_uraian__icontains='PROFILE', kategori_id__kategori_tema__tema_nama__icontains ='TEMA SMA' )
    nav_jurusan_sma = sub_kat.objects.filter(kategori_id__kategori_uraian__icontains='jurusan', kategori_id__kategori_tema__tema_nama__icontains ='TEMA SMA' )
    nav_program_sma = sub_kat.objects.filter(kategori_id__kategori_uraian__icontains='program', kategori_id__kategori_tema__tema_nama__icontains ='TEMA SMA' )
    nav_berita_sma = sub_kat.objects.filter(kategori_id__kategori_uraian__icontains='berita', kategori_id__kategori_tema__tema_nama__icontains ='TEMA SMA' )
    nav_profil_smp = sub_kat.objects.filter(kategori_id__kategori_uraian__icontains='PROFILE', kategori_id__kategori_tema__tema_nama__icontains ='TEMA SMP' )
    nav_program_smp = sub_kat.objects.filter(kategori_id__kategori_uraian__icontains='program', kategori_id__kategori_tema__tema_nama__icontains ='TEMA SMP' )
    nav_berita_smp = sub_kat.objects.filter(kategori_id__kategori_uraian__icontains='berita', kategori_id__kategori_tema__tema_nama__icontains ='TEMA SMP' )
    nav_profil_sd = sub_kat.objects.filter(kategori_id__kategori_uraian__icontains='PROFILE', kategori_id__kategori_tema__tema_nama__icontains ='TEMA SD' )
    nav_berita_sd = sub_kat.objects.filter(kategori_id__kategori_uraian__icontains='berita', kategori_id__kategori_tema__tema_nama__icontains ='TEMA SD' )
    data_guru = dt_guru.objects.filter(guru_sekolah=request.sekolah)
    data_kegiatan = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Kegiatan').order_by('-id_data_konten')[:3]
    data_berita = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:3]
    data_kerja = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Bursa Kerja').order_by('-id_data_konten')[:3]
    jumlah_berita = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').count()
    jumlah_pengumuman = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Pengumuman').count()
    jumlah_kegiatan = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Kegiatan').count()
    jumlah_kerja = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Bursa Kerja').count()
    jumlah_beasiswa = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Beasiswa').count()

    

    try:
        data_sambutan = dt_konten.objects.get(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Sambutan Kepala Sekolah')
    except Exception as e:
        data_sambutan = None

    try:
        data_pengumuman = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Pengumuman').latest('created_at')
        print(data_pengumuman)
    except Exception as e:
        data_pengumuman = None
        print('test')

    try:
        data_kepala_sekolah = dt_guru.objects.filter(guru_sekolah=request.sekolah, status_kepegawaian='kepala_sekolah')
    except Exception as e:
        data_kepala_sekolah = None
        
    # identitas_sekolah = dt_situs.objects.filter(sekolah_id=request.sekolah)
    try:
        identitas_sekolah = dt_sekolah.objects.get(sekolah_id=request.sekolah.sekolah_id)
    except Exception as e:
        print('Cannot get sekolah with id', request.sekolah)
        identitas_sekolah = None
    
    # Data galeri
    galeri = dt_galeri.objects.filter(galeri_sekolah=request.sekolah)
    galeri_footer = dt_galeri.objects.filter(galeri_sekolah=request.sekolah).order_by('-id_data_galeri')[:6]
    galeri_footer_first = dt_galeri.objects.filter(galeri_sekolah=request.sekolah).order_by('-id_data_galeri')[:1]

    
    # Data slider
    if request.sekolah:
        sliders = dt_slider.objects.filter(slider_sekolah=request.sekolah)
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
        'nav_profil_sma': nav_profil_sma,
        'nav_jurusan_sma': nav_jurusan_sma,
        'nav_program_sma': nav_program_sma,
        'nav_berita_sma': nav_berita_sma,
        'nav_profil_smp': nav_profil_smp,
        'nav_berita_smp': nav_berita_smp,
        'nav_program_smp': nav_program_smp,
        'nav_profil_sd': nav_profil_sd,
        'nav_berita_sd': nav_berita_sd,
        'galeri': galeri,
        'sliders': sliders,  # Menggunakan nama variabel 'sliders' untuk membedakannya dari model 'Data_slider'
        'galeri_footer':galeri_footer,
        'galeri_footer_first':galeri_footer_first,
        'data_guru': data_guru,
        'data_kepala_sekolah' : data_kepala_sekolah,
        'identitas_sekolah': identitas_sekolah,
        'akses_menu_master' : ["superadmin","admin"],
        'akses_menu_transaksi_situs' : ["superadmin","admin","admin_kabupaten"],
        'akses_menu_data' : ["superadmin","admin","admin_sekolah"],
        'akses_menu_laporan' : ["superadmin","admin","admin_kabupaten"],
        'data_kegiatan' : data_kegiatan,
        'data_berita' : data_berita,
        'data_kerja' : data_kerja,
        'data_sambutan' : data_sambutan,
        'data_pengumuman' : data_pengumuman,
        'jumlah_berita' : jumlah_berita,
        'jumlah_pengumuman' : jumlah_pengumuman,
        'jumlah_kegiatan' : jumlah_kegiatan,
        'jumlah_kerja' : jumlah_kerja,
        'jumlah_beasiswa' : jumlah_beasiswa,
    }
    
    return data
