import pytest
from gaifers import hangman


def test_check_for_hangman_winner():
    assert not hangman.check_for_hangman_winner("test", "fail")
    assert hangman.check_for_hangman_winner("word", "word")


def test_check_word_for_guess():

    result, success = hangman.check_word_for_guess("a", "cramp", "     ")

    assert result == "  a  "
    assert success is True

    result, success = hangman.check_word_for_guess("z", "cramp", "     ")

    assert result == "     "
    assert success is False


def test_set_hangman_data():
    gd = hangman.set_hangman_data()

    assert gd["gameData"]["word"] != ""

    assert gd["gameData"]["word_length"] == len(gd["gameData"]["word"])

    assert "_" in gd["gameData"]["current_word_state"]


def test_get_user_guess(mock_input):
    mock_input.side_effect = ["1", "2", "s"]
    guess = hangman.get_user_guess(mock_input.side_effect)
    assert guess == "s"


