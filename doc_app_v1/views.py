from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    return render(request,'doctors/homepage.html')

def register(request):
    return render(request, "doctors/register.html")


