import pytest
from unittest.mock import patch, mock_open
from rich.console import Console
from players import Player
from utilities import ErrorRaising, Utility

class TestErrorRaising():
    """ A class to test the ErrorRaising class. """

    @staticmethod
    def test_read_player_data(test_player_data):
        """ Tests whether the list of Player objects is created correctly. """
        with patch("builtins.open", mock_open(read_data=test_player_data)):
            players = Utility.read_player_data("test.csv")
            assert isinstance(players, list)
            assert all(isinstance(player, Player) for player in players)
            assert len(players) == 2

    @staticmethod
    def test_validate_str():
        """ Tests whether a TypeError is raised when a non string is input. """
        with pytest.raises(TypeError):
            ErrorRaising.validate_str(10)

    @staticmethod
    def test_validate_char_space():
        """ Tests whether a ValueError is raised when an input string is not
            only characters and spaces. """
        with pytest.raises(ValueError):
            ErrorRaising.validate_char_space("test 1")

    @staticmethod
    def test_validate_digits():
        """ Tests whether a ValueError is raised when an input string is not
            only digits. """
        with pytest.raises(ValueError):
            ErrorRaising.validate_digits("12four5")

    @staticmethod
    def test_validate_two_inputs():
        """ Tests whether a ValueError is raised when an input string is not 
            either of 2 inputs. """
        with pytest.raises(ValueError):
            ErrorRaising.validate_two_inputs("test", "True", "False")

    @staticmethod
    def test_validate_one_name():
        """ Tests whether a ValueError is raised when input string contains more than 1 name. """
        with pytest.raises(ValueError):
            ErrorRaising.validate_one_name("jeffrey sackey")

    @staticmethod
    def test_validate_empty_string():
        """ Tests whether a ValueError is raised when input string is empty. """
        with pytest.raises(ValueError):
            ErrorRaising.validate_not_empty("")
    
    @staticmethod
    def test_validate_whitespace_string():
        """ Tests whether a ValueError is raised when input string is only whitespace. """
        with pytest.raises(ValueError):
            ErrorRaising.validate_not_empty("   ")

    @staticmethod
    def test_validate_console():
        """ Tests whether a TypeError is raised when input is not
            a rich.console.Console object. """
        with pytest.raises(TypeError):
            ErrorRaising.validate_console("string")

class TestUtility():
    """ A class to test the Utility class. """

    @staticmethod
    def test_get_input_leading(test_console):
        """ Tests whether leading space is removed. """
        test_console.input.return_value = "  input"
        val = Utility.get_input(test_console, "Enter Input Here: ")

        assert val == "input"

    @staticmethod
    def test_get_input_trailing(test_console):
        """ Tests whether trailing space is removed. """
        test_console.input.return_value = "input  "
        val = Utility.get_input(test_console, "Enter Input Here: ")

        assert val == "input"

    @staticmethod
    def test_get_input_lowercase(test_console):
        """ Tests whether input is made lowercase. """
        test_console.input.return_value = "iNpUt"
        val = Utility.get_input(test_console, "Enter Input Here: ")

        assert val == "input"

    @staticmethod
    def test_option_one():
        """ Tests whether 1 is returned when the input matches the first option. """
        option = Utility.check_two_options("True", "True", "False")
        assert option == 1

    @staticmethod
    def test_option_two():
        """ Tests whether 2 is returned when the input matches the second option. """
        option = Utility.check_two_options("False", "True", "False")
        assert option == 2

    @staticmethod
    def test_search_first(test_players_no_dupes):
        """ Tests whether a list with the correct Player object 
            is returned for a matching first name. """
        matches = Utility.search_first_nick_name(test_players_no_dupes, "shourinji")
        assert isinstance(matches, list)
        assert len(matches) == 1
        assert matches[0] == test_players_no_dupes[0]

    @staticmethod
    def test_search_first_case(test_players_no_dupes):
        """ Tests whether a list with the correct Player object is 
            returned for a matching first name regardless of case. """
        matches = Utility.search_first_nick_name(
            test_players_no_dupes, "shouRInji")
        assert isinstance(matches, list)
        assert len(matches) == 1
        assert matches[0] == test_players_no_dupes[0]

    @staticmethod
    def test_search_first_two(test_players_same_first):
        """ Tests whether a list with the correct Player objects is returned 
            for a matching first name if more than 1 matches are found. """
        matches = Utility.search_first_nick_name(
            test_players_same_first, "shourinji")
        assert isinstance(matches, list)
        assert len(matches) == 2
        assert matches[0] == test_players_same_first[0]
        assert matches[1] == test_players_same_first[1]

    @staticmethod
    def test_search_nick(test_players_no_dupes):
        """ Tests whether a list with the correct Player object 
            is returned for a matching nickname. """
        matches = Utility.search_first_nick_name(
            test_players_no_dupes, "shourin")
        assert isinstance(matches, list)
        assert len(matches) == 1
        assert matches[0] == test_players_no_dupes[0]

    @staticmethod
    def test_search_nick_case(test_players_no_dupes):
        """ Tests whether a list with the correct Player object is 
            returned for a matching nickname regardless of case. """
        matches = Utility.search_first_nick_name(
            test_players_no_dupes, "shouRIn")
        assert isinstance(matches, list)
        assert len(matches) == 1
        assert matches[0] == test_players_no_dupes[0]

    @staticmethod
    def test_search_nick_two(test_players_same_nick):
        """ Tests whether a list with the correct Player objects is returned 
            for a matching nickname if more than 1 matches are found. """
        matches = Utility.search_first_nick_name(
            test_players_same_nick, "shourin")
        assert isinstance(matches, list)
        assert len(matches) == 2
        assert matches[0] == test_players_same_nick[0]
        assert matches[1] == test_players_same_nick[1]

    @staticmethod
    def test_search_last(test_players_no_dupes):
        """ Tests whether a list with the correct Player object 
            is returned for a matching last name. """
        matches = Utility.search_last_name(
            test_players_no_dupes, "sakichi")
        assert isinstance(matches, list)
        assert len(matches) == 1
        assert matches[0] == test_players_no_dupes[1]

    @staticmethod
    def test_search_last_case(test_players_no_dupes):
        """ Tests whether a list with the correct Player object is 
            returned for a matching last name regardless of case. """
        matches = Utility.search_last_name(
            test_players_no_dupes, "SaKichi")
        assert isinstance(matches, list)
        assert len(matches) == 1
        assert matches[0] == test_players_no_dupes[1]

    @staticmethod
    def test_search_last_two(test_players_same_last):
        """ Tests whether a list with the correct Player objects is returned 
            for a matching last name if more than 1 matches are found. """
        matches = Utility.search_last_name(
            test_players_same_last, "ayumu")
        assert isinstance(matches, list)
        assert len(matches) == 2
        assert matches[0] == test_players_same_last[0]
        assert matches[1] == test_players_same_last[1]
