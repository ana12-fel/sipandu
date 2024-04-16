from django.shortcuts import render, redirect
from sipandu_app.models import Master_sekolah, Master_wilayah, Master_jenjang

def IndexSekolah(request):
    if request.method == 'POST':
        nama_sekolah = request.POST.get('sekolah_nama')
        wilayah_id = request.POST.get('kampung')  
        npsn = request.POST.get('sekolah_npsn')
        jenis_sekolah = request.POST.get('sekolah_jenis')
        bentuk_pendidikan = request.POST.get('sekolah_bentuk_pendidikan')  

        dt_sekolah = Master_sekolah.objects.create(
            sekolah_nama=nama_sekolah,
            sekolah_npsn=npsn,
            sekolah_jenis=jenis_sekolah,
            sekolah_bentuk_pendidikan=bentuk_pendidikan,
            sekolah_wilayah_id=wilayah_id,  
        )

        print(nama_sekolah,npsn,jenis_sekolah,bentuk_pendidikan,wilayah_id)

        return redirect('sipandu_admin:index_sekolah')
    
    else:
        sekolah_list = Master_sekolah.objects.all()
        wilayah_list = Master_wilayah.objects.all()
        return render(request, 'admin/master/index_master_sekolah.html', {'sekolah_list': sekolah_list, 'wilayah_list': wilayah_list})
    
def edit_sekolah(request, sekolah_id):
    if request.method == 'POST':
        sekolah = Master_sekolah.objects.get(id=sekolah_id)
        sekolah.sekolah_nama = request.POST.get('sekolah_nama')
        sekolah.sekolah_npsn = request.POST.get('sekolah_npsn')
        sekolah.sekolah_jenis = request.POST.get('sekolah_jenis')
        bentuk_pendidikan = request.POST.get('sekolah_bentuk_pendidikan')
        jenjang = Master_jenjang.objects.get(jenjang_nama=bentuk_pendidikan)
        sekolah.sekolah_bentuk_pendidikan = jenjang
        sekolah.save()
        
        return redirect('sipandu_admin:index_sekolah')
    
    else:
        sekolah = Master_sekolah.objects.get(id=sekolah_id)
        return render(request, 'admin/master/edit_sekolah.html', {"dt_sekolah": sekolah})
    
def delete_sekolah(request, sekolah_id):
    try:
        sekolah = Master_sekolah.objects.get(id=sekolah_id)
        sekolah.delete()
        return redirect('sipandu_admin:index_sekolah')
    except Master_sekolah.DoesNotExist:
        return HttpResponse("Sekolah tidak ditemukan", status=404)
