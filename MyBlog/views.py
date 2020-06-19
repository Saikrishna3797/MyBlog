from django.shortcuts import render

def base_page(request):
    return render(request,"base1.html")

def home_page(request):
    return render(request,"home.html")