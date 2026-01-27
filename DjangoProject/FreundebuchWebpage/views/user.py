from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render

from Entries.models import EntryV1
from settings import settings


def login_page(request):
    match request.method:
        case 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                return
        case 'GET':
            return render(request, "user/login_page.html")
        case _:
            return HttpResponseNotAllowed(['GET', 'POST'])

@login_required
def logout_page(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def register_page(request):
    match request.method:
        case 'POST':
            username = request.POST['username']
            if User.objects.filter(username=username).exists():
                return render(request, "user/register_page.html", {'error': 'Username already exists'})
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            if password != confirm_password:
                return render(request, "user/register_page.html", {'error': 'Passwords do not match'})
            email = request.POST['email'] if request.POST['email'] != "" else None
            User.objects.create_user(username, email, password)
            return HttpResponseRedirect('/')
        case 'GET':
            return render(request, "user/register_page.html")
        case _:
            return HttpResponseNotAllowed(['GET', 'POST'])

@login_required
def account_page(request):
    entries = EntryV1.objects.filter(owner_id=request.user.id)
    can_create_entry = entries.count() < settings.user.max_entries
    context = {
        "entries": entries,
        "can_create_entry": can_create_entry
        }
    return render(request, "user/account_page.html", context)