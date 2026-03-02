from Notebook.storage import NotebookStorage
from Notebook.note import Note

class Service:
    def __init__(self, notebook):
        self.notebook = notebook

    def get_notes(self):
        return self.notebook.get_nb_notes()

    def choose_note_by_id(self,note_id):
        return self.notebook.get_note_by_id(note_id)

    def add_note(self,title, description, date, tag): #tested
        note_id = self.notebook.create_new_id()
        note = Note(note_id, title, description, date, tag)
        self.notebook.add_note(note)

    @staticmethod
    def edit_note(note, key, value):
        if key == 1:
            note.change_title(value)

        elif key == 2:
            note.change_description(value)

        elif key == 3:
            note.change_date(value)

        elif key == 4:
            note.change_tag(value)

    def delete_note(self,note):
        if not note:
            return None
        self.notebook.delete_note(note)
        return True

    def update_notebook(self):
        NotebookStorage.to_file(self.notebook, 'notebook.json')

