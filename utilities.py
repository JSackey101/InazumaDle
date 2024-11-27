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
