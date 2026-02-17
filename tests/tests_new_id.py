from Notebook.notebook import Notebook
from Notebook.note import Note

#self.notes = []
def test_create_id_empty():

    notebook = Notebook()

    assert notebook.create_new_id() == 1


#self.notes = [1note]
def test_create_id_1note():

    notebook = Notebook()

    notebook.notes = [
        Note(2,'title','description','date','tag')
    ]

    assert notebook.create_new_id() == 3 #return highest +1 -> max[2] = 2 + 1


#self.notes = [2notes] # check if max is working
def test_create_id_notes():

    notebook = Notebook()

    notebook.notes = [
        Note(3, 'title', 'description', 'date', 'tag'),
        Note(5, 'title', 'description', 'date', 'tag')
    ]

    assert notebook.create_new_id() == 6 #return highest +1 -> max[3,5] = 5 + 1


#note_id = "str number"
def test_create_new_id_str():

    notebook = Notebook()

    notebook.notes = [Note("4",'title','description','date','tag')]

    assert notebook.create_new_id() == 5 #max[int("4")] = 4 + 1


def test_create_id_duplicate():

    notebook = Notebook()

    notebook.notes = [
        Note("10",'title','description','date','tag'),
        Note("10", 'title1', 'description1', 'date1', 'tag1')
        ]

    assert notebook.create_new_id() == 11 #max[10,10] = 10 + 1

def test_create_id_various():

    notebook = Notebook()

    notebook.notes = [
        Note("10",'title','description','date','tag'),
        Note("11", 'title1', 'description1', 'date1', 'tag1'),
        Note(12, 'title1', 'description1', 'date1', 'tag1')
        ]

    assert notebook.create_new_id() == 13




















