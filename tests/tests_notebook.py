from Notebook.notebook import Notebook
from Notebook.note import Note
import pytest

@pytest.mark.parametrize('notes_list, expected',[
    #empty self.notes
    ([], False),

    #self.notes with 1 note
    ([Note(1,'title','description','date','tag')], True),

    #self.notes with more than 1 note
    (
        [Note(1,'title','description','date','tag'),
        Note(1,'title','description','date','tag')], True)
])

def test_notebook_len(notes_list, expected):
    notebook = Notebook()

    notebook.notes = notes_list

    assert notebook.check_notebook_len() is expected






#-----------------------------------------------------------------------------------------------------------------------


