import pytest
from unittest.mock import patch, mock_open, MagicMock
from io import StringIO
from players import Player
from utilities import read_player_data

def test_read_player_data(test_player_data):
    """ Tests whether the list of Player objects is created correctly. """
    with patch("builtins.open", mock_open(read_data=test_player_data)):
        players = read_player_data("test.csv")
        assert isinstance(players, list)
        assert all(isinstance(player, Player) for player in players)
        assert len(players) == 2
