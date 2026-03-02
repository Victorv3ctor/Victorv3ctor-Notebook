from Notebook.service import Service
from unittest.mock import Mock
from Notebook.note import Note


def test_get_notes_empty():
    notebook_mock = Mock()
    service = Service(notebook_mock)

    notebook_mock.get_nb_notes.return_value = None

    result = service.get_notes()
    assert result is None

    assert notebook_mock.get_nb_notes.call_count == 1

def test_get_notes_filled_notes():

    notebook_mock = Mock()
    service = Service(notebook_mock)

    note = Note(1,'t','d','d','d')

    notebook_mock.get_nb_notes.return_value = note

    result = service.get_notes()
    assert result == note

    assert notebook_mock.get_nb_notes.call_count == 1













