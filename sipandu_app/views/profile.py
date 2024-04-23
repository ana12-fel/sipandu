from django.shortcuts import render
from django.shortcuts import render,redirect
from support.support_function import JENJANG, TEMPLATE_NAME

def identitas(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/profile/identitas.html', )
def Visi(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/profile/Visi.html', )

