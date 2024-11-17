# player.py

class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']  # Pelaajan nimi
        self.team = player_dict['team']  # Joukkueen nimi (merkkijono)
        self.nationality = player_dict['nationality']  # Kansallisuus
        self.goals = player_dict['goals']  # Maalit
        self.assists = player_dict['assists']  # Syötöt

        #laske pisteet
        self.points = self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team:3} {self.goals:2} + {self.assists:2} = {self.points:3}"
