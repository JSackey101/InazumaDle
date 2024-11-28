class Player:
    def __init__(self, player_data, header_info):
        self.player_dict = {}
        for i in range(len(header_info)):
            self.player_dict[header_info[i]] = player_data[i]
            # exec(f"self.{header_info[i]} = player_data[i]")

    def __str__(self):
        return f"{self.player_dict['nickname'].title()} ({self.player_dict['name'].split(' ')[0].title()} {self.player_dict['name'].split(' ')[1].title()})"

    def compare_players(self, other_player):
        return map(lambda a, b: a == b, self.player_dict.values(), other_player.player_dict.values())


class PlayerDatabase:
    def __init__(self, player_obj_list):
        self.player_obj_list = player_obj_list

    def print_players(self, first_letter):
        print("")
        for player in self.player_obj_list:
            if player.player_dict["nickname"][0] == first_letter.lower() or player.player_dict["name"][0] == first_letter.lower():
                print(player)
        print("")
