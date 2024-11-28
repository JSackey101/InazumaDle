from players import Player, PlayerDatabase
from utilities import read_player_data

player_data = PlayerDatabase(read_player_data("data.csv"))
print(list(player_data.player_obj_list[0].compare_players(
    player_data.player_obj_list[1])))
player_data.print_players("s")
