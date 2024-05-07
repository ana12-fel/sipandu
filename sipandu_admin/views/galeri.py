from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from sipandu_app.models import Data_galeri
from django.urls import reverse

def Indexgaleri(request):
    if request.method == 'POST':
        judul = request.POST.get ('judul')
        gambar = request.FILES.get('image_konten')

        dt_galeri = Data_galeri.objects.create(
                                            judul=judul,
                                            gambar=image_konten)
        
        print(judul,gambar)


        return redirect('sipandu_admin:index_galeri')
    
    else:
        dt_galeri= Data_galeri.objects.all()
 
        
        return render(request, 'admin/data/galeri.html', {"data_galeri" : dt_galeri,})