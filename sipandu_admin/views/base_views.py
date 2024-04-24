from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='sipandu_admin:login_index')
def admin_index(request):
   return render(request, f'admin/base/index.html', )




# Create your views here.
