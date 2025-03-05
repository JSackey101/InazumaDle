import pytest

@pytest.fixture
def test_player_data():
    """ Returns CSV format player data. """
    return """nickname,name,element,gender,position,year
endou,endou mamoru,mountain,male,GK,2
kazemaru,kazemaru ichirouta,wind,male,DF,2"""
