from Notebook.notebook import Notebook
from Notebook.note import Note
from Notebook.ui import UI


#DO PRZETESTOWANIA

import pytest
from unittest.mock import Mock
from unittest.mock import patch


@pytest.fixture
def empty_notebook(tmp_path, monkeypatch):
    file = tmp_path / 'notebook.json'
    file.write_text("[]")
    monkeypatch.chdir(tmp_path)

    return file

def filled_notebook(tmp_path, monkeypatch):
    file = tmp_path / 'notebook.json'
    file.write_text("[]")
    monkeypatch.chdir(tmp_path)

    ui = UI()
    ui.notebook.add_note(Note(1,'t','d','d','t'))
    ui.storage.to_file(ui.notebook.notes, tmp_path)

    return file

def test_handle_show_notebook(empty_notebook):
    ui = UI()

    assert len(ui.notebook.notes) == 0



