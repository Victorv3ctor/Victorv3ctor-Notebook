from Notebook.notebook import Notebook
from Notebook.note import Note
from Notebook.storage import NotebookStorage

def test_integration_storage_with_notes(tmp_path):

    notebook = Notebook()
    notebook.add_note(Note(1,'Wiktor','Yes','21/05/25','java'))
    notebook.add_note(Note(2,'Kamila','No','23/02/26','python'))

    filename = tmp_path / 'notebook.json'
    NotebookStorage.to_file(notebook, filename)

    loaded_notebook = NotebookStorage.from_file(filename)

    assert len(loaded_notebook.notes) == 2
    assert loaded_notebook.notes[0].title == 'Wiktor'
    assert loaded_notebook.notes[0].note_id == 1
    assert loaded_notebook.notes[1].title == 'Kamila'
    assert loaded_notebook.notes[1].tag == 'python'



def test_integration_storage_empty_note_fields(tmp_path):

    notebook = Notebook()

    filename = tmp_path / 'notebook.json'

    NotebookStorage.to_file(notebook,filename)

    loeaded_notebook = NotebookStorage.from_file(filename)

    assert loeaded_notebook.notes == []
    assert notebook.get_notes() == []
    assert filename.exists()

