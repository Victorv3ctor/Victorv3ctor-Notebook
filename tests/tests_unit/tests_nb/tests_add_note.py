from Notebook.notebook import Notebook
from Notebook.note import Note
import pytest

@pytest.fixture
def nb():
    return Notebook()

def test_empty_notebook_add_note(nb):
    assert len(nb.notes) == 0

    note = Note(1, 't', 'd', 'd', 't')

    nb.add_note(note)

    assert len(nb.notes) == 1
    assert nb.notes[0].title == 't'
    assert nb.notes[0].note_id == 1

def test_filled_notebook_add_note(nb):
    assert len(nb.notes) == 0

    note = Note(1,'t1','d','d','java')
    nb.add_note(note)

    assert len(nb.notes) == 1

    note1 = Note(2,'t2','d2','d3','python')

    nb.add_note(note1)

    assert len(nb.notes) == 2

    assert nb.notes[0].note_id == 1
    assert nb.notes[0].title == 't1'
    assert nb.notes[1].note_id == 2
    assert nb.notes[1].title == 't2'
























