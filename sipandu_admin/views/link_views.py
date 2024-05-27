from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from sipandu_app.models import Data_link, Master_sekolah

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
        data_link = Data_link.objects.all()
        return render(request, 'admin/data/link.html', {'data_sekolah' : data_sekolah, 'data_link' : data_link})
        

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

  