import os
import csv
from players import Player
from rich.console import Console

class ErrorRaising():
    """ Class for raising errors. """

    @staticmethod
    def validate_str(input_val: str) -> None:
        """ Validates that input is a string. """
        if not isinstance(input_val, str):
            raise TypeError("Input must be a string. ")
    @staticmethod
    def validate_char_space(input_val: str) -> None:
        """ Validates that input contains only characters and spaces. """
        if not all(char.isalpha() or char.isspace() for char in input_val):
            raise ValueError("Input must consist of only characters and spaces. ")
    @staticmethod
    def validate_digits(input_val: str) -> None:
        """ Validates that input contains only digits. """
        if not all(char.isdigit() for char in input_val):
            raise ValueError("Input must consist of only digits. ")
    @staticmethod
    def validate_two_inputs(input_val: str, first_acc_input: str, second_acc_input: str) -> None:
        """ Validates that the input is one of the accepted inputs. """
        if input_val.strip().capitalize() not in [first_acc_input, second_acc_input]:
            raise ValueError(f"Input must be either '{first_acc_input}' or '{second_acc_input}'.")

    @staticmethod
    def validate_one_name(input_val: str):
        """ Validates that the input only contains 1 name. """
        if len(input_val.split()) != 1:
            raise ValueError("Input must contain only 1 name. ")
    @staticmethod
    def validate_not_empty(input_val: str):
        """ Validates that the input is not empty (either "" or whitespace only). """
        if not input_val.strip():
            raise ValueError("Input must not be empty. ")

class Utility():
    """ Class containing utility functions for the program. """


    ABS_PATH = os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def get_input(console: Console, input_msg: str) -> str:
        """ Takes an input, removes leading/trailing spaces and makes it all lowercase. """
        ErrorRaising.validate_str(input_msg)
        input_val = console.input(input_msg).strip().lower()
        return input_val
    @staticmethod
    def check_two_options(input_val: str, first_acc_input: str, second_acc_input: str) -> int:
        """ Checks which one of the accepted inputs the given input matches. """
        ErrorRaising.validate_str(input_val)
        ErrorRaising.validate_str(first_acc_input)
        ErrorRaising.validate_str(second_acc_input)
        ErrorRaising.validate_two_inputs(input_val, first_acc_input, second_acc_input)
        if input_val == first_acc_input:
            return 1
        return 2



    @staticmethod
    def read_player_data(file_name: str) -> list[Player]:
        """ Reads the player data from the CSV file and 
            creates and returns a list of Player objects. """
        with open(os.path.join(Utility.ABS_PATH, file_name), "r",
                  newline="", encoding="utf-8") as players:
            players_csv = csv.reader(players)
            players_data = list(row for row in players_csv)
            header_info = players_data.pop(0)
            list_of_players = []
            for row in players_data:
                player = Player(row, header_info)
                list_of_players.append(player)
            return list_of_players
    @staticmethod
    def search_first_nick_name(player_list: list[Player], guess_name: str):
        """ Return players whose first name or nickname matches the guess name. """
        return [player for player in player_list
                if guess_name.split()[0].lower() in
                (player.player_dict['name'].split()[0].lower(), 
                 player.player_dict['nickname'].lower())]

    @staticmethod
    def search_last_name(player_list: list[Player], guess_name: str):
        """ Return players whose last name matches the guess name. """
        print(player_list[0].player_dict['name'].split()[1].lower())
        print(guess_name.split()[0].lower())
        return [player for player in player_list
                if guess_name.split()[0].lower() == player.player_dict['name'].split()[1].lower()]


def input_checker(input_msg, des_type, reject_msg, console):
    input_not_given = True
    while input_not_given:
        input_val = console.input(input_msg).strip()
        if des_type == str and all(char.isalpha() or char.isspace() for char in input_val):
            return input_val
        elif des_type == int and all(char.isdigit for char in input_val):
            return input_val
        elif des_type == bool and (input_val.capitalize() == "True" or input_val.capitalize() == "False"):
            return input_val.capitalize()
        else:
            console.print(reject_msg)


def two_input_checker(input_msg, reject_msg, acc_input_A, acc_input_B, console):
    input_not_given = True
    while input_not_given:
        input_val = "".join(
            filter(lambda x: x != " ", list(console.input(input_msg))))
        if input_val.capitalize() == acc_input_A:
            return 1
        elif input_val.capitalize() == acc_input_B:
            return 2
        else:
            console.print(reject_msg)


def make_guess(player_data, random_player, tries, guessed_players, console):
    guess_not_made = True
    while guess_not_made:
        guess_name = input_checker(
            "Enter the name/nickname of the character you wish to guess: ", str,
            "The name/nickname can only contain letters", console)
        matches = [player for player in player_data.player_obj_list if player.player_dict["name"].split(" ")[0] == guess_name.split(" ")[0]
                   or player.player_dict["nickname"] == guess_name.split(" ")[0]]
        if len(matches) == 0:
            console.print(
                f"""The name/nickname you entered (\"{guess_name}\") was not found within the system.
                    \n""", style="warning")
        elif len(matches) == 1:
            if matches[0] in guessed_players:
                console.print(
                    f"""You have already guessed (\"{matches[0]}\"). Please guess another.
                    \n""", style="warning")
            else:
                correct_guess, styled_print = player_data.comparison_result(
                    random_player, matches[0])
                guessed_players.append(matches[0])
                tries += 1
                return correct_guess, styled_print, tries

        else:
            if guess_name.split(" ") > 1:
                new_matches = [player for player in matches if player["name"].split(" ")[
                    1] == guess_name.split(" ")[1]]
            else:
                console.print(
                    f"The surname you have entered ({guess_name}) matches too many within the system", style="warning")
                need_given_name = True
                while need_given_name:
                    console.print(
                        "The names within the system that match the given surname are:")
                    for player in matches:
                        console.print(player)
                    guess_given_name = input_checker(
                        "Enter the given name of the character you wish to guess: ", str,
                        "The given name can only contain letters", console)
                    new_matches = [
                        player for player in matches if player["name"].split(" ")[
                            1] == guess_given_name]
                    if len(new_matches) == 0:
                        console.print(f"""The given name you entered (\"{guess_given_name}\") does not match a name.
                        \nPlease refer to the names within the system that match the given surname.\n""", style="warning")
                    else:
                        if matches[0] in guessed_players:
                            console.print(f"""You have already guessed (\"{matches[0]}\"). Please guess another.
                            \n""", style="warning")
                        else:
                            correct_guess = player_data.comparison_result(
                                random_player, matches[0])
                            guessed_players.append(matches[0])
                            tries += 1
                            return correct_guess, tries


def check_players(player_data, guessed_players, console):
    check_not_done = True
    while check_not_done:
        check_letter = input_checker(
            "Enter the letter you wish to find character matches for: ", str,
            "This input should only contain letters.", console)
        if len(check_letter) > 1:
            console.print("You should only enter 1 letter\n", style="warning")
            continue
        matches = [player for player in player_data.player_obj_list if (player.player_dict["name"][0] == check_letter.lower()
                   or player.player_dict["nickname"][0] == check_letter.lower()) and player not in guessed_players]
        if len(matches) == 0:
            console.print(
                f"""No player names/nicknames that have not been guessed begin with the letter: (\"{check_letter.upper()}\").
                    \n""", style="warning")
        else:
            styled_players = []
            for player in matches:
                styled_players.append(f"[white on #666666]{player}")
            return styled_players, check_letter


def refresh_page(console, headline):
    console.clear()
    console.rule(f"[bold rgb(255,165,0)]:zap: {headline} :zap:[/]\n")


def show_guesses(guess_results, console):
    console.print(guess_results[0], justify="left")
    for guess in reversed(guess_results[1:]):
        console.print(guess, justify="left")


def show_checks(check_results, check_letter, console):
    console.print(
        f"\nThe characters that have not been guessed beginning with {check_letter.upper()} are:", justify="center")
    for result in check_results:
        console.print(result, justify="center")
