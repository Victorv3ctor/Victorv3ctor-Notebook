from unittest.mock import patch
from Notebook.ui import UI
from Notebook.note import Note
import pytest

@pytest.fixture
def empty_notebook(tmp_path, monkeypatch):
    notebook_file = tmp_path / 'notebook.json'
    notebook_file.write_text("[]")
    monkeypatch.chdir(tmp_path)
    return notebook_file

@pytest.fixture
def notebook_filled(tmp_path, monkeypatch):
    notebook_file = tmp_path / 'notebook.json'
    monkeypatch.chdir(tmp_path)
    notebook_file.write_text("[]")

    ui = UI()
    ui.notebook.add_note(Note(1,'t','d','d','t'))
    ui.storage.to_file(ui.notebook, 'notebook.json')

    return notebook_file



def test_choose_note_empty_notebook(empty_notebook):
    ui = UI()

    result = ui.choose_note()
    assert result is None


@patch('Notebook.ui.UI._get_int_input', return_value = 1)
def test_choose_note_valid_id(mock_get_int_input, notebook_filled):
    ui = UI()

    assert len(ui.notebook.notes) == 1

    result = ui.choose_note()

    assert result.note_id == 1
    assert ui.notebook.notes[0].note_id == 1

    mock_get_int_input.assert_called()
    assert mock_get_int_input.call_count == 1


@patch('Notebook.ui.UI._get_int_input', return_value = 2)
def test_choose_note_invalid_id(mock_get_int_input, notebook_filled):

    ui = UI()

    result = ui.choose_note()
    assert result is None
    assert ui.notebook.notes[0].note_id == 1

















