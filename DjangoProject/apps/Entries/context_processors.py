# entries/context_processors.py

from .helpers.permission_checks import can_create_entry


def entry_permissions(request):
    return {
        "can_create_entry": can_create_entry(request),
    }