from django.shortcuts import render, redirect
from sipandu_app.models import Master_tema

def IndexTema(request):
    if request.method == 'POST':
        tema_id = request.POST.get ('tema_id')
        tema_nama = request.POST.get ('tema_nama')
        tema_jenjang = request.POST.get ('tema_jenjang')
        tema_thumbnail = request.POST.get ('tema_thumbnail')
        tema_folder_name = request.POST.get ('tema_folder_name')

        dt_tema = Master_tema.objects.create(tema_id=tema_id,tema_nama=tema_nama,tema_jenjang=tema_jenjang,tema_thumbnail=tema_thumbnail,tema_folder_name=tema_folder_name)

        print(tema_id,tema_nama,tema_jenjang,tema_thumbnail,tema_folder_name)

        return redirect('sipandu_admin:index_tema')
    
    else:
        data_tema = Master_tema.objects.all()

        return render(request, 'admin/master/index_master_tema.html', {"data_tema" : data_tema})
   






# from django.shortcuts import render, redirect
# from sipandu_app.models import Master_tema

# def IndexTema(request):
#     if request.method == 'GET':
#         data = {}
#         return render(request, 'admin/master/index_master_tema.html', data)