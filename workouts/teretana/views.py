from django.shortcuts import render
from teretana.models import Grupa,Vezba,StaKoVezba
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import authenticate,login as lgn

def naslovna(req):
    id_grupe = int(req.GET.get("grupa")) if req.GET.get("grupa") else 0

    grupe = Grupa.objects.all()
    vezbe = Vezba.objects.filter(grupa=id_grupe)

    izlaz = render(req,"index.html",{
        "grupe": grupe,
        "vezbe": vezbe,
        "id_grupe": id_grupe
        })
    return izlaz


def detalji(req,idvezbe):
    vezba = Vezba.objects.get(id=idvezbe)
    return render(req,"detalji.html",{"vezba": vezba})


def odabir(req,idgrupe):
    korisnik = req.user
    if not korisnik.is_authenticated:
        return render(req,"invaliduser.html")
    else:
        skv = StaKoVezba()
        skv.id = korisnik.id
        skv.program_vezbanja = idgrupe
        skv.save()
        return render(req,"odabir.html")
    

def login(req):
    if req.method == "POST":
        uname = req.POST.get("username")
        pwd = req.POST.get("password")
        user = authenticate(username=uname,password=pwd)
        if user:
            lgn(req,user)
            return HttpResponseRedirect("/")
        else:
            return render(req,"login.html")
    else:
        return render(req,"login.html")