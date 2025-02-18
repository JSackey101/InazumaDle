import csv
from players import Player


def read_player_data(filepath):
    with open(filepath, "r", newline="", encoding="utf-8") as players:
        players_csv = csv.reader(players)
        players_data = [row for row in players_csv]
        header_info = players_data.pop(0)
        list_of_players = []
        for row in players_data:
            player = Player(row, header_info)
            list_of_players.append(player)
        return list_of_players


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
