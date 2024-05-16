from django.shortcuts import render,redirect
from sipandu_app.models import Data_siswa

def IndexSiswa(request):
    if request.method == 'POST':
        data = {}
        return render(request, 'admin/data/data_siswa.html', data)