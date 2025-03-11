from django.shortcuts import render

# Create your views here.
def shoe(request):
    return render(request,'shoes.html')

def watch(request):
    return render(request,'watch.html')

