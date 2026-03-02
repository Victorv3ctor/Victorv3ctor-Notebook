from Notebook.notebook import Notebook
from Notebook.note import Note
import pytest


@pytest.mark.parametrize('notes_list, expected',[

    ([], 1),


    ([Note(2,'title','description','date','tag')], 3),


    ([Note("2",'title','description','date','tag')], 3),


    ([Note(2, 'title', 'description', 'date', 'tag'),
      Note(3, 'title', 'description', 'date', 'tag')], 4),


    ([Note("2", 'title', 'description', 'date', 'tag'),
      Note(4, 'title', 'description', 'date', 'tag')], 5)
])


def test_create_new_id(notes_list, expected):
    notebook = Notebook()
    notebook.notes = notes_list

    created_id = notebook.create_new_id()

    assert created_id == expected






















