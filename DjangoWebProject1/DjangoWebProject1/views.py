from django.shortcuts import render
from django.http import HttpResponse
def pylinkweb(request):
    return HttpResponse("Django 让 python 能方便连接网页")
def deposits(request):
    return render(request,'E_10_1.html',{})
def result(request):
    pv=int(request.GET['amount'])
    i=float(request.GET['rate'])
    n=int(request.GET['period'])
    fv=str(round(pv*((1+i)**n),2))
    return HttpResponse(fv)
