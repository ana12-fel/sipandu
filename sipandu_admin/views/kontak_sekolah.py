from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse, HttpResponse
from sipandu_app.models import Data_kontak,Master_sekolah
from django.urls import reverse

def Indexkontak(request):
    if request.method == 'POST':
        kontak_sekolah = request.POST.get('kontak_sekolah')
        no_hp = request.POST.get ('no_hp')
        e_mail = request.POST.get ('e-mail')
        fb = request.POST.get ('fb')
        tw = request.POST.get ('tw')
        ig = request.POST.get ('ig')

        
        dt_kontak = Data_kontak.objects.create(kontak=kontak_sekolah)

        print(kontak_sekolah,no_hp,e_mail,fb,tw,ig)

        dt_kontak = Data_kontak.objects.create(
                                                kontak_sekolah=Master_sekolah.objects.get(sekolah_id=kontak_sekolah),
                                                no_hp=no_hp,
                                                email=e_mail,
                                                fb=fb,
                                                tw=tw,
                                                ig=ig)

        return redirect('sipandu_admin:index_kontak')
    else:
        dt_kontak = Data_kontak.objects.all()
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/kontak_sekolah.html', {"data_kontak": dt_kontak, "data_sekolah" : data_sekolah})
    
def TambahKontak(request):
    if request.method == 'POST':
        kontak_sekolah = request.POST.get('kontak_sekolah')
        no_hp = request.POST.get ('no_hp')
        e_mail = request.POST.get ('e-mail')
        fb = request.POST.get ('fb')
        tw = request.POST.get ('tw')
        ig = request.POST.get ('ig')

        
        dt_kontak = Data_kontak.objects.create(kontak=kontak_sekolah)

        print(kontak_sekolah,no_hp,e_mail,fb,tw,ig)

        dt_kontak = Data_kontak.objects.create(
                                                kontak_sekolah=Master_sekolah.objects.get(sekolah_id=kontak_sekolah),
                                                no_hp=no_hp,
                                                email=e_mail,
                                                fb=fb,
                                                tw=tw,
                                                ig=ig)

        return redirect('sipandu_admin:index_kontak')
    else:
        dt_kontak = Data_kontak.objects.all()
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/tambah_kontak.html', {"data_kontak": dt_kontak, "data_sekolah" : data_sekolah})

def EditKontak(request):
    if request.method == 'POST':
        kontak_sekolah = request.POST.get('kontak_sekolah')
        no_hp = request.POST.get ('no_hp')
        e_mail = request.POST.get ('e-mail')
        fb = request.POST.get ('fb')
        tw = request.POST.get ('tw')
        ig = request.POST.get ('ig')

        
        dt_kontak = Data_kontak.objects.create(kontak=kontak_sekolah)

        print(kontak_sekolah,no_hp,e_mail,fb,tw,ig)

        dt_kontak = Data_kontak.objects.create(
                                                kontak_sekolah=Master_sekolah.objects.get(sekolah_id=kontak_sekolah),
                                                no_hp=no_hp,
                                                email=e_mail,
                                                fb=fb,
                                                tw=tw,
                                                ig=ig)

        return redirect('sipandu_admin:index_kontak')
    else:
        dt_kontak = Data_kontak.objects.all()
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/kontak_sekolah.html', {"data_kontak": dt_kontak, "data_sekolah" : data_sekolah})

def DeleteKontak(request, id_data_kontak):
    try:
        dt_galeri = get_object_or_404(Data_kontak, galeri_id=id_data_kontak)
        dt_galeri.delete()
        
        data = {
            'status': 'success',
            'message': 'Data galeri berhasil dihapus'
        }
        return JsonResponse(data, status=200)
    except Data_kontak.DoesNotExist:
        data = {
            'status': 'error',
            'message': 'Data galeri gagal dihapus, data galeri tidak ditemukan'
        }
        return JsonResponse(data, status=400)
