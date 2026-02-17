import json

from notebook import Notebook
from note import Note

class NotebookStorage:
    @staticmethod
    def from_file(filename):
        notebook = Notebook()
        try:
            with open(filename) as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        for note in data:
            note = Note(note['id'], note['title'], note['description'], note['date'], note['tag'])
            notebook.add_note(note)
        return notebook

    @staticmethod
    def to_file(notebook, filename):
        with open(filename, 'w') as file:
            json_data = [note.to_dict() for note in notebook.notes]
            json.dump(json_data, file, indent = 4)


