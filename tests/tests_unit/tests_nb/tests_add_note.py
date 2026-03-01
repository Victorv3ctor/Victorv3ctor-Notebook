from Notebook.notebook import Notebook
from Notebook.note import Note


#add note to empty self.notes
def test_add_note_empty_notes():
    notebook = Notebook()
    #check with notebook.note starts empty
    assert notebook.notes == []

    note = Note(1,'t','d','d','t')

    notebook.add_note(note)
    assert note in notebook.notes

#add note to self.notes with existing notes
def test_add_note_existing_notes():

    notebook = Notebook()
    #check if notebook.notes starts empty
    assert notebook.notes == []

    note = Note(2,'title','desc','date','tag')
    note1 = Note(3,'title1','desc1','date1','tag1')


    notebook.add_note(note)

    notebook.add_note(note1)

    assert note in notebook.notes
    assert note1 in notebook.notes
    assert len(notebook.notes) == 2















