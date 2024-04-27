from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from sipandu_app.models import Master_jenjang
from django.urls import reverse

def IndexKonten(request):
    if request.method == 'POST':
        # jenjang_id = request.POST.get ('jenjang_id')
        # jenjang_nama = request.POST.get('jenjang_nama')
        # jenjang_status = request.POST.get('jenjang_status')
        # dt_jenjang = Master_jenjang.objects.create(jenjang_id=jenjang_id,jenjang_nama=jenjang_nama, jenjang_status=jenjang_status)
        return redirect('sipandu_admin:index_konten')

    else:
        data = {}
        return render(request, 'admin/data/konten.html', data)

def TambahKonten(request):
    if request.method == 'POST':
        return redirect('sipandu_admin:tambah_konten')
    else:
        data = {}
        return render(request, 'admin/data/tambah_konten.html', data)


