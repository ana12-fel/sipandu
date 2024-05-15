from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse, HttpResponse
from sipandu_app.models import Data_kontak,Master_sekolah
from django.urls import reverse

def Indexkontak(request):
    if request.method == 'POST':
        kontak_sekolah = request.POST.get('kontak_sekolah')
        no_hp = request.POST.get ('no_hp')
        email = request.POST.get ('email')
        fb = request.POST.get ('fb')
        tw = request.POST.get ('tw')
        ig = request.POST.get ('ig')

        print(kontak_sekolah,no_hp,email,fb,tw,ig)
        dt_kontak = Data_kontak.objects.create(
                                                kontak_sekolah_id=kontak_sekolah,
                                                no_hp=no_hp,
                                                email=email,
                                                fb=fb,
                                                tw=tw,
                                                ig=ig)

        return redirect('sipandu_admin:index_kontak')
    else:
        dt_kontak = Data_kontak.objects.all()
        data_sekolah = Master_sekolah.objects.all()
        print('tes ini kontak')
        return render(request, 'admin/data/kontak_sekolah.html', {"data_kontak": dt_kontak, "data_sekolah" : data_sekolah})

def TambahKontak(request):
    if request.method == 'POST':
        kontak_sekolah = request.POST.get('kontak_sekolah')
        no_hp = request.POST.get('no_hp')
        email = request.POST.get('E_mail')
        fb = request.POST.get('fb')
        tw = request.POST.get('tw')
        ig = request.POST.get('ig')

        # Debug output
        print("POST data:", request.POST)
        print("Extracted data:", kontak_sekolah, no_hp, email, fb, tw, ig)

        # Basic validation (you can expand this as needed)
        if not kontak_sekolah or not no_hp or not email:
            return HttpResponse("Kontak sekolah, nomor HP, dan email harus diisi.", status=400)

        try:
            dt_kontak = Data_kontak.objects.create(
                kontak_sekolah_id=kontak_sekolah,
                no_hp=no_hp,
                email=email,
                fb=fb,
                tw=tw,
                ig=ig
            )
            dt_kontak.save()

            return redirect('sipandu_admin:index_kontak')
        except Exception as e:
            print("Error saving data:", e)
            return HttpResponse(f"Error: {e}", status=500)

    else:
        dt_kontak = Data_kontak.objects.all()
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/tambah_kontak.html', {"data_kontak": dt_kontak, "data_sekolah": data_sekolah})


def EditKontak(request, id_data_kontak):
    
    if request.method == 'POST':
        kontak_sekolah = request.POST.get('kontak_sekolah')
        no_hp = request.POST.get ('no_hp')
        email = request.POST.get ('email')
        fb = request.POST.get ('fb')
        tw = request.POST.get ('tw')
        ig = request.POST.get ('ig')
        print(request.POST)

        dt_kontak = get_object_or_404(Data_kontak, id_data_kontak=id_data_kontak)
        dt_kontak.kontak_sekolah_id=kontak_sekolah
        dt_kontak.no_hp=no_hp
        dt_kontak.email=email
        dt_kontak.fb=fb
        dt_kontak.tw=tw
        dt_kontak.ig=ig

        dt_kontak.save()

        return redirect('sipandu_admin:index_kontak')
    else:
        dt_kontak = get_object_or_404(Data_kontak , id_data_kontak=id_data_kontak )
        data_sekolah = Master_sekolah.objects.all()
        return render(request, 'admin/data/edit_kontak.html', {"data_kontak": dt_kontak, "data_sekolah" : data_sekolah})

def DeleteKontak(request, id_data_kontak):
    try:
        dt_galeri = get_object_or_404(Data_kontak, id_data_kontak=id_data_kontak)
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