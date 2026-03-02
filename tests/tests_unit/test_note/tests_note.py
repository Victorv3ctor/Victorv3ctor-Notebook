from Notebook.note import Note
import pytest

@pytest.fixture
def note():
    return Note(1,'t','d','d','t')
@pytest.fixture
def new():
    return 'test'


def test_note_to_dict(note):


    result = note.to_dict()

    assert isinstance(result, dict)
    assert result['id'] == 1
    assert result['title'] == 't'
    assert result['description'] == 'd'
    assert result['date'] == 'd'
    assert result['tag'] == 't'

def test_note_str(note):


    result = str(note)

    assert 'TITLE' in result
    assert 'ID' in result
    assert 'Date' in result
    assert 'Tag' in result

def test_change_title(note, new):
    assert note.title == 't'


    note.change_title(new)
    assert note.title == 'test'

def test_change_description(note, new):

    assert note.description == 'd'


    note.change_description(new)
    assert note.description == 'test'

def test_change_date(note, new):

    assert note.date == 'd'

    note.change_date(new)
    assert note.date == 'test'

def test_change_tag(note, new):
    assert note.tag == 't'

    note.change_tag(new)

    assert note.tag == 'test'






