from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph,Image
from sipandu_app.models import  Master_sekolah,Transanksi_situs,Master_tema
from django.db.models import Subquery, OuterRef
from django.contrib.staticfiles import finders

def laporan_transaksi_belum(request):
    # Ambil data sekolah yang belum memiliki transaksi situs
    data_sekolah = Master_sekolah.objects.exclude(
        sekolah_id__in=Subquery(
            Transanksi_situs.objects.values('sekolah_id')
        )
    )

    # Nama file PDF
    filename = "Laporan_Data_Sekolah.pdf"

    # Buat HttpResponse dengan tipe konten PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Buat file PDF menggunakan reportlab
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Path ke logo
    logo_path = finders.find('admin/images/brand/logo-papua.png')

    # Gaya untuk kop surat
    styles = getSampleStyleSheet()
    kop_surat_style = ParagraphStyle(
        name='KopSurat',
        parent=styles['Normal'],
        fontSize=14,
        spaceAfter=14,
        leading=21,  # Mengatur leading untuk jarak 1,5 per paragraf
        alignment=1  # 1 untuk center alignment
    )

    title_style = ParagraphStyle(
        name='Title',
        parent=styles['Heading1'],
        alignment=1,  # 1 untuk center alignment
        fontSize=12  # Ukuran font lebih kecil dari kop surat
    )

    # Konten kop surat
    kop_surat_text = "<h2>PEMERINTAH PROVINSI PAPUA TENGAH</h2><br/><h4>DINAS PENDIDIKAN DAN KEBUDAYAAN</h4><br/>Kontak Perusahaan"
    kop_surat = Paragraph(kop_surat_text, kop_surat_style)

    # Tambahkan logo dan kop surat dalam tabel
    if logo_path:  # Periksa apakah logo ditemukan
        logo = Image(logo_path, width=50, height=50)
        data_kop = [[logo, kop_surat, ""]]
        col_widths = [60, 400, 60]  # Tambahkan kolom kosong untuk menyeimbangkan
    else:
        data_kop = [["", kop_surat, ""]]
        col_widths = [60, 400, 60]

    kop_table = Table(data_kop, colWidths=col_widths)  # Sesuaikan lebar kolom sesuai kebutuhan
    kop_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('SPAN', (1, 0), (2, 0)),  # Menggabungkan kolom untuk teks kop surat
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('LEFTPADDING', (0, 0), (0, 0), 0),
        ('LEFTPADDING', (1, 0), (1, 0), 10),  # Menambahkan padding di sekitar teks
    ]))
    elements.append(kop_table)
    elements.append(Spacer(1, 20))

    # Judul
    title = Paragraph("Laporan", title_style)
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Data sekolah dalam bentuk list
    data = [["Provinsi","Kabupaten","Kecamatan","Nama Sekolah", "NPSN", "Jenjang", "Status"]]

    # Isi data sekolah
    for sekolah in data_sekolah:
        data.append([
            sekolah.sekolah_provinsi.wilayah_nama,
            sekolah.sekolah_kabupaten.wilayah_nama,
            sekolah.sekolah_kecamatan.wilayah_nama,
            sekolah.sekolah_nama,
            sekolah.sekolah_npsn,
            sekolah.sekolah_jenjang.jenjang_nama, 
            "Aktif" if sekolah.sekolah_status else "Tidak Aktif"
        ])

    # Buat tabel dari data
    table = Table(data)

    # Tambahkan style ke tabel
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    table.setStyle(style)

    # Tambahkan tabel ke dokumen
    elements.append(table)
    doc.build(elements)

    return response
def laporan_transaksi_sudah(request):
    data_transaksi = Transanksi_situs.objects.all()

    filename = "Laporan_Data_Transaksi_Sudah.pdf"
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []
    
     # Gaya untuk judul
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        name='Center',
        parent=styles['Heading1'],
        alignment=1,  # 1 for center alignment
        fontSize=16
    )

    # Judul
    title = Paragraph("LAPORAN DATA SITUS WEBSITE YANG TELAH TERBIT", title_style)
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Tabel untuk sekolah yang sudah melakukan transaksi
    data_sudah_transaksi = [["Provinsi", "Kabupaten", "Kecamatan", "Nama Sekolah", "NPSN", "Jenjang", "Domain"]]
    for transaksi in data_transaksi:
        data_sudah_transaksi.append([
            transaksi.sekolah_id.sekolah_provinsi.wilayah_nama,
            transaksi.sekolah_id.sekolah_kabupaten.wilayah_nama,
            transaksi.sekolah_id.sekolah_kecamatan.wilayah_nama,
            transaksi.sekolah_id.sekolah_nama,
            transaksi.sekolah_id.sekolah_npsn,
            transaksi.sekolah_id.sekolah_jenjang.jenjang_nama,
            transaksi.domain,
        ])

    table_sudah = Table(data_sudah_transaksi)
    style_sudah = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table_sudah.setStyle(style_sudah)
    elements.append(table_sudah)

    doc.build(elements)
    return response