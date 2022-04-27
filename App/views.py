from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
def asosiy(request):
    return render(request, "asosiy.html")
def ustoz(request):

    m = Ustoz.objects.all()
    return render(request, "Ustozlar.html", {'Ustozlar':m})


def fan(request):
    m = Fan.objects.all()
    return render(request, "Fan.html", {'Fanlar':m})




def ochir_ustoz(request , son):
    Ustoz.objects.get(id=son).delete()
    return redirect("/ustozlar/")