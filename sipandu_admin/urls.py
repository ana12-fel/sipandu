from django.urls import path, include
from .views import base_views,admin_views
from django.contrib.auth import views as auth_views

# yang digunakan untuk link di html adalah app_name:name ex:sipandu_admin:index_user

app_name = 'sipandu_admin'
urlpatterns = [
    path('', base_views.admin_index, name='admin_index'),
    path('login/', admin_views.login_index, name='login_index'),
    path('index-master-user/', admin_views.IndexUser, name='index_user'),
    path('index-master-jenjang/', admin_views.IndexJenjang, name='index_jenjang'),
    path('index-master-wilayah/', admin_views.IndexWilayah, name='index_wilayah'),
    path('index-master-sekolah/', admin_views.IndexSekolah, name='index_sekolah'),
    path('transanksi-situs/', admin_views.TransanksiSitus, name='transanksi_situs'),
    path('data-sekolah/', admin_views.DataSekolah, name='data_sekolah'),
    path('konten/', admin_views.Konten, name='konten'),
    path('laporan-data-sekolah/', admin_views.LaporanDataSekolah, name='laporan_data_sekolah'),
    path('form-jenjang/', admin_views.FormJenjang, name='form_jenjang'),








]