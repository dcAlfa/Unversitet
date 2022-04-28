from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
def asosiy(request):
    return render(request, "asosiy.html")
def ustoz(request):
    if request.method=="POST":
        if request.POST.get('n')== "False":
            natija = False
        else:
            natija = True
        Ustoz.objects.create(
            ism =  request.POST.get('ismi'),
            yosh = request.POST.get('y'),
            nafaqada = natija,
            sana = request.POST.get('v')
        )
        return redirect("/ustozlar/")
    soz = request.GET.get("qidirish")
    if soz==None or soz=="":
        m = Ustoz.objects.filter().order_by('ism')
    else:
        m = Ustoz.objects.filter(ism=soz)
    return render(request, "Ustozlar.html", {'Ustozlar':m})


def fan(request):
    if request.method=="POST":
        if request.POST.get('a')==False:
            natija = False
        else:
            natija = True
        Fan.objects.create(
            nom = request.POST.get('n'),
            cod = request.POST.get('c'),
            vaqt = request.POST.get('v'),
            is_active = natija,
        )
        return redirect("/fanlar/")
    soz = request.GET.get("qidirish")
    if soz==None or soz=="":
        m = Fan.objects.filter().order_by('nom')
    else:
        m = Fan.objects.filter(nom=soz)
    return render(request, "Fan.html", {'Fanlar':m})
def yonalish(request):
    a = Ustoz.objects.all()
    b = Fan.objects.all()
    if request.method=="POST":
        d = request.POST.get('ustozi')
        g = request.POST.get('fani')
        ustozlari = Ustoz.objects.get(id=d)
        fanlari = Fan.objects.get(id=g)
        Yonalish.objects.create(
            nom = request.POST.get("n"),
            fanlar = fanlari,
            ustozlar = ustozlari
        )
        return redirect("/birlashma/")
    soz = request.GET.get("qidirish")
    if soz==None or soz=="":
        hammasi = Yonalish.objects.filter().order_by('nom')
    else:
        hammasi = Yonalish.objects.filter(nom=soz)
    return render(request, "Yonalish.html", {'Hammasi': hammasi, "shablon": a, "fanlar": b})

def ochir_ustoz(request, son):
    Ustoz.objects.get(id=son).delete()
    return redirect("/ustozlar/")

def ochir_fan(request, fn):
    Fan.objects.get(id=fn).delete()
    return redirect("/fanlar/")


def ochir_yonalish(request, ysh):
    Yonalish.objects.get(id=ysh).delete()
    return redirect("/birlashma/")