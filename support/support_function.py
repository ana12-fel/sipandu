from django.shortcuts import render,redirect, get_object_or_404
from sipandu_app.models import Data_link as dt_link, Data_kontak as dt_kontak, Data_siswa as dt_siswa,Transanksi_situs as dt_situs

def global_var(request):
    data_link_footer = dt_link.objects.filter(link_sekolah = request.sekolah)
    data_kontak_footer = dt_kontak.objects.filter(kontak_sekolah = request.sekolah)
    data_siswa_foooter = dt_siswa.objects.filter(siswa_sekolah = request.sekolah)

    if request.sekolah:
        data_sekolah_header = get_object_or_404(dt_situs, sekolah_id = request.sekolah)
    else:
        data_sekolah_header = ''
    # print('cekcok', request.sekolah, data_link_footer)
    print(data_sekolah_header)
    data = {
         'data_link_footer': data_link_footer,
         'data_kontak_footer':data_kontak_footer,
         'data_siswa_footer':data_siswa_foooter,
         'data_sekolah_header':data_sekolah_header,
    }

    
    return data

# JENJANG = global_var()['jenjang']
# TEMPLATE_NAME = global_var()['template_name']