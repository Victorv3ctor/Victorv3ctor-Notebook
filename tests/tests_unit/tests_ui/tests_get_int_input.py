from Notebook.ui import UI
from unittest.mock import patch

@patch('Notebook.ui.input', side_effect = ["1", "2", "Three"])
def test_get_int_input(mock_input):
    ui = UI()

    result = ui._get_int_input("message", "error_msg")
    result1 = ui._get_int_input("message", "error_msg")
    result2 = ui._get_int_input("message", "error_msg")

    assert result == 1
    assert result1 == 2
    assert result2 is None
    assert mock_input.call_count == 3
