# printer.py

from rich.console import Console
from rich.table import Table
from player import Player

class PlayerPrinter:
    def __init__(self):
        self.console = Console()  # Rich Console -olio, joka huolehtii tulostuksesta

    def print_top_scorers(self, players, nationality, season):
        # Luo taulukko ja määritä sarakkeet
        table = Table(title=f"Top Scorers ({nationality} players) - {season}")

        table.add_column("Nimi", justify="left", style="cyan", no_wrap=True)
        table.add_column("Joukkue", justify="center", style="magenta")
        table.add_column("Maalit", justify="right", style="green")
        table.add_column("Syötöt", justify="right", style="yellow")
        table.add_column("Pisteet", justify="right", style="bold white")

        # Lisää pelaajat taulukkoon
        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

        # Tulostetaan taulukko Richin avulla
        self.console.print(table)
