from statistics_service import StatisticsService, SortBy
from player_reader import PlayerReader


def main():
    stats = StatisticsService(
        PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt")
    )

    print("Top point getters:")
    for player in stats.top(10, SortBy.POINTS):
        print(player)

    for player in stats.top(10):
        print(player)

    print("Top goal scorers:")
    for player in stats.top(10, SortBy.GOALS):
        print(player)

    print("Top by assists:")
    for player in stats.top(10, SortBy.ASSISTS):
        print(player)

if __name__ == "__main__":
    main()
