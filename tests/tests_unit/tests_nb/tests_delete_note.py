from Notebook.notebook import Notebook
from Notebook.note import Note

def test_delete_note_correct():
    notebook = Notebook()

    note = Note(1,'t','d','d','t')
    note1 = Note(2,'t','d','d','t')

    notebook.notes = [note,note1]
    assert len(notebook.notes) == 2
    notebook.delete_note(note)

    assert note not in notebook.notes
    assert len(notebook.notes) == 1



def test_delete_note_incorrect():
    notebook = Notebook()

    note = Note(1,'t','d','d','t')
    note1 = Note(2,'t','d','d','t')
    note3 = Note(1,'t','d','d','t')

    notebook.notes = [note,note1]
    notebook.delete_note(note3)

    assert len(notebook.notes) == 2




