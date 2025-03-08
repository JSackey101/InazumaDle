import pytest
from unittest.mock import MagicMock
from rich.console import Console
from players import Player

@pytest.fixture
def test_player_data():
    """ Returns CSV format player data. """
    return """nickname,name,element,gender,position,year
endou,endou mamoru,mountain,male,GK,2
kazemaru,kazemaru ichirouta,wind,male,DF,2"""

@pytest.fixture
def test_console():
    """ Returns a Mock Console object. """
    return MagicMock(spec=Console)

@pytest.fixture()
def test_players_no_dupes():
    """ Returns a list of Player objects with no duplicate values. """
    header_info = "nickname,name,element,gender,position,year".split(",")
    player_one = "shourin,shourinji ayumu,forest,male,MF,1".split(",")
    player_two = "shishido,shishido sakichi,fire,male,MF,1".split(",")
    return [Player(player, header_info) for player in (player_one, player_two)]


@pytest.fixture()
def test_players_same_nick():
    """ Returns a list of Player objects with the same nickname. """
    header_info = "nickname,name,element,gender,position,year".split(",")
    player_one = "shourin,shourinji ayumu,forest,male,MF,1".split(",")
    player_two = "shourin,shishido sakichi,fire,male,MF,1".split(",")
    return [Player(player, header_info) for player in (player_one, player_two)]


@pytest.fixture()
def test_players_same_first():
    """ Returns a list of Player objects with the same first name. """
    header_info = "nickname,name,element,gender,position,year".split(",")
    player_one = "shourin,shourinji ayumu,forest,male,MF,1".split(",")
    player_two = "shishido,shourinji sakichi,fire,male,MF,1".split(",")
    return [Player(player, header_info) for player in (player_one, player_two)]


@pytest.fixture()
def test_players_same_last():
    """ Returns a list of Player objects with the same last name. """
    header_info = "nickname,name,element,gender,position,year".split(",")
    player_one = "shourin,shourinji ayumu,forest,male,MF,1".split(",")
    player_two = "shishido,shishido ayumu,fire,male,MF,1".split(",")
    return [Player(player, header_info) for player in (player_one, player_two)]
