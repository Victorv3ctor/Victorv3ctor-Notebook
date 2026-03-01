from unittest.mock import patch
from Notebook.ui import UI

@patch('Notebook.ui.input', side_effect = ["1", "2", "3", "str"])

def test_mini_menu(mock_input):
    ui = UI()


    result = ui.mini_menu()
    result1 = ui.mini_menu()
    result2 = ui.mini_menu()
    result3 = ui.mini_menu()

    assert result is True
    assert result1 is False
    assert result2 is False
    assert result3 is False

    assert mock_input.call_count == 4
    mock_input.assert_called()





