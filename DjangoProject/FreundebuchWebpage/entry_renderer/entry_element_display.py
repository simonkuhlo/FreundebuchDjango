from django.template.loader import render_to_string

class EntryElementDisplay:
    def __init__(self):
        self.label: str = ""
        self.str_value: str = ""


    @property
    def as_field_group(self):
        context = {"element" : self}
        return render_to_string("book_explorer/parts/sys/element_field_group.html", context)