from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan, Or, QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query1 = QueryBuilder()
    query2 = QueryBuilder()
    

    matcher = query1.one_of(
        query1.plays_in("PHI")
            .has_at_least(10, "assists")
            .has_fewer_than(10, "goals")
            .build(),

        query2.plays_in("EDM")
            .has_at_least(50, "points")
            .build()
    ).build()

    for player in stats.matches(matcher):
        print(player)


    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))


if __name__ == "__main__":
    main()
