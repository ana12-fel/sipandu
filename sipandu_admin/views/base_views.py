
from django.shortcuts import render, redirect
from django.db.models import Count, F, Sum
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from sipandu_app.models import Transanksi_situs

# @login_required(login_url='sipandu_admin:login_index')
# @require_http_methods(["GET"])

# @login_required(login_url='sipandu_admin:login_index')
# @require_http_methods(["GET"])
@login_required
def admin_index(request):
   # Mengambil data transaksi situs
   transaksi_situs = Transanksi_situs.objects.all()

    # Menghitung jumlah total sekolah dari data transaksi situs
   total_sekolah = transaksi_situs.values('sekolah_id').distinct().count()

   total_website_sd = Transanksi_situs.objects.filter(sekolah_id__sekolah_jenjang__jenjang_nama='SD').count()
   total_website_smp = Transanksi_situs.objects.filter(sekolah_id__sekolah_jenjang__jenjang_nama='SMP').count()
   total_website_sma = Transanksi_situs.objects.filter(sekolah_id__sekolah_jenjang__jenjang_nama = 'SMA').count()

   total_kabupaten = Transanksi_situs.objects.values('sekolah_id__sekolah_kabupaten', 'sekolah_id__sekolah_kabupaten__wilayah_nama').annotate(dcount=Count('sekolah_id__sekolah_kabupaten'))
   print(total_kabupaten)
   data_kab = ['x']
   data_total = ['Total Per Kabupaten']
   for x in total_kabupaten:
      data_kab.append(x['sekolah_id__sekolah_kabupaten__wilayah_nama'].upper())
      data_total.append(x['dcount'])

   context = {
        'total_sekolah': total_sekolah,
        'total_website_sd': total_website_sd,
        'total_website_smp': total_website_smp,
        'total_website_sma' : total_website_sma,
        'data_kab': data_kab,
        'data_total': data_total,
    }


   return render(request, 'admin/base/index.html', context)






# Create your views here.
