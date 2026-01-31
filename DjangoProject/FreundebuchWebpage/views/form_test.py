from django.shortcuts import render
from ..forms.entry_form import EntryForm

def form_test(request):
    match request.method:
        case "POST":
            pass
        case "GET":
            context = {
                "form" : EntryForm()
            }
            return render(request, "main/form_test.html", context)