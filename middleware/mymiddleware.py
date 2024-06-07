from django.conf import settings
from django.shortcuts import render, redirect
# -------- MODEL -----------
from sipandu_app.models import Transanksi_situs
# ----- END MODEL ------

class MyModelMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # TODO - your processing here

        domain_name = request.META['HTTP_HOST']
        domain_name = domain_name.split('.')[0]
        print(request.path.startswith('/admin'))

        if not request.path.startswith('/admin') and not request.path.startswith('/assets') and not request.path.startswith('/media'):
            try:
                data_app = Transanksi_situs.objects.get(domain = domain_name)
                request.jenjang = data_app.sekolah_id.sekolah_jenjang.jenjang_nama
                request.template_name = data_app.tema_id.tema_folder_name
                request.sekolah = data_app.sekolah_id
            except Exception as e:
                print('[ERROR MIDDLEWARE]', e)
                request.jenjang = ''
                request.template_name = ''
                request.sekolah = None
                return redirect('https://disdikpapuatengah.id/')
        else:
            print('ss')
            request.jenjang = ''
            request.template_name = ''
            request.sekolah = None

        
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response