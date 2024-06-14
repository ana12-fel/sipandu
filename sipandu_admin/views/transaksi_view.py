from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from sipandu_app.models import Master_tema, Master_sekolah, Transanksi_situs
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

@login_required
def IndexTransaksi(request):
    if request.method == 'POST':
        transanksi_id = request.POST.get('transanksi_id')
        sekolah_id = request.POST.get('sekolah_nama')
        tema_id = request.POST.get('tema_nama')
        domain = request.POST.get('domain')

        try:
            # Dapatkan instance Master_tema dari ID yang diberikan
            tema = get_object_or_404(Master_tema, pk=tema_id)

            # Buat instance Transanksi_situs baru
            dt_transaksi = Transanksi_situs.objects.create(
                transanksi_id=transanksi_id,
                sekolah_id_id=sekolah_id, 
                tema_id_id=tema_id,
                domain=domain
            )
            
            print(transanksi_id, sekolah_id, tema_id, domain)

            return redirect('sipandu_admin:index_transaksi')

        except IntegrityError as e:
            print(f"Error: {e}")
            return render(request, 'admin/tema/transaksi_situs.html', {
                "error": "Terjadi kesalahan saat menyimpan data. Pastikan data yang dimasukkan benar.",
                "data_tema": Master_tema.objects.all(),
                "data_sekolah": Master_sekolah.objects.all(),
                "data_transaksi": Transanksi_situs.objects.filter(deleted_at=None),
                "data_arsip": Transanksi_situs.objects.filter(deleted_at__isnull=False)
            })

    else:
        data_tema = Master_tema.objects.all()
        data_sekolah = Master_sekolah.objects.all()
        data_transaksi = Transanksi_situs.objects.filter(deleted_at=None)
        data_arsip = Transanksi_situs.objects.filter(deleted_at__isnull=False)

        return render(request, 'admin/tema/transaksi_situs.html', {
            "data_tema": data_tema,
            "data_sekolah": data_sekolah,
            "data_transaksi": data_transaksi,
            "data_arsip": data_arsip
        })

@login_required
def edit_transaksi(request, transanksi_id):
    dt_transaksi = get_object_or_404(Transanksi_situs, transanksi_id=transanksi_id)

    if request.method == 'POST':
        sekolah_id = request.POST.get('sekolah_nama_edit')
        tema_id = request.POST.get('tema_nama_edit')
        domain = request.POST.get('domain_edit')

        try:
            dt_transaksi.sekolah_id_id = sekolah_id
            dt_transaksi.tema_id_id = tema_id
            dt_transaksi.domain = domain

            dt_transaksi.save()
            
            return redirect('sipandu_admin:index_transaksi')

        except IntegrityError as e:
            print(f"Error: {e}")
            return render(request, 'admin/tema/edit_transaksi.html', {
                "error": "Terjadi kesalahan saat menyimpan data. Pastikan data yang dimasukkan benar.",
                "data_tema": Master_tema.objects.all(),
                "data_sekolah": Master_sekolah.objects.all(),
                "data_transaksi": Transanksi_situs.objects.all(),
                "dt_transaksi": dt_transaksi
            })

    else:
        data_tema = Master_tema.objects.all()
        data_sekolah = Master_sekolah.objects.all()

        return render(request, 'admin/tema/edit_transaksi.html', {
            "data_tema": data_tema,
            "data_sekolah": data_sekolah,
            "data_transaksi": Transanksi_situs.objects.all(),
            "dt_transaksi": dt_transaksi
        })

@login_required
def delete_transaksi(request, transanksi_id):
    try:
        dt_transaksi = get_object_or_404(Transanksi_situs, transanksi_id=transanksi_id)
        dt_transaksi.delete()

        data = {
            'status': 'success',
            'message': 'Data transaksi berhasil dihapus'
        }
        return JsonResponse(data, status=200)

    except Transanksi_situs.DoesNotExist:
        data = {
            'status': 'error',
            'message': 'Data transaksi gagal dihapus, data tidak ditemukan'
        }
        return JsonResponse(data, status=400)

@login_required
def archive_transaksi(request, transanksi_id):
    if request.method == "POST":
        try:
            transaksi = get_object_or_404(Transanksi_situs, transanksi_id=transanksi_id)
            transaksi.archive()
            return JsonResponse({"message": "Data berhasil diarsipkan."}, status=200)
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"error": "Terjadi kesalahan saat mengarsipkan data."}, status=500)
    else:
        return JsonResponse({"error": "Metode HTTP tidak valid."}, status=405)
    

@login_required
def unarchive_transaksi(request, transanksi_id):
    if request.method == 'POST':
        print('test')
        try:
            transaksi = Transanksi_situs.objects.get(transanksi_id=transanksi_id)
             # Ubah status menjadi aktif

            print(transaksi)
            transaksi.deleted_at = None
            transaksi.save()
            return JsonResponse({'message': 'Data berhasil diunarsipkan'}, status=200)
        except Transanksi_situs.DoesNotExist:
            return JsonResponse({'error': 'Data jenjang tidak ditemukan'}, status=404)
    else:
        return JsonResponse({'error': 'Metode request tidak diizinkan'}, status=405)
