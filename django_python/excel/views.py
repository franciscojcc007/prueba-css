from django.shortcuts import render
from django.http import HttpResponse

def index1(request):
    return render(request, "excel/index.html")

def index0(request):
    return HttpResponse("Hello, world!")