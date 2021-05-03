from django.shortcuts import render
from currency_converter import CurrencyConverter

# Create your views here.
def home(request):
    if(request.method == 'GET'):
        return render(request, 'conv/home.html', {})
    elif(request.method == 'POST'): 
        try:
            amount = request.POST['amount']   
            fcurrency = request.POST['fcurrency']
            tcurrency = request.POST['tcurrency']
            c = CurrencyConverter()
            camount = c.convert(amount, fcurrency, tcurrency)
        except:
            return render(request, 'conv/home.html', {'err': 'Something went wrong'})
        return render(request, 'conv/home.html', {'camount':camount, 'tcurrency':tcurrency, 'fcurrency':fcurrency, 'amount':amount})