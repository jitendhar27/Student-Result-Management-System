from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from .models import Admin
# Create your views here.


def ttmhome(request):
    return render(request, "ttmhome.html")


def checkadminlogin(request):
    if request.method == "POST":
        adminuname = request.POST["uname"]
        adminpwd = request.POST["pwd"]
        flag = Admin.objects.filter(Q(username=adminuname, password=adminpwd)).values()
        if flag:
            return render(request, "ttmhome.html")
        else:
            return HttpResponse("Login Fail")
