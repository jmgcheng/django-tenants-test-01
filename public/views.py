from django.shortcuts import render

def landing(request):
    return render(request, "public/landing.html")

def pricing(request):
    return render(request, "public/pricing.html")
