from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import uuid
from django.utils import timezone

LEVEL_WILAYAH = (
    (1, 'Provinsi'),
    (2, 'Kabupaten'),
    (3, 'Kecamatan'),
    (4, 'Kampung')
)

WARNA = (
    (1, 'merah putih'),
    (2, 'putih biru'),
    (3, 'putih abu'),
    (4, 'biru putih')
)

ROLE_CHOICE =[
    ('superadmin', 'Superadmin'),
    ('admin', 'Admin'),
    ('admin_kabupaten', 'Admin Kabupaten'),
    ('admin_sekolah', 'Admin Sekolah')
]

JENIS_SEKOLAH =(('negeri','Negeri'),('swasta','Swasta'))
STATUS_KEPEMILIKAN_SEKOLAH = (('pemda','Pemerintah Daerah'),('pribadi','Pribadi'),('yayasan','Yayasan'))
AKREDITASI_SEKOLAH = (('belum','Belum Terakreditasi'),('a','A'),('b','B'),('c','C'))
KURIKULUM_SEKOLAH = (('2013','Kurikulum 2013'),('merdeka','Kurikulum Merdeka'))
WAKTU_PENYELANGGARAAN_SEKOLAH =(('pagi','Pagi'),('siang','Siang'),('sore','Sore'),('malam','Malam'))
SUMBER_LISTRIK = (('pln','PLN'),('pembangkit','Pembangkit Listrik'),('diesel','Diesel'))

class Master_wilayah(models.Model):
    wilayah_id = models.TextField(primary_key=True, default=uuid.uuid4,editable=False, unique=True)
    wilayah_kode = models.TextField(unique=True)
    wilayah_parent = models.ForeignKey('self', default=None, on_delete=models.PROTECT, null=True)
    wilayah_nama = models.TextField()
    wilayah_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Master_jenjang(models.Model):
    jenjang_id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    jenjang_nama = models.TextField()
    jenjang_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def create_jenjang():
    # Buat instance model Jenjang dengan memberikan nilai yang valid untuk jenjang_status
        new_jenjang = Master_jenjang.objects.create(
        jenjang_nama='SD',
        jenjang_status=True  # Berikan nilai boolean True atau False
    )

class Master_sekolah(models.Model):
    sekolah_id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    sekolah_nama = models.TextField(null=True, default=None)
    sekolah_wilayah = models.ForeignKey(Master_wilayah, on_delete=models.PROTECT,default=None, null=True)
    sekolah_npsn = models.TextField(unique=True)
    sekolah_jenis = models.TextField(choices=JENIS_SEKOLAH)
    sekolah_bentuk_pendidikan = models.ForeignKey(Master_jenjang, on_delete=models. PROTECT, default=None, null=True) 
    sekolah_status_kepemilikan = models.TextField(choices=STATUS_KEPEMILIKAN_SEKOLAH, null=True, default=None)
    sekolah_no_sk_pendirian = models.TextField(null=True, default=None) 
    sekolah_tgl_sk_pendirian = models.DateField(null=True, default=None)
    sekolah_no_sk_operasional = models.TextField(null=True, default=None)
    sekolah_tgl_sk_operasional = models.DateField(null=True, default=None) 
    sekolah_kepsek = models.TextField(null=True, default=None)
    sekolah_akreditasi = models.TextField(choices=AKREDITASI_SEKOLAH, null=True, default=None) 
    sekolah_kurikulum = models.TextField(choices=KURIKULUM_SEKOLAH, null=True, default=None)
    sekolah_waktu_penyelenggaraan = models. TextField(choices= WAKTU_PENYELANGGARAAN_SEKOLAH, null=True, default=None)
    sekolah_alamat = models.TextField(null=True, default=None)
    sekolah_rt = models.TextField(null=True, default=None)
    sekolah_rw = models.TextField(null=True, default=None)
    sekolah_dusun = models.TextField(null=True, default=None) 
    sekolah_kelurahan = models.TextField(null=True, default=None)
    sekolah_kodepos = models.CharField(max_length=5, null=True, default=None) 
    sekolah_status = models.BooleanField(default=True)
    sekolah_kebutuhan_khusus = models.BooleanField(default=None, null=True)
    sekolah_bank = models.TextField(null=True, default=None)
    sekolah_bank_kcp = models.TextField(null=True, default=None) 
    sekolah_rek_nama = models.TextField(null=True, default=None)
    sekolah_bos_status = models.BooleanField(default=None, null=True)
    sekolah_iso_sertifikat = models.TextField(default='', null=True, blank=True)
    sekolah_sumber_listrik = models.TextField(default=None, null=True, choices=SUMBER_LISTRIK)
    sekolah_daya_listrik = models.IntegerField(default=0) 
    sekolah_kecepatan_internet = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

class Master_user(AbstractBaseUser):
    user_id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_email = models.EmailField(unique=True)
    user_password = models.TextField(default='', null=False)
    user_status = models.BooleanField(default=True)
    user_role = models.CharField(max_length = 15, choices = ROLE_CHOICE, default = 'admin_sekolah')
    user_ulang_password = models.TextField(default='', null=False)
    user_level = models.CharField(default=None, choices=LEVEL_WILAYAH, max_length=1)
    user_first_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=100)
    user_is_staff = models.BooleanField(default=False)
    user_is_superuser = models.BooleanField(default=False)
    user_is_activate = models.BooleanField(default=False)
    user_is_verified = models.BooleanField(default=False)
    user_date_joined = models.DateField(default=timezone.now)
    user_last_login = models.DateTimeField(null=True)
    user_phone = models.CharField(max_length=15)
    user_date_of_birth = models.DateField(blank=True, null=True)
    user_sekolah = models.ForeignKey(Master_sekolah, default=None, null=True, on_delete=models.PROTECT)
    user_kabupaten = models.ForeignKey(Master_wilayah, default=None, null=True, on_delete=models.PROTECT)

class Master_tema(models.Model):
    tema_id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    tema_jenjang = models.ForeignKey(Master_jenjang, on_delete=models.PROTECT,default=None, null=True)
    tema_warna = models.CharField(default=None, choices=WARNA, max_length=1)
    tema_nama = models.CharField(max_length=200)
    tema_folder_name = models.CharField(max_length=200)
    tema_thumbnail = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Master_kategori(models.Model):
    kategori_id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    tema_id = models.ForeignKey(Master_tema, on_delete=models.PROTECT,default=None, null=True)
    sekolah_id = models.ForeignKey(Master_sekolah, on_delete=models.PROTECT,default=None, null=True)
    kategori_uraian = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Sub_kategori(models.Model):
    sub_kategori_id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    kategori_id = models.ForeignKey(Master_kategori, on_delete=models.PROTECT,default=None, null=True)
    sub_kategori_uraian = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Transanksi_situs(models.Model):
    transanksi_id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    tema_id = models.ForeignKey(Master_tema, on_delete=models.PROTECT,default=None, null=True)
    sekolah_id = models.ForeignKey(Master_sekolah,on_delete=models.PROTECT,default=None, null=True)
    domain = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Data_konten(models.Model):
    id_data_konten = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    sekolah_id = models.ForeignKey(Master_sekolah, on_delete=models.PROTECT,default=None, null=True)
    kategori_id = models.ForeignKey(Master_kategori, on_delete=models.PROTECT,default=None, null=True)
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    image = models.ImageField()
    tag = models.TextField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# Create your views here.
