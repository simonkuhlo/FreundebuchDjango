from django.shortcuts import render


def index(request):
    return render(request, "main/main.html")

def dedication(request):
    return render(request, "main/dedication.html")