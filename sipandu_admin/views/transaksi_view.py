from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from sipandu_app.models import Master_tema,Master_sekolah,Transanksi_situs


def IndexTransaksi(request):
    if request.method == 'POST':
        transanksi_id = request.POST.get('transanksi_id')
        sekolah_id = request.POST.get('sekolah_nama')
        tema_id = request.POST.get('tema_nama')
        domain = request.POST.get('domain')

        # Dapatkan instance Master_tema dari ID yang diberikan
        tema = get_object_or_404(Master_tema, pk=tema_id)

        dt_transaksi = Transanksi_situs.objects.create(
            transanksi_id=transanksi_id,
            sekolah_id_id=sekolah_id, 
            tema_id_id=tema_id,
            domain=domain)
        
        print(transanksi_id, sekolah_id, tema_id, domain)

        return redirect('sipandu_admin:index_transaksi')

    else:
        data_tema = Master_tema.objects.all()
        data_sekolah = Master_sekolah.objects.all()
        data_transaksi= Transanksi_situs.objects.all()

        return render(request, 'admin/tema/transaksi_situs.html', {"data_tema": data_tema, "data_sekolah": data_sekolah,"data_transaksi": data_transaksi})
    

def edit_transaksi(request, transanksi_id):
    dt_transaksi = get_object_or_404(Transanksi_situs, transanksi_id=transanksi_id)

    if request.method == 'POST':
        

        sekolah_id = request.POST.get('sekolah_nama')
        tema_id = request.POST.get('tema_nama')
        domain = request.POST.get('domain')

        dt_transaksi.sekolah_id = sekolah_id
        dt_transaksi.tema_id_id = tema_id
        dt_transaksi.domain = domain

        dt_transaksi.save()
        
        return redirect('sipandu_admin:index_transaksi')
    
    else:
        return render(request, 'admin/tema/edit_transaksi.html', {"dt_transaksi": dt_transaksi, "id_transanksi": transanksi_id })
    

def delete_transaksi(request, transanksi_id):
    try:
        dt_transaksi = get_object_or_404(Transanksi_situs, transanksi_id=transanksi_id)
        
        dt_transaksi.delete()

        data = {
                'status': 'success',
                'message': 'data transaksi berhasil dihapus'
        }
        return JsonResponse(data, status=200)

    except Transanksi_situs.DoesNotExist:
        data = {
                'status': 'error',
                'message': 'data sekolah gagal dihapus, data sekolah tidak ditemukan'
        }
        return JsonResponse(data, status=400)

