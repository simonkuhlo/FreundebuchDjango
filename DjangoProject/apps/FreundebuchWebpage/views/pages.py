from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    return render(request, "main/main.html")

def dedication(request) -> HttpResponse:
    return render(request, "main/dedication.html")