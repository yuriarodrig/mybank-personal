from django.shortcuts import render, HttpResponse

# Create your views here.

def bank_list(request):
    return HttpResponse("Lista de Paginas")
    

def upload_file_bank(request):
    return HttpResponse("Anexar Extrato do banco")