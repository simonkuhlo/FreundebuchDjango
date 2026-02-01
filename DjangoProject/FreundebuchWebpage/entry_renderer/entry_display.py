from Entries.models import EntryV1


class EntryDisplay:
    def __init__(self, entry: EntryV1):
        self.entry = entry
