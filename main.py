from players import Player, PlayerDatabase
from utilities import read_player_data, input_checker, two_input_checker, make_guess
import random


# print(list(player_data.player_obj_list[0].compare_players(
#   player_data.player_obj_list[1])))
# player_data.print_players("s")

def check_players(player_data, guessed_players):
    check_not_done = True
    while check_not_done:
        check_letter = input_checker(
            "Enter the letter you wish to find character matches for: ", str,
            "This input should only contain letters.")
        if len(check_letter) > 1:
            print("You should only enter 1 letter\n")
            continue
        matches = [player for player in player_data.player_obj_list if (player.player_dict["name"][0] == check_letter.lower()
                   or player.player_dict["nickname"][0] == check_letter.lower()) and player not in guessed_players]
        if len(matches) == 0:
            print(
                f"""No player names/nicknames that have not been guessed begin with the letter: (\"{check_letter.upper()}\").
                    \n""")
        else:
            print(
                f"\nThe characters that have not been guessed beginning with {check_letter.upper()} are:")
            for player in matches:
                print(player)
            check_not_done = False


if __name__ == "__main__":
    player_data = PlayerDatabase(read_player_data("data.csv"))
    random_player = player_data.player_obj_list[random.randint(
        0, player_data.player_count - 1)]
    tries = 0
    guessed_players = []
    prog_start = True
    while prog_start:
        prompt = two_input_checker("""\nWhat would you like to do?
\nType "Guess" to make a guess.
\nType "Check" to see a list of characters beginning with a specific letter that have not been guessed already.
\nEnter here: """,
                                   """\nYou must type either "Guess" or "Check".""", "Guess", "Check")
        if prompt == 1:
            correct_guess, tries = make_guess(
                player_data, random_player, tries, guessed_players)
            if correct_guess:
                print(f"""Victory!

You guessed {random_player}

Number of tries: {tries}""")
                break

        else:
            check_players(player_data, guessed_players)
