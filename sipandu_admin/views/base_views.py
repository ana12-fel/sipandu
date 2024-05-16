
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# @login_required(login_url='sipandu_admin:login_index')
# @require_http_methods(["GET"])
def admin_index(request):
   return render(request, 'admin/base/index.html', )





# Create your views here.
