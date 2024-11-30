from players import Player, PlayerDatabase
from utilities import read_player_data, input_checker, two_input_checker
import random


# print(list(player_data.player_obj_list[0].compare_players(
#   player_data.player_obj_list[1])))
# player_data.print_players("s")

if __name__ == "__main__":
    prog_start = True
    while prog_start:
        player_data = PlayerDatabase(read_player_data("data.csv"))
        random_player = player_data.player_obj_list[random.randint(
            0, player_data.player_count - 1)]
        tries = 0
        prompt = two_input_checker("""\nWhat would you like to do?
\nType "Guess" to make a guess.
\nType "Check" to see a list of characters beginning with a specific letter.
\nEnter here: """,
                                   """\nYou must type either "Guess" or "Check".""", "Guess", "Check")
        if prompt == 1:
            pass
        else:
            pass
