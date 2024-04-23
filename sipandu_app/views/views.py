from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from django.views import View
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
# from support.support_function import truncate, convert_size, get_folder_size
from app.models import Master_User as m_user, Master_sekolah as m_sekolah, Master_wilayah as m_wilayah, ROLE_CHOICES
import shutil,os
from django.db import transaction
from django.db.models.functions import TruncMonth
from django.db.models import Sum, Count
from support.support_function import check_is_email
from support import support_function as sup
from support.support_function import admin_only
from django.db.models import Q, F

# import requests

# Create your views here.
@method_decorator(admin_only(), name='dispatch')
@method_decorator(login_required(), name='dispatch')
class AkunViews(View):
    def get(self, request):
        keyword_query = request.GET.get('query', '')
        kwargs_filter = {}

        if keyword_query != '':
            kwargs_filter['email__icontains'] = keyword_query
            kwargs_filter['username__icontains'] = keyword_query
            kwargs_filter['first_name__icontains'] = keyword_query
            kwargs_filter['last_name__icontains'] = keyword_query
            kwargs_filter['sekolah_sekolah_nama_icontains'] = keyword_query
            kwargs_filter['kabupaten_wilayah_nama_icontains'] = keyword_query

        data_user = m_user.objects.filter(Q(**kwargs_filter, _connector=Q.OR),).order_by('first_name', 'last_name')
        
        # PAGINATOR
        page_num = request.GET.get('page', 1)
        per_page = request.GET.get('per_page', 10)
        page_obj = sup.paging(data_user, page_num, per_page)
        # END PAGINATOR

        # -- STAR CREATE USER SEKOLAH --
        # data_sekolah = m_sekolah.objects.all()
        # for x in data_sekolah:
        #     data_akun = m_user()
        #     data_akun.set_password(f'{x.sekolah_npsn}888@!?')
        #     data_akun.email = f'{x.sekolah_npsn}@gmail.com'
        #     data_akun.username = x.sekolah_npsn
        #     data_akun.first_name = 'Admin'
        #     data_akun.last_name = x.sekolah_nama
        #     data_akun.is_active = True
        #     data_akun.role = 'admin_sekolah'
        #     data_akun.kabupaten = None
        #     data_akun.sekolah = x
        #     data_akun.save()
        # -- END CREATE USER SEKOLAH --

        # -- STAR CREATE USER KABUPATEN --
        # data_kab = m_wilayah.objects.filter(wilayah_level = 2)
        # for x in data_kab:
        #     data_akun = m_user()
        #     print(x.wilayah_kode, x.wilayah_nama)
        #     data_akun.set_password(f'{x.wilayah_kode}888@!?')
        #     data_akun.email = f'{x.wilayah_kode}@gmail.com'
        #     data_akun.username = x.wilayah_kode
        #     data_akun.first_name = 'Admin'
        #     data_akun.last_name = x.wilayah_nama
        #     data_akun.is_active = True
        #     data_akun.role = 'admin_kabupaten'
        #     data_akun.kabupaten = x
        #     data_akun.sekolah = None
        #     data_akun.save()
        # -- END CREATE USER KABUPATEN --

        data = {
            'page_title': 'Index Akun',
            'breadcumb': [{'title': 'Pengaturan Pengguna', 'url':reverse('app:index_akun')}],
            'page_obj': page_obj,
        }
        return render(request, 'app/akun/index_akun.html', data)

class LoginViews(View):
    def get(self, request):
        data = {
            'page_title': 'Dashboard',
            'breadcumb': [{'title': 'SIMDIKOAP', 'url':reverse('app:index_admin')}],
        }
        return render(request, 'app/akun/login.html', data)

    def post(self, request):
        if not request.user.is_authenticated:
            email = request.POST.get('frm_email')
            pwd = request.POST.get('frm_pwd')

            is_email = check_is_email(email)
            
            if is_email:
                user = authenticate(request, email=email, password=pwd)
            else:
                try:
                    user = m_user.objects.get(username = email, is_active = True)
                    if not user.check_password(pwd):
                        user = None
                except Exception as e:
                    user = None
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Selamat datang {user.username} ({user.get_role_display().upper()})")
                if request.GET.get('next') is not None:
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('app:index_admin')
            else:
                messages.error(request, "Login gagal, silahkan masukkan data dengan benar")
                return redirect('app:login')
        else:
            return redirect('app:index_admin')

@method_decorator(login_required(), name='dispatch')
class LogoutViews(View):
    def get(self, request):
        logout_message = request.GET.get('logout_message', None)
        if logout_message is not None:
            messages.info(request, logout_message)
        
        logout(request)
        return redirect(request.META['HTTP_REFERER'])

def save_edit_akun(request, data_akun=None):
    data = {}

    frm_nama_depan = request.POST.get('frm_nama_depan')
    frm_nama_belakang = request.POST.get('frm_nama_belakang')
    frm_username = request.POST.get('frm_username')
    frm_email = request.POST.get('frm_email')
    frm_password = request.POST.get('frm_password')
    frm_role = request.POST.get('frm_role')
    frm_status = request.POST.get('frm_status', False)
    frm_password2 = request.POST.get('frm_password2')
    select_level = request.POST.get('select_level', None)
    select_provinsi = request.POST.get('select_provinsi')
    select_kabupaten = request.POST.get('select_kabupaten')
    select_kecamatan = request.POST.get('select_kecamatan')
    select_sekolah = request.POST.get('select_sekolah')

    try:
        with transaction.atomic():

            if frm_password != frm_password2:
                data['status'] = 'error'
                data['message'] = 'Password tidak cocok'
                return data
            else:
                if data_akun is None:
                    data_akun = m_user()
                    frm_status = True
                    data_akun.set_password(frm_password)
                    data_akun.is_active = frm_status

            data_akun.email = frm_email
            data_akun.username = frm_username
            data_akun.first_name = frm_nama_depan
            data_akun.last_name = frm_nama_belakang
            
            if select_level is None:
                select_level = request.user.role

            data_akun.role = select_level
            
            data_akun.kabupaten = None
            data_akun.sekolah = None

            if select_level == 'admin_kabupaten':
                data_akun.kabupaten = m_wilayah.objects.get(wilayah_id = select_kabupaten)
            elif select_level == 'admin_sekolah':
                data_akun.sekolah = m_sekolah.objects.get(sekolah_id = select_sekolah)
                
            data_akun.save()

            data['status'] = 'success'
            data['message'] = 'Input / Edit akun berhasil.'
    except Exception as e:
        print('Error akun', e)
        data['status'] = 'error'
        data['message'] = f'Input / Edit akun gagal. {str(e)}'
    return data

@method_decorator(admin_only(), name='dispatch')
@method_decorator(login_required(), name='dispatch')
class AddAkunViews(View):
    def get(self, request):
        data_hakakses = ROLE_CHOICES

        data = {
            'data_hakakses': data_hakakses,
            'url_save': reverse('app:tambah_akun'),
            'aksi': 'add',
        }
        return render(request, 'app/akun/tambah_akun.html', data)

    def post(self, request):
        data = save_edit_akun(request)
        return JsonResponse(data)

@method_decorator(login_required(), name='dispatch')
class EditAkunViews(View):
    def get(self, request, user_id):
        data_hakakses = ROLE_CHOICES

        dt_user = m_user.objects.get(user_id = user_id)

        data = {
            'data_hakakses': data_hakakses,
            'data_user': dt_user,
            'url_save': reverse('app:ubah_akun', args=[user_id]),
            'aksi': 'edit',
        }
        return render(request, 'app/akun/tambah_akun.html', data)

    def post(self, request, user_id):
        data_akun = m_user.objects.get(user_id = user_id)

        data = save_edit_akun(request, data_akun)
        return JsonResponse(data)

@method_decorator(login_required(), name='dispatch')
class PengaturanAkunViews(View):
    def get(self, request):

        dt_user = request.user

        data = {
            'data_user': dt_user,
            'url_save': reverse('app:pengaturan_akun'),
            'aksi': 'pengaturan_akun',
        }
        return render(request, 'app/akun/tambah_akun.html', data)

    def post(self, request):
        data_akun = request.user

        data = save_edit_akun(request, data_akun)
        return JsonResponse(data)

@method_decorator(login_required(), name='dispatch')
class UbahPasswordViews(View):
    def get(self, request):
        dt_user = request.user
        data = {
            'data_user': dt_user,
            'url_save': reverse('app:ubah_password'),
            'aksi': 'ubah_password',
        }
        return render(request, 'app/akun/ubah_password.html', data)

    def post(self, request):
        frm_password_old = request.POST.get('frm_password_old')
        frm_password = request.POST.get('frm_password')
        frm_password2 = request.POST.get('frm_password2')

        data = {}

        if not request.user.check_password(frm_password_old):
            data['status'] = 'error'
            data['message'] = 'Password Lama tidak cocok.'
            return JsonResponse(data, status = 400)
        elif frm_password != frm_password2:
            data['status'] = 'error'
            data['message'] = 'Password tidak sama.'
            return JsonResponse(data, status = 400)
        else:
            try:
                with transaction.atomic():
                    request.user.set_password(frm_password)
                    request.user.save()
                    data['status'] = 'success'
                    data['message'] = 'Password Anda berhasil diubah.'
            except Exception as e:
                data['status'] = 'error'
                data['message'] = 'Maaf, terjadi kesalahan server.'
                return JsonResponse(data, status = 400)

        return JsonResponse(data)


@method_decorator(admin_only(), name='dispatch')
@method_decorator(login_required(), name='dispatch')
class ChangeStatusAkunViews(View):
    def post(self, request, user_id):
        data = {}
        try:
            dt_user = m_user.objects.get(user_id = user_id)

            if dt_user.is_active:
                status_message = 'dinonaktifkan'
                dt_user.is_active = False
            else:
                status_message = 'diaktifkan'
                dt_user.is_active = True
        except Exception as e:
            data['status'] = 'error'
            data['message'] = 'User tidak ditemukan'
            return JsonResponse(data, status = 400)

        try:
            with transaction.atomic():
                dt_user.save()

            data['status'] = 'success'
            data['message'] = f'User berhasil di {status_message}'
        except Exception as e:
            data['status'] = 'error'
            data['message'] = f'User gagal di {status_message}'
            return JsonResponse(data, status = 400)

        return JsonResponse(data, status = 200)

@method_decorator(admin_only(), name='dispatch')
@method_decorator(login_required(), name='dispatch')
class ResetPasswordViews(View):
    def post(self, request, user_id):
        data = {}
        try:
            dt_user = m_user.objects.get(user_id = user_id)
        except Exception as e:
            data['status'] = 'error'
            data['message'] = 'User tidak ditemukan.'
            return JsonResponse(data, status = 400)

        try:
            with transaction.atomic():
                pwd = sup.generate_password(10)
                dt_user.set_password(pwd)
                if dt_user.role not in ['admin', 'superadmin']:
                    dt_user.save()
                else:
                    data['status'] = 'error'
                    data['message'] = 'User ADMIN tidak bisa reset password.'
                    return JsonResponse(data, status=400)

            data['status'] = 'success'
            data['message'] = f'Password berhasil diubah, password baru : {pwd}'
        except Exception as e:
            raise e
        return JsonResponse(data, status=200)