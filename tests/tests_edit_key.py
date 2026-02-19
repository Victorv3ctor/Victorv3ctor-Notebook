from Notebook.notebook import Notebook
import pytest

@pytest.mark.parametrize('choose_key, expected', [
    (0, False),
    (1, 'title'),
    (2, 'description'),
    (3, 'date'),
    (4, 'tag'),
    (5, False),
    ('a', False)
])

def test_edit_key(choose_key, expected):
    notebook = Notebook()

    result = notebook.get_edit_key(choose_key)

    assert result == expected