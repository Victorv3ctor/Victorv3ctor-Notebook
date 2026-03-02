from Notebook.notebook import Notebook
from Notebook.note import Note
import pytest

@pytest.fixture
def empty_notebook():
    return Notebook()

@pytest.fixture
def filled_notebook():
    notebook = Notebook()
    note = Note(1,'t','d','d','t')

    notebook.add_note(note)

    return notebook

def test_get_nb_notes(empty_notebook):
    notebook = empty_notebook

    assert len(notebook.notes) == 0

    result = notebook.get_nb_notes()

    assert len(result) == 0
    assert isinstance(result, list)


def test_nb_notes(filled_notebook):
    notebook = filled_notebook
    assert len(notebook.notes) == 1

    result = notebook.get_nb_notes()
    result.append('FAKE NOTE')

    assert len(result) == 2
    assert len(notebook.notes) == 1
    assert isinstance(result, list)



