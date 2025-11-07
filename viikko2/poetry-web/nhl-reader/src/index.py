import requests

from player import Player


def print_players(list: list):
    for player in list:
        print(
            f"{player.name} team {player.team} goals {player.goals} assists {player.assists}"
        )


def filter_by_nationality(nationality_code: str, list: list) -> list:
    res = []
    for player in list:
        if player.nationality == nationality_code:
            res.append(player)

    return res


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
    print_players(filtered_list)


main()
