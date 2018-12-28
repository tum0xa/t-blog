from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request,'mainapp/main.html')

def subscribe(request):
    return HttpResponse('Subscribe template')