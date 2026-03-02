class Notebook:
    def __init__(self):
        self.notes = []

    def get_nb_notes(self): #tested
        return[note for note in self.notes]

    def add_note(self,note): #tested
        self.notes.append(note)

    def create_new_id(self): #tested - unit
        if self.notes:
            numbers = [int(note.note_id) for note in self.notes]
            highest = max(numbers)
            return highest + 1
        return 1

    def get_note_by_id(self, note_id): #tested - unit
        for note in self.notes:
            if note_id == int(note.note_id):
                return note
        return None

    def delete_note(self, delete_note): #tested - unit
        self.notes = [note for note in self.notes if note != delete_note]





