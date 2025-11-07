import requests

from player import Player


def print_players(list: list):
    for player in list:
        print(
            f"{player.name:20} {player.team:15} {player.goals:2} + {player.assists:2} = {player.points:2}"
        )


def filter_by_nationality(nationality_code: str, list: list) -> list:
    res = []
    for player in list:
        if player.nationality == nationality_code:
            res.append(player)

    return res


def sort_by_points(players: list):
    return sorted(players, key=lambda p: p.points, reverse=True)


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        print(player_dict)
        player = Player(player_dict)
        players.append(player)

    filtered_list = filter_by_nationality("FIN", players)
    sorted_list = sort_by_points(filtered_list)
    print_players(sorted_list)


main()
