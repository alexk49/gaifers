import pytest
from unittest.mock import patch

from gaifers import noughts


@pytest.fixture
def gameboard():
    return noughts.GameBoard()


@pytest.fixture
def test_player():
    return noughts.Player()


@pytest.fixture
def mock_input():
    with patch("builtins.input") as mocked_input:
        yield mocked_input


def test_new_board(gameboard):
    board = gameboard.new_board()
    assert type(board) is list

    # check all blank
    for tile in board:
        assert tile == " "


"""
def test_play_as(mock_input, test_player):
    mock_input.side_effect = ["z", "x"]

    result = test_player.play_as()
    assert result == "x"
"""
