import requests

from player import Player


def print_players(players: list):
    for player in players:
        print(
            f"{player.name:20} {player.team:15} {player.goals:2} + {player.assists:2} = {player.points:2}"
        )


def filter_by_nationality(nationality_code: str, players: list) -> list:
    return [p for p in players if p.nationality == nationality_code]


def sort_by_points(players: list):
    return sorted(players, key=lambda p: p.points, reverse=True)


class PlayerReader:
    def __init__(self, url: str):
        self.url = url
        self.players = self.get_players()  # ← save the list

    def get_players(self):
        response = requests.get(self.url).json()
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players


class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality_code: str):
        filtered = filter_by_nationality(nationality_code, self.players)
        sorted_players = sort_by_points(filtered)
        return sorted_players


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_scorers_by_nationality("FIN")

    print_players(players)


if __name__ == "__main__":
    main()
