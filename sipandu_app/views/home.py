from django.shortcuts import render
from django.shortcuts import render,redirect
from support.support_function import JENJANG, TEMPLATE_NAME

def index(request):
   return render(request, f'{JENJANG}/{TEMPLATE_NAME}/base/index.html', )