from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from sipandu_app.models import Data_link, Master_sekolah
from django.contrib.auth.decorators import login_required

@login_required(login_url='sipandu_admin:login_index')
def IndexLink(request):
    if request.method == 'POST':
        link_sekolah = request.POST.get('link_sekolah')
        nama_link = request.POST.get('nama_link')
        judul_link = request.POST.get('judul_link')
        posisi_link = request.POST.get('posisi_link')

        print(link_sekolah)
        dt_link = Data_link.objects.create(link_sekolah=Master_sekolah.objects.get(sekolah_id = link_sekolah),nama_link=nama_link,judul_link=judul_link, posisi_link=posisi_link)

        print(link_sekolah,nama_link,judul_link,posisi_link)

        return redirect ('sipandu_admin:index_link')
    else:
        data_sekolah = Master_sekolah.objects.all()
        data_link = Data_link.objects.by_hakakses(request.user).filter(deleted_at=None)
        data_arsip_link = Data_link.objects.filter(deleted_at__isnull=False)
        return render(request, 'admin/data/link.html', {'data_sekolah' : data_sekolah, 'data_link' : data_link, 'data_arsip_link':data_arsip_link})
        
@login_required(login_url='sipandu_admin:login_index')
def EditLink(request, id_link):
    if request.method == 'POST':
        
        dt_link = Data_link.objects.get(id_link=id_link)

        id_link = request.POST.get ('id_link')
        link_sekolah = request.POST.get('link_sekolah')
        nama_link = request.POST.get('nama_link')
        judul_link = request.POST.get('judul_link')
        posisi_link = request.POST.get('posisi_link')


        print(link_sekolah)
        dt_link.link_sekolah=Master_sekolah.objects.get(sekolah_id=link_sekolah)
        dt_link.nama_link=nama_link
        dt_link.judul_link=judul_link
        dt_link.posisi_link=posisi_link
        
        dt_link.save()
        
        return redirect('sipandu_admin:index_link')
    
    else:
        dt_link = Data_link.objects.get(id_link=id_link)       
        return render(request, 'admin/data/edit_link.html', {"dt_link": dt_link, "id_link": id_link })

@login_required(login_url='sipandu_admin:login_index')
def DeleteLink(request, id_link):
    try:
        dt_link = get_object_or_404(Data_link, id_link=id_link)
        
        dt_link.delete()

        data = {
                'status': 'success',
                'message': 'data link berhasil dihapus'
        }
        return JsonResponse(data, status=200)

    except Data_link.DoesNotExist:
        data = {
                'status': 'error',
                'message': 'data link gagal dihapus, data link tidak ditemukan'
        }
        return JsonResponse(data, status=400)

@login_required(login_url='sipandu_admin:login_index')
def archive_link(request, id_link):
    if request.method == "POST":
        link = get_object_or_404(Data_link, pk=id_link)
        link.archive()
        return JsonResponse({"message": "Data berhasil diarsipkan."})
    else:
        return JsonResponse({"error": "Metode HTTP tidak valid."}, status=405)

@login_required(login_url='sipandu_admin:login_index')
def unarchive_link(request, id_link):
    if request.method == 'POST':
        print('test')
        try:
            link = Data_link.objects.get(id_link=id_link)

            print(link)
            link.deleted_at = None
            link.save()
            return JsonResponse({'message': 'Data berhasil diunarsipkan'}, status=200)
        except Data_link.DoesNotExist:
            return JsonResponse({'error': 'Data jenjang tidak ditemukan'}, status=404)
    else:
        return JsonResponse({'error': 'Metode request tidak diizinkan'}, status=405)

  