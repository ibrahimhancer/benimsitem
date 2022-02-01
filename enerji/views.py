from django.shortcuts import render

# Create your views here.

def enerji(request):
    return render(request, 'enerji.html')