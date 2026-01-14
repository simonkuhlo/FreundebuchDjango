from typing import Optional
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Entries.models import EntryV1, CreateCode
from Entries.custom_fields import shortcuts


def create(request):
    if not request.session.get("code"):
        return redirect("/creator/enter_key")
    if not CreateCode.objects.filter(pk=request.session["code"]).exists():
        return redirect("/creator/enter_key")
    match request.method:
        case "POST":
            try:
                birthday = request.POST["birthday"]
                if birthday == "":
                    birthday = None
                custom_field_type = request.POST["custom_field_type"]
                image_file = request.FILES.get("image")
                new_entry = EntryV1.objects.create(
                    name=request.POST["name"],
                    image=image_file,
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
                    want_to_become=request.POST["want_to_become"],
                    custom_field_mode=custom_field_type,
                )
                custom_field_mapping.create(custom_field_type, request, new_entry)
                CreateCode.objects.filter(pk=request.session["code"]).first().delete()
                try:
                    return redirect(f"/explorer/partial/entry/{new_entry.get_previous_by_created().id}/next")
                except:
                    return redirect(f"/explorer/partial/entry/first")
            except Exception as e:
                print(e)
        case _:
            context = {"edit_mode": True}
            return render(request, "creator/creator.html", context)

def enter_key(request, key: Optional[str] = None):
    code = key
    match request.method:
        case "GET":
            if not key:
                return render(request, "creator/enter_creation_code.html")
        case "POST":
            code = request.POST.get("code")
        case _:
            return HttpResponse(status=404)
    code_objects = CreateCode.objects.filter(secret=code).first()
    if code_objects:
        request.session["code"] = code
        return redirect("/creator/")
    else:
        context = {"failure" : True}
        return render(request, "creator/enter_creation_code.html", context)

def custom_field(request):
    match request.method:
        case "POST":
            key = request.POST.get("custom_field_select")
            return custom_field_mapping.render_field(key, request, edit_mode=True)
        case _:
            return HttpResponse(status=404)