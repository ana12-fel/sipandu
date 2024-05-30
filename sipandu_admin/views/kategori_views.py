from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from sipandu_app.models import Master_tema,Master_kategori,Sub_kategori 

def MasterKategori(request):
    if request.method == 'POST':
        kategori_nama = request.POST.get ('kategori_nama')
        kategori_tema= request.POST.get ('form_tema_id')

        dt_kategori = Master_kategori.objects.create(kategori_uraian=kategori_nama, kategori_tema_id = kategori_tema )

        print(kategori_tema,kategori_nama)

        redirect_url = f'/admin/master-kategori?tema_id={kategori_tema}'
        return redirect(redirect_url)
    
    else:
        tema_id = request.GET.get('tema_id' , '')
        data_tema = Master_tema.objects.all()
        data_kat = None

        if tema_id:
            data_kategori = Master_kategori.objects.filter(kategori_tema=tema_id)
            data_kat = Master_tema.objects.filter(tema_id=tema_id)
            data_sub_kategori = Sub_kategori.objects.filter(kategori_id__in=data_kategori)
        else:
            data_kategori = Master_kategori.objects.all()
            data_sub_kategori = Sub_kategori.objects.all()
        
        
        return render(request, 'admin/master_kategori/master_kategori.html', {'data_tema': data_tema, 'data_kategori' : data_kategori, 'data_sub_kategori' : data_sub_kategori, 'data_kat' : data_kat, 'tema_id':tema_id})

def edit_kategori(request, kategori_id_):

    if request.method == 'POST':
        dt_kategori = Master_kategori.objects.get(kategori_id=kategori_id_)
        kategori_uraian = request.POST.get('kategori_uraian')
        kategori_tema= request.POST.get ('form_sub')

        
        dt_kategori.kategori_uraian=kategori_uraian
        dt_kategori.save()

        redirect_url = f'/admin/master-kategori?tema_id={kategori_tema}'
        return redirect(redirect_url) 
    
    else:
        dt_kategori = Master_kategori.objects.get(kategori_id=kategori_id_)

        return render(request, 'admin/master_kategori/edit_kategori.html', {"dt_kategori": dt_kategori,"id_kategori": kategori_id_})
    
def kategoriDelete(request, kategori_id):
    try:
       
        dt_kategori = get_object_or_404(Master_kategori, kategori_id=kategori_id)
        
        dt_kategori.delete()

        data = {
                'status': 'success',
                'message': 'data kategori berhasil dihapus'
        }
        return JsonResponse(data, status=200)

    except Master_kategori.DoesNotExist:
        data = {
                'status': 'error',
                'message': 'data kategori gagal dihapus, data tidak ditemukan'
        }
        return JsonResponse(data, status=400)
    
def SubKategori(request):
     if request.method == 'POST':
        kategori_id_id = request.POST.get('kategori_uraian')
        Sub_kategori_uraian = request.POST.get ('sub_kategori_uraian')
        kategori_tema= request.POST.get ('form_sub')
        data = {}
        try:
            dt_sub_kategori = Sub_kategori.objects.create(kategori_id_id=kategori_id_id,sub_kategori_uraian=Sub_kategori_uraian)
            print('sukses')
            data['status'] = True
            return JsonResponse(data, status = 201)
        except IntegrityError as e:
            print('error insert sub kategori', e)
            data['status'] = False
            return JsonResponse(data, status = 400)

     else:
        data_tema = Master_tema.objects.all()
        data_kategori = Master_kategori.objects.all()
        data_sub_kategori = Sub_kategori.objects.all()
        return render(request, 'admin/master_kategori/master_kategori.html', {'data_tema': data_tema, 'data_kategori' : data_kategori, 'data_sub_kategori' : data_sub_kategori})
     
def edit_sub_kategori(request, sub_kategori_id_):
    if request.method == 'POST':
        dt_sub_kategori = Sub_kategori.objects.get(sub_kategori_id=sub_kategori_id_)

        sub_kategori_uraian = request.POST.get('sub_kategori_uraian')
        kategori_tema= request.POST.get ('form_sub')

        
        dt_sub_kategori.sub_kategori_uraian=sub_kategori_uraian
        dt_sub_kategori.save()
        redirect_url = f'/admin/master-kategori?tema_id={kategori_tema}'
        return redirect(redirect_url)
    
    else:
        dt_sub_kategori = Sub_kategori.objects.get(sub_kategori_id=sub_kategori_id_)

        return render(request, 'admin/master_kategori/edit_sub_kategori.html', {"dt_sub_kategori": dt_sub_kategori,"sub_kategori_id": sub_kategori_id_})
    
def SubKategoriDelete(request, sub_kategori_id):
    try:
       
        dt_sub_kategori = get_object_or_404(Sub_kategori, sub_kategori_id=sub_kategori_id)
        
        dt_sub_kategori.delete()

        data = {
                'status': 'success',
                'message': 'data kategori berhasil dihapus'
        }
        return JsonResponse(data, status=200)

    except Sub_kategori.DoesNotExist:
        data = {
                'status': 'error',
                'message': 'data kategori gagal dihapus, data tidak ditemukan'
        }
        return JsonResponse(data, status=400)
    

    
    


        
        
   
    
