from django.contrib import admin

from Entries.models import EntryV1, CreateCode, CustomTextField


@admin.register(EntryV1)
class EntryAdmin(admin.ModelAdmin):
    pass

@admin.register(CustomTextField)
class CustomTextFieldAdmin(admin.ModelAdmin):
    pass

@admin.register(CreateCode)
class CreateCodeAdmin(admin.ModelAdmin):
    readonly_fields = ['info_display']

    def info_display(self, obj):
        return f"http://testing.meow.technology:6969/creator/enter_key/{obj.secret}"  # Custom info string
    info_display.short_description = "Url"
