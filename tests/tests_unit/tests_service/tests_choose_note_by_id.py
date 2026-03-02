from unittest.mock import Mock
from Notebook.service import Service
from Notebook.note import Note


def test_choose_note_by_id_none():

    notebook_mock = Mock()
    service = Service(notebook_mock)

    notebook_mock.get_note_by_id.return_value = None

    result = service.choose_note_by_id(1)

    assert result is None

    assert notebook_mock.get_note_by_id.call_count == 1

def test_choose_note_by_id_note():
    notebook_mock = Mock()
    service = Service(notebook_mock)

    note = Note(1,'t','d','d','t')

    notebook_mock.get_note_by_id.return_value = note

    result = service.choose_note_by_id(10)
    assert result == note
    assert notebook_mock.get_note_by_id.call_count == 1









