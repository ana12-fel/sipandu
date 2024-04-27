from django.shortcuts import render
from django.shortcuts import render,redirect
from support.support_function import JENJANG, TEMPLATE_NAME

def identitas(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/profile/identitas.html', )
def Visi(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/profile/Visi.html', )
def struktur(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/profile/struktur.html', )
def fasilitas(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/profile/fasilitas.html', )
def detail_fasilitas(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/profile/detail_fasilitas.html', )
def detail_fasilitas_smp(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/profile/detail_fasilitas_smp.html', )
def datagtk(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/profile/datagtk.html', )