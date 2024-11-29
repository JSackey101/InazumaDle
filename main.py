from players import Player, PlayerDatabase
from utilities import read_player_data
import random


# print(list(player_data.player_obj_list[0].compare_players(
#   player_data.player_obj_list[1])))
# player_data.print_players("s")

if __name__ == "__main__":
    player_data = PlayerDatabase(read_player_data("data.csv"))
    random_player = player_data.player_obj_list[random.randint(
        0, player_data.player_count)]
    print(random_player)
