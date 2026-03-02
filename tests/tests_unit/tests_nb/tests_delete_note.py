from Notebook.notebook import Notebook
from Notebook.note import Note
import pytest

@pytest.mark.parametrize('notes, delete_note_id, expected_len_notes', [
    ([Note(1,'t','d','d','t')], 1, 0),

    ([Note(2,'t','d','d','t')],1, 1),

    ([
        Note(1,'t','d','d','t'),
        Note(2,'t','d','d','t')], 3, 2),

    ([Note(2, 't', 'd', 'd', 't')], 0, 1),
])

def test_delete_note(notes, delete_note_id, expected_len_notes):
    notebook = Notebook()
    notebook.notes = notes

    note = notebook.get_note_by_id(delete_note_id)

    if note:
        notebook.delete_note(note)
    elif note is None:
        assert note is None

    assert len(notebook.notes) == expected_len_notes




