import requests
import json
import pandas as pd
import re


def string_to_snake_case(input_string):
    slug = re.sub(r'[^a-zA-Z0-9 ]', '', input_string).replace(' ', '_').lower()
    return slug


def get_archidekt_deck(deck_id):
    archidekt_deck_api_url = f"https://archidekt.com/api/decks/{deck_id}/"
    data = requests.get(archidekt_deck_api_url)
    deck_json = json.loads(data.text)
    deck_name = deck_json['name']
    cards = deck_json['cards']

    deck_list = []
    for i, card in enumerate(cards):
        oracle_card = card['card']['oracleCard']

        deck_list.append({
            "uuid": card['card']['uid'],
            "name": oracle_card['name'],
            "cmc": oracle_card['cmc'],
            "colors": ', '.join(oracle_card['colors']),
            "manaCost": oracle_card['manaCost'],
            "power_toughness": "N/A" if oracle_card['types'] == "Land" else f"{oracle_card['power']}/{oracle_card['toughness']}",
            "types": ', '.join(oracle_card['types']),
            "mana_production": oracle_card['manaProduction'],
            "tcg_price": 0 if card['card']['prices']['tcg'] is None else card['card']['prices']['tcg'],
            "quantity": card['quantity']
        })

    deck = pd.DataFrame(deck_list)
    deck.to_csv(string_to_snake_case(deck_name) + "_archidekt_deck" + ".csv", index=False)


if __name__ == "__main__":
    get_archidekt_deck(6340667)
