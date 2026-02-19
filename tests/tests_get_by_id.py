from Notebook.notebook import Notebook
from Notebook.note import Note
import pytest


@pytest.mark.parametrize('notes_list, test_input, expected_obj, expected_note_id, expected_note_title', [
    #empty self.notes
    ([], 1, None),

    #self.notes 1 note
    ([Note(1,'hi','description','date','tag')], 1, Note, 1,'hi'),

    #note.id str
    ([Note("2",'hi1','description','date','tag')], 2, Note, 2,'hi1'),

    #wrong user_input_id
    ([Note(1,'hi2','description','date','tag')],3, None, None,None)
])

def test_get_note_by_id(notes_list, test_input, expected_obj, expected_note_id, expected_note_title):

    notebook = Notebook()
    notebook.notes = notes_list

    note = notebook.get_note_by_id(test_input)

    if expected_obj is None:
        assert note is None

    assert isinstance(note, expected_obj)
    assert int(note.note_id) == expected_note_id
    assert note.title == expected_note_title
    assert note is not None
























