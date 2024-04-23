from django.shortcuts import render
from django.shortcuts import render,redirect
from support.support_function import JENJANG, TEMPLATE_NAME

def index_prestasi(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/prestasi/prestasi.html', )