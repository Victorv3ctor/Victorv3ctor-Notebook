from unittest.mock import patch
from Notebook.ui import UI
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def empty_notebook(tmp_path, monkeypatch):
    file = tmp_path / 'notebook.json'
    file.write_text("[]")
    monkeypatch.chdir(tmp_path) 



@patch('Notebook.ui.input', side_effect = ['t_title','t_descr','t_date', 't_tag'])
def test_handle_add_note_note(mock_input, empty_notebook):

    ui = UI()
    assert len(ui.notebook.notes) == 0

    ui.handle_add_note()

    assert len(ui.notebook.notes) == 1
    assert ui.notebook.notes[0].note_id == 1
    assert ui.notebook.notes[0].title == 't_title'
    assert ui.notebook.notes[0].description == 't_descr'
    assert ui.notebook.notes[0].date == 't_date'
    assert ui.notebook.notes[0].tag == 't_tag'

    assert mock_input.call_count == 4
    mock_input.assert_called()














