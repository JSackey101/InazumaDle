import pytest
from unittest.mock import patch, mock_open, MagicMock
from io import StringIO
from players import Player
from utilities import read_player_data, ErrorRaising

def test_read_player_data(test_player_data):
    """ Tests whether the list of Player objects is created correctly. """
    with patch("builtins.open", mock_open(read_data=test_player_data)):
        players = read_player_data("test.csv")
        assert isinstance(players, list)
        assert all(isinstance(player, Player) for player in players)
        assert len(players) == 2

def test_validate_str():
    """ Tests whether a TypeError is raised when a non string is input. """
    with pytest.raises(TypeError):
        ErrorRaising.validate_str(10)


def test_validate_char_space():
    """ Tests whether a ValueError is raised when an input string is not
        only characters and spaces. """
    with pytest.raises(ValueError):
        ErrorRaising.validate_char_space("test 1")


def test_validate_digits():
    """ Tests whether a ValueError is raised when an input string is not
        only digits. """
    with pytest.raises(ValueError):
        ErrorRaising.validate_digits("12four5")
