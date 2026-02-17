class Notebook:
    def __init__(self):
        self.notes = []

    def check_notebook_len(self):
        return bool(self.notes)

    def add_note(self,note):
        self.notes.append(note)

    def create_new_id(self):
        if self.check_notebook_len():
            numbers = [int(note.note_id) for note in self.notes]
            highest = max(numbers)
            return highest + 1
        return 1

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note_id == int(note.note_id):
                return note
        return None
    @staticmethod
    def get_edit_key(choose_key):
        keys = {1: "title", 2: "description", 3: "date", 4: "tag"}
        return keys.get(choose_key, '')

    @staticmethod
    def make_edit(note,key,value):
        setattr(note,key,value)
        return True

    def delete_note(self, delete_note):
        self.notes = [note for note in self.notes if note != delete_note]




