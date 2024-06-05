from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import uuid
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import os

LEVEL_WILAYAH = (
    (1, 'Provinsi'),
    (2, 'Kabupaten'),
    (3, 'Kecamatan'),
)

ROLE_CHOICE =[
    ('superadmin', 'Superadmin'),
    ('admin', 'Admin'),
    ('admin_kabupaten', 'Admin Kabupaten'),
    ('admin_sekolah', 'Admin Sekolah')
]

STATUS_KEPEGAWAIAN =[
    ('guru', 'Guru'),
    ('kepala_sekolah', 'Kepala sekolah'),
]


JENIS_SEKOLAH =(('negeri','Negeri'),('swasta','Swasta'))
STATUS_KEPEMILIKAN_SEKOLAH = (('pemda','Pemerintah Daerah'),('pribadi','Pribadi'),('yayasan','Yayasan'))
AKREDITASI_SEKOLAH = (('belum','Belum Terakreditasi'),('a','A'),('b','B'),('c','C'))
KURIKULUM_SEKOLAH = (('2013','Kurikulum 2013'),('merdeka','Kurikulum Merdeka'))
WAKTU_PENYELANGGARAAN_SEKOLAH =(('pagi','Pagi'),('siang','Siang'),('sore','Sore'),('malam','Malam'))
SUMBER_LISTRIK = (('pln','PLN'),('pembangkit','Pembangkit Listrik'),('diesel','Diesel'))

class Master_wilayah(models.Model):
    wilayah_id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    wilayah_kode = models.TextField(unique=True)
    wilayah_parent = models.ForeignKey('self', default=None, on_delete=models.PROTECT, null=True)
    wilayah_nama = models.TextField()
    wilayah_level = models.CharField(default=None, choices=LEVEL_WILAYAH,max_length=1)
    wilayah_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Master_jenjang(models.Model):
    jenjang_id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    jenjang_nama = models.TextField(unique=True)
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
        
    def archive(self):
        self.jenjang_status = False
        self.deleted_at = timezone.now()
        self.save()

class Master_sekolah(models.Model):
    sekolah_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    sekolah_jenjang = models.ForeignKey(Master_jenjang, on_delete=models.PROTECT,default=None, null=True)
    sekolah_nama = models.TextField(null=True, default=None)
    sekolah_kabupaten = models.ForeignKey(Master_wilayah, related_name='sekolah_kabupaten_related', on_delete=models.CASCADE, null=True, default=None)
    sekolah_kecamatan = models.ForeignKey(Master_wilayah, related_name='sekolah_kecamatan_related', on_delete=models.CASCADE, null=True, default=None)
    sekolah_provinsi = models.ForeignKey(Master_wilayah, related_name='sekolah_provinsi_related', on_delete=models.CASCADE, null=True, default=None)
    sekolah_npsn = models.TextField(unique=True)
    sekolah_jenis = models.TextField(choices=JENIS_SEKOLAH)
    sekolah_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def archive(self):
        self.archived = True
        self.deleted_at = timezone.now()
        self.save()

    def unarchive(self):
        self.archived = False
        self.deleted_at = None
        self.save()


    # sekolah_status_kepemilikan = models.TextField(choices=STATUS_KEPEMILIKAN_SEKOLAH, null=True, default=None)
    # sekolah_no_sk_pendirian = models.TextField(null=True, default=None) 
    # sekolah_tgl_sk_pendirian = models.DateField(null=True, default=None)
    # sekolah_no_sk_operasional = models.TextField(null=True, default=None)
    # sekolah_tgl_sk_operasional = models.DateField(null=True, default=None) 
    # sekolah_kepsek = models.TextField(null=True, default=None)
    # sekolah_akreditasi = models.TextField(choices=AKREDITASI_SEKOLAH, null=True, default=None) 
    # sekolah_kurikulum = models.TextField(choices=KURIKULUM_SEKOLAH, null=True, default=None)
    # sekolah_waktu_penyelenggaraan = models.TextField(choices=WAKTU_PENYELANGGARAAN_SEKOLAH, null=True, default=None)
    # sekolah_alamat = models.TextField(null=True, default=None)
    # sekolah_rt = models.TextField(null=True, default=None)
    # sekolah_rw = models.TextField(null=True, default=None)
    # sekolah_dusun = models.TextField(null=True, default=None) 
    # sekolah_kelurahan = models.TextField(null=True, default=None)
    # sekolah_kodepos = models.CharField(max_length=5, null=True, default=None) 
    # sekolah_kebutuhan_khusus = models.BooleanField(default=None, null=True)
    # sekolah_bank = models.TextField(null=True, default=None)
    # sekolah_bank_kcp = models.TextField(null=True, default=None) 
    # sekolah_rek_nama = models.TextField(null=True, default=None)
    # sekolah_bos_status = models.BooleanField(default=None, null=True)
    # sekolah_iso_sertifikat = models.TextField(default='', null=True, blank=True)
    # sekolah_sumber_listrik = models.TextField(default=None, null=True, choices=SUMBER_LISTRIK)
    # sekolah_daya_listrik = models.IntegerField(default=0) 
    # sekolah_kecepatan_internet = models.IntegerField(default=0)
    
class AccountManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, user_email, user_password, **extra_fields):
    
        if not user_email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(user_email)
        user = self.model(user_email=user_email, **extra_fields)
        print(user_password)
        user.set_password(user_password)
        user.save()
        return user

    def create_superuser(self, user_email, password, **extra_fields):
       
        extra_fields.setdefault("user_is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("user_is_activate", True)
        
        if extra_fields.get("user_is_staff") is not True:
            raise ValueError(_("Superuser must have user_is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(user_email, password, **extra_fields)

    def get_queryset(self):
        return super().get_queryset().filter()
    
class Master_user(AbstractBaseUser):
    user_id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_email = models.EmailField(unique=True)
    user_level = models.CharField(default=3, choices=LEVEL_WILAYAH, max_length=1)
    user_status = models.BooleanField(default=True)
    password = models.TextField(default=None, null=False)
    user_first_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=100)
    user_is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_is_activate = models.BooleanField(default=False)
    user_is_verified = models.BooleanField(default=False)
    user_date_joined = models.DateField(default=timezone.now)
    user_last_login = models.DateTimeField(null=True)
    user_phone = models.CharField(max_length=15)
    user_date_of_birth = models.DateField(blank=True, null=True)
    user_role = models.CharField(max_length=15, choices=ROLE_CHOICE, default='admin_sekolah')
    email_verification_token = models.CharField(max_length=100, default='')
    user_sekolah = models.ForeignKey(Master_sekolah, default=None, null=True, on_delete=models.PROTECT)
    user_kabupaten = models.ForeignKey(Master_wilayah, default=None, null=True, on_delete=models.PROTECT)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = AccountManager()

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['user_phone', 'user_role', 'is_superuser']

    def get_full_name(self):
        return f"{self.user_first_name} {self.user_last_name}"

    def get_short_name(self):
        return self.user_first_name
    
    def archive(self):
        self.user_status = False
        self.deleted_at = timezone.now()
        self.save()

    # @property
    # def is_anonymous(self):
    #     """
    #     Property to determine if the user is anonymous.
    #     """
    #     return False

    # @property
    # def is_authenticated(self):
    #     """
    #     Property to determine if the user is authenticated.
    #     """
    #     return True


class Master_tema(models.Model):
    tema_id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    tema_jenjang = models.ForeignKey(Master_jenjang, on_delete=models.PROTECT,default=None, null=True)
    tema_nama = models.CharField(max_length=200)
    tema_folder_name = models.CharField(max_length=200)
    tema_thumbnail = models.ImageField(upload_to='thumbnails_tema/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def archive(self):
        self.archived = True
        self.deleted_at = timezone.now()
        self.save()

    def unarchive(self):
        self.archived = False
        self.deleted_at = None
        self.save()

    
class Master_kategori(models.Model):
    kategori_id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    kategori_tema = models.ForeignKey(Master_tema, on_delete=models.PROTECT,default=None, null=True)
    kategori_sekolah = models.ForeignKey(Master_sekolah, on_delete=models.PROTECT,default=None, null=True)
    kategori_uraian = models.TextField()
    kategori_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def create_kategori():
    # Buat instance model Jenjang dengan memberikan nilai yang valid untuk jenjang_status
        new_kategori = Master_kategori.objects.create(
        kategori_uraian='BERITA',
        kategori_status=True  # Berikan nilai boolean True atau False
    )


class Sub_kategori(models.Model):
    sub_kategori_id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    kategori_id = models.ForeignKey(Master_kategori, on_delete=models.PROTECT,default=None, null=True)
    sub_kategori_uraian = models.TextField()
    sub_kategori_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('kategori_id', 'sub_kategori_uraian')

    
class Transanksi_situs(models.Model):
    transanksi_id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    tema_id = models.ForeignKey(Master_tema, on_delete=models.PROTECT,default=None, null=True)
    sekolah_id = models.ForeignKey(Master_sekolah,on_delete=models.PROTECT,default=None, null=True)
    domain = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def archive(self):
        self.deleted_at = timezone.now()
        self.save()

def generate_image_filename(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    timestamp = timezone.now().strftime("%H-%M-%S")
    new_filename = f"{basefilename}_{timestamp}{file_extension}"
    return f"image_konten/{new_filename}"


class Data_konten(models.Model):
    id_data_konten = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    konten_sekolah = models.ForeignKey(Master_sekolah,related_name='konten_kategori_related', on_delete=models.CASCADE,default=None, null=True)
    konten_kategori = models.ForeignKey(Master_kategori, related_name='konten_kategori_related', on_delete=models.CASCADE,default=None, null=True)
    konten_sub_kategori = models.ForeignKey(Sub_kategori, related_name='konten_kategori_related', on_delete=models.CASCADE,default=None, null=True)

    judul = models.CharField(max_length=200)
    isi_konten = models.TextField(default=None, null=True)
    status = models.BooleanField(default=True)   
    konten_image = models.ImageField(upload_to=generate_image_filename)
    konten_tag = models.TextField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def archive(self):
        self.archived = True
        self.deleted_at = timezone.now()
        self.save()

    def unarchive(self):
        self.archived = False
        self.deleted_at = None
        self.save()

class Data_galeri(models.Model):
    id_data_galeri= models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    galeri_sekolah = models.ForeignKey(Master_sekolah, on_delete=models.PROTECT,default=None, null=True)
    gambar = models.ImageField(upload_to='galeri_thumbnail/')
    video = models.TextField(null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    

class Data_kontak(models.Model):
    id_data_kontak= models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    kontak_sekolah = models.ForeignKey(Master_sekolah, on_delete=models.PROTECT,default=None, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    fb = models.CharField(max_length=100, blank=True, null=True, verbose_name="Facebook")
    tw = models.CharField(max_length=100, blank=True, null=True, verbose_name="Twitter")
    ig = models.CharField(max_length=100, blank=True, null=True, verbose_name="Instagram")
    no_hp = models.CharField(max_length=15, blank=True, null=True, verbose_name="Nomor HP")
    alamat = models.TextField(null=True, default=None)  # Field untuk alamat
    link_map = models.TextField(null=True, default=None)  # Field untuk link peta
    gambar = models.ImageField(upload_to='galeri_thumbnail/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def archive(self):
        self.deleted_at = timezone.now()
        self.save()

class Data_link(models.Model):
    id_link= models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    link_sekolah = models.ForeignKey(Master_sekolah, on_delete=models.PROTECT,default=None, null=True)
    nama_link = models.CharField(max_length=200)
    judul_link = models.CharField(max_length=200)
    posisi_link = models.TextField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def archive(self):
        self.archived = True
        self.deleted_at = timezone.now()
        self.save()

    def unarchive(self):
        self.archived = False
        self.deleted_at = None
        self.save()


class Data_siswa(models.Model):
    id_data_siswa = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    siswa_sekolah = models.ForeignKey(Master_sekolah, on_delete=models.PROTECT,default=None, null=True)
    total_siswa = models.IntegerField(null=True, default=None)
    keterangan_siswa = models.TextField(default=None, null=True)
    icon_siswa = models.TextField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def archive(self):
        self.archived = True
        self.deleted_at = timezone.now()
        self.save()

    def unarchive(self):
        self.archived = False
        self.deleted_at = None
        self.save()


class Data_guru(models.Model):
    id_data_guru = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    guru_sekolah = models.ForeignKey(Master_sekolah, on_delete=models.PROTECT,default=None, null=True)
    nama_guru = models.CharField(max_length=200)
    nip_guru = models.TextField(max_length=30, null=True)
    mata_pelajaran = models.TextField(max_length=200, null=True)
    pendidikan = models.TextField(max_length=200, null=True)
    guru_image = models.ImageField(upload_to='image_guru/')
    tahun_guru = models.CharField(max_length=10, null=True)
    status_kepegawaian = models.TextField(choices=STATUS_KEPEGAWAIAN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def archive(self):
        self.archived = True
        self.deleted_at = timezone.now()
        self.save()

    def unarchive(self):
        self.archived = False
        self.deleted_at = None
        self.save()

class Data_slider(models.Model):
    id_data_slider= models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    slider_sekolah = models.ForeignKey(Master_sekolah, on_delete=models.PROTECT,default=None, null=True)
    gambar = models.ImageField(upload_to='slider/')
    judul = models.CharField(max_length=200)
    slider_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Laporan(models.Model):
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField()
    laporan_wilayah =  models.ForeignKey(Master_wilayah, default=None, null=True, on_delete=models.PROTECT)
    laporan_sekolah =  models.ForeignKey(Master_sekolah, default=None, null=True, on_delete=models.PROTECT)
    laporan_transaksi =  models.ForeignKey(Transanksi_situs, default=None, null=True, on_delete=models.PROTECT)
    

    def __str__(self):
        return self.judul



    
    

    





# Create your views here.
