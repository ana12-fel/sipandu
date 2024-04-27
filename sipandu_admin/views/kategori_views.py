from django.shortcuts import render,redirect
def MasterKategori(request):
    if request.method == 'GET':
        data = {}
        return render(request, 'admin/tema/transanksi_situs.html', data)