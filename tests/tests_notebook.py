from Notebook.notebook import Notebook
from Notebook.note import Note

#-----------------------------------------------------------------------------------------------------------------------
#self.notes = []
def test_check_nb_len_empty():

    notebook = Notebook()

    assert notebook.check_notebook_len() is False


#self.notes = None
def test_check_nb_len_none():

    notebook = Notebook()
    notebook.notes = None

    assert notebook.check_notebook_len() is False


# self.notes = [1object]
def test_check_nb_len_1():

    notebook = Notebook()
    note = Note(1,'title','description','date','tag')

    notebook.notes = [note]

    assert notebook.check_notebook_len() is True


    # more than 1 object in self.notes
def test_check_nb_len_plus1():
    notebook = Notebook()
    notebook.notes = [
        Note(1, 'title', 'description', 'date', 'tag'),
        Note(2, 'title', 'description', 'date', 'tag')
        ]

    assert notebook.check_notebook_len() is True





#-----------------------------------------------------------------------------------------------------------------------


