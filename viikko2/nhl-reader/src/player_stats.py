# player_stats.py

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader  # PlayerReader-olio, jonka avulla pelaajat haetaan

    def top_scorers_by_nationality(self, nationality):
        # Haetaan pelaajat ja suodatetaan kansalaisuuden mukaan
        players = [player for player in self.reader.get_players() if player.nationality == nationality]

        # Järjestetään pelaajat pistemäärän mukaan laskevaan järjestykseen
        sorted_players = sorted(players, key=lambda p: p.points, reverse=True)

        return sorted_players
