class Player:
    def __init__(self, player_data, header_info):
        self.player_dict = {}
        for i in range(len(header_info)):
            self.player_dict[header_info[i]] = player_data[i]
            exec(f"self.{header_info[i]} = player_data[i]")
