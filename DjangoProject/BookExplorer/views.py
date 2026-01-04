from django.http import HttpResponse
from django.shortcuts import render
from Entries.models import EntryV1

# Create your views here.

def book_start(request) -> HttpResponse:
    context = {"var": "Hallo"}
    return render(request, "book_explorer/book.html", context)

def create(request) -> HttpResponse:
    try:
        birthday = request.POST["birthday"]
        if birthday == "":
            birthday = None
        new_entry = EntryV1.objects.create(
            name=request.POST["name"],
            nicknames=request.POST["nicknames"],
            birthday=birthday,
            size=request.POST["size"],
            origin=request.POST["origin"],
            location=request.POST["location"],
            contact=request.POST["contact"],
            likes=request.POST["likes"],
            dislikes=request.POST["dislikes"],
            loveliest_experience=request.POST["loveliest_experience"],
            craziest_experience=request.POST["craziest_experience"],
            favorite_food=request.POST["favorite_food"],
            favorite_book=request.POST["favorite_book"],
            favorite_movie=request.POST["favorite_movie"],
            favorite_animal=request.POST["favorite_animal"],
            favorite_music=request.POST["favorite_music"],
            biggest_idol=request.POST["biggest_idol"],
            want_to_become=request.POST["want_to_become"]
            )
    except Exception as e:
        print(e)
    return next_entry(request, new_entry.id - 1)

def creator(request) -> HttpResponse:
    context = {"edit_mode": True}
    return render(request, "book_explorer/creator.html", context)

def next_entry(request, source_id: int) -> HttpResponse:
    context = {
        "current_entry": EntryV1.objects.filter(pk=source_id + 1).first(),
        "previous_entry": EntryV1.objects.filter(pk=source_id).first(),
        "transition": "next",
        "edit_mode": False
               }
    return render(request, "book_explorer/animated_entry.html", context)


def previous_entry(request, source_id: int) -> HttpResponse:
    context = {
        "current_entry": EntryV1.objects.filter(pk=source_id).first(),
        "previous_entry": EntryV1.objects.filter(pk=source_id - 1).first(),
        "transition" : "prev",
        "edit_mode" : False
    }
    return render(request, "book_explorer/animated_entry.html", context)