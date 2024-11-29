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
        input_val = "".join(filter(lambda x: x != " ", list(input(input_msg))))
        if des_type == str and input_val.isalpha() == True:
            return input_val
        elif des_type == int and input_val.isdigit() == True:
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
