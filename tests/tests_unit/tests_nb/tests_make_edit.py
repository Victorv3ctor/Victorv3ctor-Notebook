from Notebook.note import Note
from Notebook.notebook import Notebook

def test_make_edit_correct():

    note = Note(1,'t','d','d','t')
    key = 'title'
    value = 'new_title'

    Notebook.make_edit(note, key, value)

    assert note.title == 'new_title'

def test_make_edit_incorrect_key():
    note = Note(1,'t','d','d','t')

    key = 'tittttle'
    value = 'test_title'

    original_title = note.title

    Notebook.make_edit(note, key, value)

    assert note.title == original_title









