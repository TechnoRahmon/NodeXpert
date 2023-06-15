class NodeVersion:
    def __init__(self):
        self.notes = {}
        self.versions = []

    def add_notes_list(self, new_notes: dict):
        self.notes = new_notes

    def add_versions_list(self, new_notes: list):
        self.versions = new_notes

    def merge_all(self) -> list:
        new_list = []
        if len(self.versions) > 1:
          for versionItem in self.versions:
              versionNumber = versionItem['version']
              new_list.append({**versionItem, 'notes': self.notes[versionNumber]})
        else:
          self.versions[0]['notes'] = self.notes[self.versions[0]['version']]
          new_list.append(self.versions[0])
        return new_list
    


class NoteItem:
    def __init__(self, notes: str, version: str):
        self.notes: str = notes
        self.version: str = version


class NvmItem:
    def __init__(self, version: str, active: bool):
        self.version: str = version
        self.active: bool = active

    def to_dict(self):
        return {"version": self.version, "active": self.active}
