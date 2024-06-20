from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render,redirect, get_object_or_404
from sipandu_app.models import Data_konten as dt_konten, Transanksi_situs as dt_situs,Data_guru as dt_guru
# from support.support_function import JENJANG, TEMPLATE_NAME
from django.core.paginator import Paginator

def identitas(request):
   
   # tolong di admin ditamnbahkan kunci untuk menu sub kategori.
   data_sejarah = get_object_or_404(dt_konten, konten_sekolah = request.sekolah, judul__icontains = 'Sejarah singkat' )
   data = {
      'data_sejarah' : data_sejarah,
   }
   return render(request, f'{request.jenjang}/{request.template_name}/profile/identitas.html', data)

def sambutan(request):
   
   data_sambutan = get_object_or_404(dt_konten, konten_sekolah = request.sekolah, judul__icontains = 'data_sambutan' )
   data = {
      'data_sambutan' : data_sambutan,
   }
   return render(request, f'{request.jenjang}/{request.template_name}/base/index.html', data)


def visi(request):
    # tolong di admin ditamnbahkan kunci untuk menu sub kategori.
   data_visi = get_object_or_404(dt_konten, konten_sekolah = request.sekolah, judul__icontains = 'Visi' )
   data_misi = dt_konten.objects.filter(konten_sekolah = request.sekolah, judul__icontains = 'Misi')
   data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
   data = {
      'data_visi' : data_visi,
      'data_misi' : data_misi,
      'data_berita_latest' : data_berita_latest,
   }
   return render(request, f'{request.jenjang}/{request.template_name}/profile/visi.html', data )


def struktur(request):
   print ('test')
   data_struktur = get_object_or_404(dt_konten, konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Struktur Organisasi' )
   data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]

   data = {
      'data_struktur' : data_struktur,
      'data_berita_latest' : data_berita_latest,
   }
   return render(request, f'{request.jenjang}/{request.template_name}/profile/struktur.html', data )

def fasilitas(request):
   
   # data_fasilitas = get_object_or_404(dt_konten, konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian__icontains='Fasilitas' )
   # print(data_fasilitas)
   data_fasilitas = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Fasilitas')
   data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]

   # Set up pagination, 3 berita per halaman
   paginator = Paginator(data_fasilitas, 3)  # 3 berita per halaman
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)

    # Siapkan data untuk template
   data = {
        'page_obj': page_obj,
        'data_berita_latest': data_berita_latest,
    }
   return render(request, f'{request.jenjang}/{request.template_name}/profile/fasilitas.html', data )


def detail_fasilitas(request, id_data_konten):

   data_detail_fasilitas = get_object_or_404(dt_konten, konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian__icontains='Fasilitas', id_data_konten=id_data_konten )
   data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
   # print(data_detail_fasilitas)
   data = {
      'data_detail_fasilitas' : data_detail_fasilitas,
      'data_berita_latest' : data_berita_latest,
   }
   return render(request, f'{request.jenjang}/{request.template_name}/profile/detail_fasilitas.html', data)

def datagtk(request):
    # Fetch data for GTK
    data_gtk = dt_guru.objects.filter(guru_sekolah=request.sekolah)
    data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
   
    
    data = {
        'data_gtk': data_gtk,
        'data_berita_latest' : data_berita_latest,

    }
    return render(request, f'{request.jenjang}/{request.template_name}/profile/datagtk.html', data)

def detail_guru(request, id_data_guru):
    # Fetch detailed data for a specific guru
    data_detail_guru = get_object_or_404(dt_guru, guru_sekolah=request.sekolah, id_data_guru=id_data_guru)
    data_berita_latest = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='Berita').order_by('-id_data_konten')[:5]
   
    data = {
        'data_detail_guru': data_detail_guru,
        'data_berita_latest': data_berita_latest,
    }
    return render(request, f'{request.jenjang}/{request.template_name}/profile/detail_guru.html', data)



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
