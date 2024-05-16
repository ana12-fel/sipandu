from django.urls import path, include
from .views import base_views,admin_views,jenjang_view,user_view, sekolah_view,login_view,wilayah_view,tema_view, konten_views,kategori_views,siswa_views
from .views import base_views,admin_views,jenjang_view,user_view, sekolah_view,login_view,wilayah_view,tema_view, konten_views,transaksi_view,galeri,kontak_sekolah
from django.contrib.auth import views as auth_views


# yang digunakan untuk link di html adalah app_name:name ex:sipandu_admin:index_user

app_name = 'sipandu_admin'
urlpatterns = [
    path('', base_views.admin_index, name='admin_index'),
    path('login/', login_view.login_index, name='login_index'),
    path('logout/', login_view.logout_views, name='logout'),

    path('index-master-user/', user_view.IndexUser, name='index_user'),
    path('edit_user/<str:user_id>/', user_view.edit_user, name='edit_user'),
    path('user/delete/<str:user_id>/', user_view.delete_user, name='delete_user'),
    path('get-wilayah-by-level/', user_view.get_wilayah_by_level, name='get_wilayah_by_level'),


    path('index-master-wilayah/', wilayah_view.IndexWilayah, name='index_wilayah'),
    path('edit_wilayah/<str:wilayah_id>/', wilayah_view.edit_wilayah, name='edit_wilayah'),
    path('wilayah/<str:wilayah_id>/delete/', wilayah_view.delete_wilayah, name='delete_wilayah'),
    path('get-wilayah-by-level/', wilayah_view.get_wilayah_by_level, name='get_wilayah_by_level'),
    path('cek_kode_wilayah/', wilayah_view.cek_kode_wilayah, name='cek_kode_wilayah'),

    path('index-master-jenjang/', jenjang_view.IndexJenjang, name='index_jenjang'),
    path('edit_jenjang/<str:jenjang_id>/', jenjang_view.edit_jenjang, name='edit_jenjang'),
    path('jenjang/<str:jenjang_id>/delete/', jenjang_view.delete_jenjang, name='delete_jenjang'),

    path('index-master-sekolah/', sekolah_view.IndexSekolah, name='index_sekolah'),
    path('edit_sekolah/<str:sekolah_id>/', sekolah_view.edit_sekolah, name='edit_sekolah'),
    path('sekolah/<str:sekolah_id>/delete/', sekolah_view.delete_sekolah, name='delete_sekolah'),
    path('get-wilayah/', sekolah_view.get_wilayah, name='get_wilayah'),


    path('index-master-tema/', tema_view.IndexTema, name='index_tema'),
    path('edit_tema/<str:tema_id>/', tema_view.edit_tema, name='edit_tema'),
    path('tema/<str:tema_id>/delete/', tema_view.delete_tema, name='delete_tema'),

    path('master-kategori/', kategori_views.MasterKategori, name='master_kategori'),
    path('edit_kategori/<str:kategori_id_>/', kategori_views.edit_kategori, name='edit_kategori'),
    path('kategori/<str:kategori_id>/delete/', kategori_views.kategoriDelete, name='delete_kategori'),
    path('sub-kategori/', kategori_views.SubKategori, name='sub_kategori'),
    path('edit_sub_kategori/<str:sub_kategori_id_>/', kategori_views.edit_sub_kategori, name='edit_sub_kategori'),
    path('subkategori/<str:sub_kategori_id>/delete/', kategori_views.SubKategoriDelete, name='delete_sub_kategori'),

    path('konten/', konten_views.IndexKonten, name='index_konten'),
    path('tambah_konten/', konten_views.TambahKonten, name='tambah_konten'),
    path('edit_konten/<str:id_data_konten>/edit', konten_views.EditKonten, name='edit_konten'),
    path('delete_konten/<str:id_data_konten>/delete', konten_views.DeleteKonten, name='delete_konten'),
    
    path('galeri/', galeri.Indexgaleri, name='index_galeri'),
    path('tambah_galeri/', galeri.Tambahgaleri, name='tambah_galeri'),
    path('edit_galeri/<str:id_data_galeri>/', galeri.Editgaleri, name='edit_galeri'),
    path('delete_galeri/<str:id_data_galeri>/delete', galeri.Deletegaleri, name='delete_galeri'),
    
    
    path('kontak/', kontak_sekolah.Indexkontak, name='index_kontak'),
    path('tambah_kontak/', kontak_sekolah.TambahKontak, name='tambah_kontak'),
    path('edit_kontak/<str:id_data_kontak>/', kontak_sekolah.EditKontak, name='edit_kontak'),
    path('delete_kontak/<str:id_data_kontak>/delete', kontak_sekolah.DeleteKontak, name='delete_kontak'),


    path('transanksi-situs/', admin_views.TransanksiSitus, name='transanksi_situs'),
    path('index-transaksi/', transaksi_view.IndexTransaksi, name='index_transaksi'),
    path('edit-transaksi/<str:transanksi_id>/', transaksi_view.edit_transaksi, name='edit_transaksi'),
    path('delete-transaksi/<str:transanksi_id>/delete/',  transaksi_view.delete_transaksi, name='delete_transaksi'),
    
    path('laporan-data-sekolah/', admin_views.LaporanDataSekolah, name='laporan_data_sekolah'),
    path('index-siswa/', siswa_views.IndexSiswa, name='index_siswa'),
    path('edit_siswa/<str:id_data_siswa>/', siswa_views.EditSiswa, name='edit_siswa'),
    path('delete_siswa/<str:id_data_siswa>/delete', siswa_views.DeleteSiswa, name='delete_siswa')

  

]

