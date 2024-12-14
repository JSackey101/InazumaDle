import csv
from players import Player


def read_player_data(filepath):
    with open(filepath, "r", newline="") as players:
        players_csv = csv.reader(players)
        players_data = [row for row in players_csv]
        header_info = players_data[0]
        players_data.remove(header_info)
        list_of_players = []
        for row in players_data:
            player = Player(row, header_info)
            list_of_players.append(player)
        return list_of_players


def input_checker(input_msg, des_type, reject_msg):
    input_not_given = True
    while input_not_given:
        # "".join(filter(lambda x: x != " ", list(input(input_msg))))
        input_val = input(input_msg).strip()
        if des_type == str and all(char.isalpha() or char.isspace() for char in input_val):
            return input_val
        elif des_type == int and all(char.isdigit for char in input_val):
            return input_val
        elif des_type == bool and (input_val.capitalize() == "True" or input_val.capitalize() == "False"):
            return input_val.capitalize()
        else:
            print(reject_msg)


def two_input_checker(input_msg, reject_msg, acc_input_A, acc_input_B):
    input_not_given = True
    while input_not_given:
        input_val = "".join(filter(lambda x: x != " ", list(input(input_msg))))
        if input_val.capitalize() == acc_input_A:
            return 1
        elif input_val.capitalize() == acc_input_B:
            return 2
        else:
            print(reject_msg)


def make_guess(player_data, random_player, tries, guessed_players):
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
            if matches[0] in guessed_players:
                print(
                    f"""You have already guessed (\"{matches[0]}\"). Please guess another.
                    \n""")
            else:
                correct_guess = player_data.comparison_result(
                    random_player, matches[0])
                guessed_players.append(matches[0])
                tries += 1
                return correct_guess, tries

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
                        if matches[0] in guessed_players:
                            print(f"""You have already guessed (\"{matches[0]}\"). Please guess another.
                            \n""")
                        else:
                            correct_guess = player_data.comparison_result(
                                random_player, matches[0])
                            guessed_players.append(matches[0])
                            tries += 1
                            return correct_guess, tries


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
