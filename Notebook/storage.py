import csv

from service import Notebook, Note

class NotebookStorage:
    @staticmethod
    def from_file(filename):
        notebook = Notebook()
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                note = Note(row['id'], row['title'], row['description'], row['date'], row['tag'])
                notebook.add(note)
        return notebook
            #notebook storage

    @staticmethod
    def to_file(notebook, filename):
        with open(filename, 'w') as file:
            writer = csv.DictWriter(file,fieldnames = ['id', 'title', 'description', 'date', 'tag'])
            writer.writeheader()
            for note in notebook.notes:
                writer.writerow(note.to_dict())