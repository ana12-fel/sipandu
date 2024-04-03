from django.shortcuts import render, redirect, HttpResponse
from sipandu_app.models import Master_jenjang

def IndexJenjang(request):
    if request.method == 'POST':
        jenjang_id = request.POST.get ('jenjang_id')
        jenjang_nama = request.POST.get('jenjang_nama')
        jenjang_status = request.POST.get('jenjang_status')

        dt_jenjang = Master_jenjang.objects.create(jenjang_id=jenjang_id,jenjang_nama=jenjang_nama, jenjang_status=jenjang_status)
        
        print(jenjang_id,jenjang_nama, jenjang_status)

        return redirect('sipandu_admin:index_jenjang')

    else:
        data_jenjang = Master_jenjang.objects.all()

        return render(request, 'admin/master/index_master_jenjang.html', {"data_jenjang" : data_jenjang})


def edit_jenjang(request, jenjang_id):
    if request.method == 'POST':
        dt_jenjang = Master_jenjang.objects.get(jenjang_id=jenjang_id)
        jenjang_nama = request.POST.get('jenjang_nama')
        
        dt_jenjang.jenjang_nama=jenjang_nama
        # Lakukan perubahan yang diperlukan pada objek dt_jenjang
        dt_jenjang.save()
        return redirect('sipandu_admin:index_jenjang')  # Redirect ke halaman edit_jenjang dengan menyertakan jenjang_id
    
    else:
        dt_jenjang = Master_jenjang.objects.get(jenjang_id=jenjang_id)
        return render(request, 'admin/master/edit_jenjang.html', {"dt_jenjang": dt_jenjang,"id_jenjang": jenjang_id})
    
def delete_jenjang(request, jenjang_id):     
    try:
       
        dt_jenjang = Master_jenjang.objects.get(jenjang_id=jenjang_id)
        dt_jenjang.delete()

        return redirect('sipandu_admin:index_jenjang')  

    except Master_jenjang.DoesNotExist:

        return HttpResponse("Jenjang tidak ditemukan", status=404)  
