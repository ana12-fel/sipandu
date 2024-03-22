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

class Master_wilayah(models.Model):
    wilayah_id = models.TextField(primary_key=True, default=uuid.uuid4,editable=False, unique=True)
    wilayah_kode = models.TextField(unique=True)
    wilayah_parent = models.ForeignKey('self', default=None, on_delete=models.PROTECT, null=True)
    wilayah_nama = models.TextField()
    wilayah_level = models.CharField(default=None, choices=LEVEL_WILAYAH, max_length=1)
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
    sekolah_waktu_penyelenggaraan = models. TextField(choices=WAKTU_PENYELENGGARAAN_SEKOLAH, null=True, default=None)
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

class Master_user(models.)

# Create your views here.
