from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render,redirect, get_object_or_404
from sipandu_app.models import Data_konten as dt_konten
# from support.support_function import JENJANG, TEMPLATE_NAME

def identitas(request):
   return render(request, f'{request.jenjang}/{request.template_name}/profile/identitas.html', )
def Visi(request):
   return render(request, f'{request.jenjang}/{request.template_name}/profile/Visi.html', )
def struktur(request):
   return render(request, f'{request.jenjang}/{request.template_name}/profile/struktur.html', )
def fasilitas(request):
   return render(request, f'{request.jenjang}/{request.template_name}/profile/fasilitas.html', )
def detail_fasilitas(request):
   return render(request, f'{request.jenjang}/{request.template_name}/profile/detail_fasilitas.html', )
def detail_fasilitas_smp(request):
   return render(request, f'{request.jenjang}/{request.template_name}/profile/detail_fasilitas_smp.html', )
def datagtk(request):
   return render(request, f'{request.jenjang}/{request.template_name}/profile/datagtk.html', )
def detail_guru(request):
   return render(request, f'{request.jenjang}/{request.template_name}/profile/detail_guru.html', )

