from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from sipandu_app.models import Master_tema, Master_jenjang

def IndexTema(request):
    if request.method == 'POST':
        tema_id = request.POST.get ('tema_id')
        tema_nama = request.POST.get ('tema_nama')
        tema_jenjang = request.POST.get ('tema_jenjang')
        tema_thumbnail = request.FILES.get ('tema_thumbnail')
        tema_folder_name = request.POST.get ('tema_folder_name')

        print(tema_jenjang)
        dt_tema = Master_tema.objects.create(tema_id=tema_id,
                                             tema_nama=tema_nama,
                                             tema_jenjang=Master_jenjang.objects.get(jenjang_id = tema_jenjang),
                                             tema_thumbnail=tema_thumbnail,
                                             tema_folder_name=tema_folder_name)

        print(tema_id,tema_nama,tema_jenjang,tema_thumbnail,tema_folder_name)

        return redirect('sipandu_admin:index_tema')
    
    else:
        data_jenjang = Master_jenjang.objects.all()
        data_tema = Master_tema.objects.all()
        
        return render(request, 'admin/master/index_master_tema.html', {"data_tema" : data_tema, "data_jenjang": data_jenjang})
    
def edit_tema(request, tema_id):
    if request.method == 'POST':
        
        dt_tema = Master_tema.objects.get(tema_id=tema_id)

        tema_id = request.POST.get ('tema_id')
        tema_nama = request.POST.get ('tema_nama')
        tema_jenjang = request.POST.get ('tema_jenjang')
        tema_thumbnail = request.FILES.get ('tema_thumbnail')
        tema_folder_name = request.POST.get ('tema_folder_name')

        
        dt_tema.tema_nama=tema_nama
        print(tema_thumbnail)
        if tema_thumbnail is not None:
            dt_tema.tema_thumbnail=tema_thumbnail
        dt_tema.tema_jenjang=Master_jenjang.objects.get(jenjang_id__icontains = tema_jenjang)
        dt_tema.tema_folder_name=tema_folder_name
        
        dt_tema.save()
        
        return redirect('sipandu_admin:index_tema')
    
    else:
        dt_tema = Master_tema.objects.get(tema_id=tema_id)
        return render(request, 'admin/master/edit_tema.html', {"dt_tema": dt_tema, "id_tema": tema_id })
    
def delete_tema(request, tema_id):
    try:
        dt_tema = get_object_or_404(Master_tema, tema_id=tema_id)
        
        dt_tema.delete()

        data = {
                'status': 'success',
                'message': 'data sekolah berhasil dihapus'
        }
        return JsonResponse(data, status=200)

    except Master_tema.DoesNotExist:
        data = {
                'status': 'error',
                'message': 'data sekolah gagal dihapus, data sekolah tidak ditemukan'
        }
        return JsonResponse(data, status=400)
    


   





