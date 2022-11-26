from django.shortcuts import render, redirect
from .models import Userss
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

def main(request):
    context = {"acc": 0}
    if request.user.is_authenticated:
        context["acc"] = 1
        
    return render(request, "main/main.html", context)

def regist(request):
    if request.user.is_authenticated:
        return redirect("main")
    if request.method == "POST":
        users = Userss(user_login=request.POST["login"], user_password=request.POST["password"], user_email=request.POST["email"])
        users.save()
        user = User.objects.create_user(username=request.POST["login"], password=request.POST["password"], email=request.POST["email"])
        user = authenticate(request, username=request.POST["login"], password=request.POST["password"])
        login(request, user)
        return redirect("main")
    return render(request, "main/register.html")

def vhod(request):
    if request.user.is_authenticated:
        return redirect("main")
    if request.method == "POST":
        try:
            sign_user = Userss.objects.get(user_login=request.POST["login"])
            if sign_user.user_password == request.POST["password"]:
                sign_user = authenticate(request, username=request.POST["login"], password=request.POST["password"])
                login(request, sign_user)
                return redirect("main")
        except Userss.DoesNotExist:
            pass
    return render(request, "main/vhod.html")

def vihod(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("main")    

def test(request):
    return render(request, "main/anketa.html")

def create(request):
    if request.method == "POST":
        print(request.FILES)
        user_email = request.user.email
        create_user = Userss.objects.get(user_email=user_email)
        create_user.user_name = request.POST["name"]
        create_user.user_age = request.POST["age"]
        create_user.user_phone = request.POST["phone"]
        create_user.user_gender = request.POST["gender"]
        create_user.user_category = request.POST["vakan"]
        request.FILES["avatar"].name = str(create_user.user_id) + "." + request.FILES["avatar"].name.split(".")[1]
        create_user.user_avatar = request.FILES["avatar"]
        request.FILES["file"].name = str(create_user.user_id) + "." + request.FILES["file"].name.split(".")[1]
        create_user.user_cv = request.FILES["file"]
        create_user.save()
        return redirect("main")
    if request.user.is_authenticated:
        try:
            user_email = request.user.email
            create_user = Userss.objects.get(user_email=user_email)
            user_name = create_user.user_name
            return render(request, "Ссылка на страницу пользователя")
        except:
            return render(request, "main/anketa.html")

def jobs(request, classs=None, ids=None):
    if not request.user.is_authenticated:
        return redirect("vhod")
    if request.is_ajax():
        if request.method == "POST":
            print(request.POST["classs"]+" "+request.POST["ids"])
            users = Userss.objects.filter(user_category=request.POST["classs"]+" "+request.POST["ids"])
            data = serializers.serialize("json", users, use_natural_foreign_keys=True, use_natural_primary_keys=True)
            print(data)
            return JsonResponse({"data": data})
    return render(request, "main/hr_sort.html")