from django.contrib import admin

from Blume.models import User, EntryV1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(EntryV1)
class EntryAdmin(admin.ModelAdmin):
    pass
