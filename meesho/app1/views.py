from django.shortcuts import render

# Create your views here.

def dress(request):
    return render(request,'dress.html')

def perfume(request):
    return render(request,'perfume.html')

