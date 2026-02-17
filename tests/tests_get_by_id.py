from Notebook.notebook import Notebook
from Notebook.note import Note
import pytest

# def get_note_by_id(self, note_id):
#     for note in self.notes:
#         if note_id == int(note.note_id):
#             return note
#     return None

# @pytest.mark.parametrize('test_input, expected', [
#     (2, True), (1, False), (10, False), (0, False), (-1, False)])
# def test_check_move(test_input, expected):
#     board = Board()
#     board.game_board[0] = 'x'
#
#     assert board.check_move(test_input) is expected

#self.notes = []
def test_get_id_empty():

    notebook = Notebook()
    notebook.notes = []

    note = notebook.get_note_by_id(1)
    assert note is None


#self.notes = [Note]
def test_get_id():

    notebook = Notebook()
    notebook.notes = [
        Note(1,'title','description','date','tag')
    ]

    note = notebook.get_note_by_id(1)
    assert isinstance(note, Note)
    assert note.note_id == 1
    assert note.title == 'title'
    assert not note is None

#self.notes = [Note]
def test_get_id_str():

    notebook = Notebook()

    notebook.notes = [
        Note("2",'title2','description','date','tag')
    ]

    note = notebook.get_note_by_id(2)
    assert isinstance(note, Note)
    assert int(note.note_id) == 2
    assert note.title == 'title2'
    assert not note is None























