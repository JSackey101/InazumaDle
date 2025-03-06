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
