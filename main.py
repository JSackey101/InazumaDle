from players import Player, PlayerDatabase
from utilities import read_player_data, input_checker, two_input_checker
import random


# print(list(player_data.player_obj_list[0].compare_players(
#   player_data.player_obj_list[1])))
# player_data.print_players("s")

def make_guess(player_data, random_player):
    guess_not_made = True
    while guess_not_made:
        guess_name = input_checker(
            "Enter the name/nickname of the character you wish to guess: ", str,
            "The name/nickname can only contain letters")
        matches = [player for player in player_data.player_obj_list if player.player_dict["name"].split(" ")[0] == guess_name.split(" ")[0]
                   or player.player_dict["nickname"] == guess_name.split(" ")[0]]
        if len(matches) == 0:
            print(
                f"""The name/nickname you entered (\"{guess_name}\") was not found within the system.
                    \n""")
        elif len(matches) == 1:
            correct_guess = player_data.comparison_result(
                random_player, matches[0])
            return correct_guess

        else:
            if guess_name.split(" ") > 1:
                new_matches = [player for player in matches if player["name"].split(" ")[
                    1] == guess_name.split(" ")[1]]
            else:
                print(
                    f"The surname you have entered ({guess_name}) matches too many within the system")
                need_given_name = True
                while need_given_name:
                    print(
                        "The names within the system that match the given surname are:")
                    for player in matches:
                        print(player)
                    guess_given_name = input_checker(
                        "Enter the given name of the character you wish to guess: ", str,
                        "The given name can only contain letters")
                    new_matches = [
                        player for player in matches if player["name"].split(" ")[
                            1] == guess_given_name]
                    if len(new_matches) == 0:
                        print(f"""The given name you entered (\"{guess_given_name}\") does not match a name.
                        \nPlease refer to the names within the system that match the given surname.\n""")
                    else:
                        correct_guess = player_data.comparison_result(
                            random_player, matches[0])
                        return correct_guess


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
            correct_guess = make_guess(player_data, random_player)
        else:
            pass
