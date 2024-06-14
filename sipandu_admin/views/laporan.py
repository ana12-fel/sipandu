from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph, Image, HRFlowable
from sipandu_app.models import Master_sekolah, Transanksi_situs, Master_tema
from django.db.models import Subquery, OuterRef
from django.contrib.staticfiles import finders
from django.contrib.auth.decorators import login_required

@login_required(login_url='sipandu_admin:login_index')
def laporan_transaksi_belum(request):
    # Ambil data sekolah yang belum memiliki transaksi situs
    data_sekolah = Master_sekolah.objects.exclude(
        sekolah_id__in=Subquery(
            Transanksi_situs.objects.values('sekolah_id')
        )
    )

    # Nama file PDF
    filename = "Laporan_Sekolah_Yang_Belum_Transaksi.pdf"

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
    times_new_roman = "Times-Roman"
    kop_surat_style = ParagraphStyle(
        name='KopSurat',
        parent=styles['Normal'],
        fontName=times_new_roman,
        fontSize=14,
        spaceBefore=0,
        spaceAfter=6,
        leading=15,  # Mengatur leading untuk jarak 1,5 per paragraf
        alignment=1  # 1 untuk center alignment
    )

    title_style = ParagraphStyle(
        name='Title',
        parent=styles['Heading1'],
        fontName=times_new_roman,
        alignment=1,  # 1 untuk center alignment
        fontSize=12  # Ukuran font lebih kecil dari kop surat
    )

    # Konten kop surat
    kop_surat_text = """<para alignment="center">
                            <font size=12><b>PEMERINTAH PROVINSI PAPUA TENGAH</b></font><br/>
                            <font size=14><b>DINAS PENDIDIKAN DAN KEBUDAYAAN</b></font><br/>
                            <font size=10><b><i>JL. Pepera No. 17 Kelurahan Karang Mulia Nabire-Papua Tengah</i></b></font><br/>
                            <font size=9><b><i>email dibudpapuatengah@gmail.com</i></b></font>
                        </para>"""
    kop_surat = Paragraph(kop_surat_text, kop_surat_style)

    # Tambahkan logo dan kop surat dalam tabel
    if logo_path:  # Periksa apakah logo ditemukan
        logo = Image(logo_path, width=60, height=70)
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
        ('ALIGN', (0, 0), (0, 0), 'RIGHT'),
         # Geser logo ke kanan
    ]))

    elements.append(kop_table)
    elements.append(Spacer(1, 5))
    elements.append(HRFlowable(width=700, thickness=1, color=colors.black, spaceBefore=2, spaceAfter=2))  # Adjust width to match the table
    elements.append(Spacer(1, 20))

    # Judul
    title = Paragraph("<b>Laporan Sekolah yang Belum Melakukan Transaksi</b>", title_style)
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Data sekolah dalam bentuk list
    data = [["Provinsi", "Kabupaten", "Kecamatan", "Nama Sekolah", "NPSN", "Jenjang", "Status"]]

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
    col_widths_data = [60, 60, 60, 120, 60, 60, 60]  # Menentukan lebar kolom sesuai kebutuhan
    table = Table(data, colWidths=col_widths_data)

    # Tambahkan style ke tabel
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),  # Ukuran font header
        ('FONTSIZE', (0, 1), (-1, -1), 8),  # Ukuran font data
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),  # Mengurangi padding bawah
        ('TOPPADDING', (0, 0), (-1, 0), 6),  # Menambahkan padding atas untuk keseragaman
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black)  # Mengurangi ketebalan grid
    ])

    table.setStyle(style)

    # Tambahkan tabel ke dokumen
    elements.append(table)
    doc.build(elements)

    return response

@login_required(login_url='sipandu_admin:login_index')
def laporan_transaksi_sudah(request):
    data_transaksi = Transanksi_situs.objects.all()
    # Nama file PDF
    filename = "Laporan_Sekolah_Yang_Sudah_Transaksi.pdf"

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
    times_new_roman = "Times-Roman"
    kop_surat_style = ParagraphStyle(
        name='KopSurat',
        parent=styles['Normal'],
        fontName=times_new_roman,
        fontSize=14,
        spaceAfter=0,
        leading=15,  # Mengatur leading untuk jarak 1,5 per paragraf
        alignment=1  # 1 untuk center alignment
    )

    title_style = ParagraphStyle(
        name='Title',
        parent=styles['Heading1'],
        fontName=times_new_roman,
        alignment=1,  # 1 untuk center alignment
        fontSize=12  # Ukuran font lebih kecil dari kop surat
    )

    # Konten kop surat
    kop_surat_text = """<para alignment="center">
                            <font size=12><b>PEMERINTAH PROVINSI PAPUA TENGAH</b></font><br/>
                            <font size=14><b>DINAS PENDIDIKAN DAN KEBUDAYAAN</b></font><br/>
                            <font size=10><b><i>JL. Pepera No. 17 Kelurahan Karang Mulia Nabire-Papua Tengah</i></b></font><br/>
                            <font size=9><b><i>email dibudpapuatengah@gmail.com</i></b></font>
                        </para>"""
    kop_surat = Paragraph(kop_surat_text, kop_surat_style)

    # Tambahkan logo dan kop surat dalam tabel
    if logo_path:  # Periksa apakah logo ditemukan
        logo = Image(logo_path, width=60, height=70)
        data_kop = [[logo, kop_surat, ""]]
        col_widths = [60, 350, 50]  # Tambahkan kolom kosong untuk menyeimbangkan
    else:
        data_kop = [["", kop_surat, ""]]
        col_widths = [60, 350, 50]

    kop_table = Table(data_kop, colWidths=col_widths)  # Sesuaikan lebar kolom sesuai kebutuhan
    kop_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('SPAN', (1, 0), (2, 0)),  # Menggabungkan kolom untuk teks kop surat
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('LEFTPADDING', (0, 0), (0, 0), 0),
        ('LEFTPADDING', (1, 0), (1, 0), 10),  # Menambahkan padding di sekitar teks
        ('ALIGN', (0, 0), (0, 0), 'RIGHT'),
         # Geser logo ke kanan
    ]))

    elements.append(kop_table)
    elements.append(Spacer(1, 5))
    elements.append(HRFlowable(width=700, thickness=1, color=colors.black, spaceBefore=2, spaceAfter=2))  # Adjust width to match the table
    elements.append(Spacer(1, 20))

    # Judul
    title = Paragraph("<b>Laporan Sekolah yang Sudah Melakukan Transaksi</b>", title_style)
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

    col_widths_data_sudah = [90, 90, 90, 90, 60, 60, 60]  # Menentukan lebar kolom sesuai kebutuhan
    table_sudah = Table(data_sudah_transaksi, colWidths=col_widths_data_sudah)
    style_sudah = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),  # Ukuran font header
        ('FONTSIZE', (0, 1), (-1, -1), 8),  # Ukuran font data
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),  # Mengurangi padding bawah
        ('TOPPADDING', (0, 0), (-1, 0), 6),  # Menambahkan padding atas untuk keseragaman
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black)  # Mengurangi ketebalan grid
    ])
    table_sudah.setStyle(style_sudah)
    elements.append(table_sudah)

    

    doc.build(elements)
    return response
