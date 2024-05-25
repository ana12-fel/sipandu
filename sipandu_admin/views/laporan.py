from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from sipandu_app.models import  Master_sekolah,Transanksi_situs,Master_tema

def laporan_sekolah (request):
    # Ambil data sekolah dari database
    data_sekolah = Master_sekolah.objects.all()

    # Nama file PDF
    filename = "Laporan_Data_Sekolah.pdf"

    # Buat HttpResponse dengan tipe konten PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Buat file PDF menggunakan reportlab
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Data sekolah dalam bentuk list
    data = [["Provinsi","Kabupaten","Kecamatan","Nama Sekolah", "NPSN", "Jenjang", "Status"]]

    # Isi data sekolah
    for sekolah in data_sekolah:
        data.append([sekolah.sekolah_provinsi.wilayah_nama,sekolah.sekolah_kabupaten.wilayah_nama,sekolah.sekolah_kecamatan.wilayah_nama,sekolah.sekolah_nama, sekolah.sekolah_npsn, sekolah.sekolah_jenjang.jenjang_nama, 
                     "Aktif" if sekolah.sekolah_status else "Tidak Aktif"])

    # Buat tabel dari data
    table = Table(data)

    # Tambahkan style ke tabel
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)

    # Tambahkan tabel ke dokumen
    elements.append(table)
    doc.build(elements)

    return response

def laporan_transaksi (request):
    # Ambil data sekolah dari database
    data_transaksi = Transanksi_situs.objects.all()

    # Nama file PDF
    filename = "Laporan_Data_Transaksi.pdf"

    # Buat HttpResponse dengan tipe konten PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Buat file PDF menggunakan reportlab
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Data sekolah dalam bentuk list
    data = [["Tema","Sekolah","Domain","Thumbnail"]]

    # Isi data sekolah
    for transaksi in data_transaksi:
        data.append([transaksi.tema_id.tema_nama,transaksi.sekolah_id.sekolah_nama,transaksi.domain,transaksi.tema_id.tema_thumbnail])

    # Buat tabel dari data
    table = Table(data)

    # Tambahkan style ke tabel
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)

    # Tambahkan tabel ke dokumen
    elements.append(table)
    doc.build(elements)

    return response

