import pytest

from gaifers import noughts


def test_update_turn_marker():
    assert noughts.update_turn_marker("x") == "o"
    assert noughts.update_turn_marker("o") == "x"


def test_validate_marker():
    assert noughts.validate_marker("x") is True

    assert noughts.validate_marker("o") is True

    assert noughts.validate_marker("a") is False


def test_check_for_draw():
    game_data = noughts.game_data_default

    assert noughts.check_for_draw(game_data) == False

    game_data["gameData"]["boardData"]["top-left"] = "x"
    game_data["gameData"]["boardData"]["top-center"] = "o"
    game_data["gameData"]["boardData"]["top-right"] = "x"
    game_data["gameData"]["boardData"]["middle-left"] = "x"
    game_data["gameData"]["boardData"]["center"] = "o"
    game_data["gameData"]["boardData"]["middle-right"] = "o"
    game_data["gameData"]["boardData"]["bottom-left"] = "o"
    game_data["gameData"]["boardData"]["bottom-center"] = "x"
    game_data["gameData"]["boardData"]["bottom-right"] = "x"

    assert noughts.check_for_draw(game_data) == True


def test_check_for_winner():
    game_data = noughts.game_data_default.copy()

    assert noughts.check_for_winner(game_data) == []

    game_data["gameData"]["playerMarker"] = "x"

    game_data["gameData"]["boardData"]["top-left"] = "x"
    game_data["gameData"]["boardData"]["top-center"] = "x"
    game_data["gameData"]["boardData"]["top-right"] = "x"

    assert noughts.check_for_winner(game_data) == ["top-left", "top-center", "top-right"]


def test_validate_game_data():
    game_data = noughts.game_data_default.copy()
    org_game_data = noughts.game_data_default.copy()

    game_data["gameData"]["playerMarker"] = "x"
    game_data["gameData"]["new_position"] = "top-left"
    game_data["gameData"]["boardData"]["top-left"] = "y"
    
    org_game_data["gameData"]["new_position"] = "top-right"
    org_game_data["gameData"]["boardData"]["top-right"] = "x"
    org_game_data["gameData"]["boardData"]["top-left"] = "x"

    assert noughts.validate_game_data(game_data, org_game_data) is False
