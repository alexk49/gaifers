from unittest.mock import patch

import pytest

from gaifers import noughts


@pytest.fixture
def gameboard():
    return noughts.GameBoard()


@pytest.fixture
def mock_input():
    """Provides mocked input for python built in input
    mock_input can be reused across tests"""
    with patch("builtins.input") as mocked_input:
        yield mocked_input


@pytest.fixture
def test_player(mock_input):
    """Player marker defined on init
    Tests faulty input then assigns x as marker"""
    mock_input.side_effect = ["z", "20", "x"]
    test_player = noughts.Player()
    assert test_player.marker == "x"
    return test_player


def test_player_choose_position(test_player, mock_input):
    mock_input.side_effect = ["0", "-10", "20", "a" "words", "8"]
    assert test_player.choose_position() == 8


def test_new_board(gameboard):
    board = gameboard.new_board()
    assert type(board) is list

    # check all blank
    for tile in board:
        assert tile == " "


def test_update_board(gameboard):
    gameboard.new_board()

    assert gameboard.validate_position(8) is True
    gameboard.update_board(8, "x")

    assert gameboard.board[7] == "x"

    assert gameboard.validate_position(8) is False


def test_check_for_winner(gameboard):
    gameboard.new_board()

    assert gameboard.check_for_winner("o") is False
    assert gameboard.check_for_winner("x") is False

    gameboard.update_board(1, "x")
    gameboard.update_board(2, "x")
    gameboard.update_board(3, "x")

    assert gameboard.check_for_winner("o") is False
    assert gameboard.check_for_winner("x") is True


def test_for_draw(gameboard):
    gameboard.new_board()

    assert gameboard.check_for_draw() is False

    gameboard.update_board(1, "x")
    gameboard.update_board(2, "o")
    gameboard.update_board(3, "x")
    gameboard.update_board(4, "x")
    gameboard.update_board(5, "o")
    gameboard.update_board(6, "o")
    gameboard.update_board(7, "o")
    gameboard.update_board(8, "x")
    gameboard.update_board(9, "x")

    assert gameboard.check_for_winner("x") is False
    assert gameboard.check_for_winner("o") is False

    assert gameboard.check_for_draw() is True
