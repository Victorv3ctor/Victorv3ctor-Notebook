from Notebook.notebook import Notebook
from Notebook.note import Note
import pytest


@pytest.mark.parametrize('notes_list, user_input, expected_note_id', [
    ([],1,None),

    ([Note(1,'t','d','d','java')], 1, 1),

    ([Note(3,'t','d','d','python')], 3, 3),

    ([Note(5,'t','d','d','t')],4, None)

])

def test_get_note_by_id(notes_list, user_input, expected_note_id):
    notebook = Notebook()
    notebook.notes = notes_list

    result = notebook.get_note_by_id(user_input)

    if expected_note_id is None:
        assert result is None
    else:
        assert result is not None
        assert result.note_id == expected_note_id




























