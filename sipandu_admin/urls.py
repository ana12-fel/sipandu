from django.urls import path, include
from .views import base_views,admin_views,jenjang_view,user_view, sekolah_view,login_view,wilayah_view,tema_view, konten_views,transaksi_view
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

    path('index-master-wilayah/', wilayah_view.IndexWilayah, name='index_wilayah'),
    path('edit_wilayah/<str:wilayah_id>/', wilayah_view.edit_wilayah, name='edit_wilayah'),
    path('wilayah/<str:wilayah_id>/delete/', wilayah_view.delete_wilayah, name='delete_wilayah'),

    path('index-master-jenjang/', jenjang_view.IndexJenjang, name='index_jenjang'),
    path('edit_jenjang/<str:jenjang_id>/', jenjang_view.edit_jenjang, name='edit_jenjang'),
    path('jenjang/<str:jenjang_id>/delete/', jenjang_view.delete_jenjang, name='delete_jenjang'),

    path('index-master-sekolah/', sekolah_view.IndexSekolah, name='index_sekolah'),
    path('edit_sekolah/<str:sekolah_id>/', sekolah_view.edit_sekolah, name='edit_sekolah'),
    path('sekolah/<str:sekolah_id>/delete/', sekolah_view.delete_sekolah, name='delete_sekolah'),

    path('index-master-tema/', tema_view.IndexTema, name='index_tema'),
    path('edit_tema/<str:tema_id>/', tema_view.edit_tema, name='edit_tema'),
    path('tema/<str:tema_id>/delete/', tema_view.delete_tema, name='delete_tema'),

    path('index-transaksi/', transaksi_view.IndexTransaksi, name='index_transaksi'),
    path('edit-transaksi/<str:transanksi_id>/', transaksi_view.edit_transaksi, name='edit_transaksi'),
    path('delete-transaksi/<str:transanksi_id>/delete/',  transaksi_view.delete_transaksi, name='delete_transaksi'),
    
    path('data-sekolah/', admin_views.DataSekolah, name='data_sekolah'),
    path('konten/', konten_views.IndexKonten, name='index_konten'),
    path('tambah_konten/', konten_views.TambahKonten, name='tambah_konten'),
    path('laporan-data-sekolah/', admin_views.LaporanDataSekolah, name='laporan_data_sekolah'),
  
]


