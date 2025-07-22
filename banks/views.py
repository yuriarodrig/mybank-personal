from django.shortcuts import render, HttpResponse
from .models import Bank, BankStatement

# Create your views here.

def bank_list(request):
    if request.method == "GET":
        
        banks = Bank.objects.all()
        data = {
            "banks": banks
        }
    
    return render(request, "banks/banks.html", data)
    

def upload_file_bank(request):
    
    banks = Bank.objects.all()
    data = {
            "banks": banks
        }
    
    return render(request, "banks/forms/upload_file_bank.html", data)