from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
def asosiy(request):
    return render(request, "asosiy.html")
def ustoz(request):
    soz = request.GET.get("qidirish")
    if soz==None or soz=="":
        m = Ustoz.objects.filter().order_by('ism')
    else:
        m = Ustoz.objects.filter(ism=soz)
    return render(request, "Ustozlar.html", {'Ustozlar':m})


def fan(request):
    soz = request.GET.get("qidirish")
    if soz==None or soz=="":
        m = Fan.objects.filter().order_by('nom')
    else:
        m = Fan.objects.filter(nom=soz)
    return render(request, "Fan.html", {'Fanlar':m})
def yonalish(request):
    soz = request.GET.get("qidirish")
    if soz==None or soz=="":
        hammasi = Yonalish.objects.filter().order_by('nom')
    else:
        hammasi = Yonalish.objects.filter(nom=soz)
    return render(request, "Yonalish.html", {'Hammasi': hammasi})

def ochir_ustoz(request, son):
    Ustoz.objects.get(id=son).delete()
    return redirect("/ustozlar/")

def ochir_fan(request, fn):
    Fan.objects.get(id=fn).delete()
    return redirect("/fanlar/")


def ochir_yonalish(request, ysh):
    Yonalish.objects.get(id=ysh).delete()
    return redirect("/birlashma/")