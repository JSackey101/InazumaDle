from players import PlayerDatabase
from utilities import read_player_data, two_input_checker, make_guess, check_players, refresh_page
import random
from rich.console import Console  # type: ignore
from rich.theme import Theme  # type: ignore
import time


def show_guesses(guess_results):
    for guess in guess_results:
        console.print(guess, justify="left")


if __name__ == "__main__":
    console = Console(width=120, theme=Theme({"warning": "red on yellow"}))
    refresh_page(console, "InazumaDle")
    player_data = PlayerDatabase(read_player_data("data.csv"))
    random_player = player_data.player_obj_list[random.randint(
        0, player_data.player_count - 1)]
    tries = 0
    guessed_players = []
    guess_results = [""]
    for heading in list(random_player.player_dict.keys()):
        guess_results[0] += (
            f"[bold white on #666666]{heading.title()}") + " "*(20-len(heading))
    # I wish to refresh the page then display the guesses made already
    prog_start = True
    while prog_start:
        refresh_page(console, "InazumaDle")
        show_guesses(guess_results)
        prompt = two_input_checker("""\nWhat would you like to do?
\nType "Guess" to make a guess.
\nType "Check" to see a list of characters beginning with a specific letter that have not been guessed already.
\nEnter here: """,
                                   """\nYou must type either "Guess" or "Check".""", "Guess", "Check", console)
        if prompt == 1:
            correct_guess, styled_print, tries = make_guess(
                player_data, random_player, tries, guessed_players, console)
            guess_results.append(styled_print)
            show_guesses(guess_results)
            if correct_guess:
                console.print(f"""Victory!

You guessed {random_player}

Number of tries: {tries}""")
                break

        else:
            check_players(player_data, guessed_players, console)
