# main.py

from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats
from printer import PlayerPrinter

def main():
    console = Console()

    # Valitaan kausi listasta
    seasons = ["2023-24", "2022-23", "2021-22", "2020-21", "2019-20"]
    console.print("Valitse kausi:")
    for idx, season in enumerate(seasons, 1):
        console.print(f"[{idx}] {season}")

    season_choice = IntPrompt.ask("Syötä numeron mukainen valinta kaudelle", choices=[str(i) for i in range(1, len(seasons) + 1)])

    season = seasons[int(season_choice) - 1]  # Valitaan kausi käyttäjän syötteen perusteella

    # Valitaan kansallisuus listalta
    nationalities = ["FIN", "USA", "CAN", "SWE", "RUS", "CZE", "SVK", "GER", "LAT", "EST"]
    nationality_choice = Prompt.ask("Valitse kansalaisuus", choices=nationalities)

    # Luo PlayerReader ja PlayerStats -oliot
    reader = PlayerReader(season)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality_choice)

    # Tulostetaan pelaajat
    printer = PlayerPrinter()
    printer.print_top_scorers(players, nationality_choice, season)

if __name__ == "__main__":
    main()
