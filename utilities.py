import csv


def read_player_data(filepath):
    with open(filepath, "r", newline="") as players:
        players_csv = csv.reader(players)
        players_data = [row for row in players_csv]
        header_info = players_data[0]
        players_data.remove(header_info)
        list_of_players = []
        for row in players_data:
            char_dict = {}
            for i in range(len(header_info)):
                char_dict[header_info[i]] = row[i]
            list_of_players.append(char_dict)


read_player_data("data.csv")
