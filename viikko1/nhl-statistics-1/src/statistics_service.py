from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, player_reader):
        self._players = player_reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=SortBy.POINTS):
        # Define a function to get the sorting key based on the sort criteria
        if sort_by == SortBy.GOALS:
            sort_key = lambda player: player.goals
        elif sort_by == SortBy.ASSISTS:
            sort_key = lambda player: player.assists
        else:  # Default to sorting by points
            sort_key = lambda player: player.points

        sorted_players = sorted(
            self._players,
            key=sort_key,
            reverse=True  # This ensures highest values come first
        )

        return sorted_players[:how_many]  # Return only the top `how_many` players
