from django.shortcuts import render
from django.shortcuts import render,redirect
# from support.support_function import JENJANG, TEMPLATE_NAME

def ipa(request):
   return render(request, f'{request.jenjang}/{request.template_name}/jurusan/ipa.html', )
# def ips(request):
#    return render(request, f'{JENJANG}/{TEMPLATE_NAME}/jurusan/ips.html', )
# def bahasa(request):
#    return render(request, f'{JENJANG}/{TEMPLATE_NAME}/jurusan/bahasa.html', )