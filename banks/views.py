from django.shortcuts import render, HttpResponse
from .models import Bank, BankStatement
from datetime import datetime

# Create your views here.

def bank_list(request):
    if request.method == "GET":
        
        banks = Bank.objects.all()
        data = {
            "banks": banks
        }
    
    return render(request, "banks/banks.html", data)


def upload_statement(request):
    if request.method == "POST":
        bank_id = request.POST['bank_id']
        month_input = request.POST['month']
        file = request.FILES['statement']
        file_format = request.POST['format']
        
        month = datetime.strptime(
            month_input + "-01", "%Y-%m-%d").date()
        
        bank = Bank.objects.get(id=bank_id)
        
        statement = BankStatement.objects.create(
            bank=bank,
            file=file,
            format=file_format,
            month=month
        )
        return HttpResponse("Extrato importado com sucesso.")


def upload_file_bank_form(request):
    
    banks = Bank.objects.all()
    data = {
            "banks": banks
        }

    return render(request, "banks/forms/upload_file_bank.html", data)