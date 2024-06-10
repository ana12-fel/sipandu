from django.shortcuts import render
from sipandu_app.models import Data_konten as dt_konten

def ipa(request):
    # Filter for content with specific criteria (e.g., title contains 'IPA')
    data_ipa = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='IPA')
    data = {
        'data_ipa': data_ipa,
    }
    return render(request, f'{request.jenjang}/{request.template_name}/jurusan/ipa.html', data)



def ips(request):
    # Filter for content with specific criteria (e.g., title contains 'IPS')
    data_ips = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='IPS')
    data = {
        'data_ips': data_ips,
    }
    return render(request, f'{request.jenjang}/{request.template_name}/jurusan/ips.html', data)

def bahasa(request):
   data_bahasa = dt_konten.objects.filter(konten_sekolah=request.sekolah, konten_sub_kategori__sub_kategori_uraian='bahasa').first()
   data = {
      'data_bahasa': data_bahasa,
   }
   return render(request, f'{request.jenjang}/{request.template_name}/jurusan/bahasa.html', data)
