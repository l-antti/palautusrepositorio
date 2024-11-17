# player_reader.py

import requests
from player import Player

class PlayerReader:
    def __init__(self, season, url_template="https://studies.cs.helsinki.fi/nhlstats/{}/players"):
        self.url = url_template.format(season)  # URL kaudelle

    def get_players(self):
        # Haetaan pelaajatiedot ja luodaan Player-olioita
        response = requests.get(self.url).json()
        players = [Player(player_dict) for player_dict in response]
        return players
