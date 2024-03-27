from django.shortcuts import render, redirect

def admin_index(request):
   return render(request, f'admin/base/base_index.html', )



# Create your views here.
