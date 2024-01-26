import requests
import json
from database_config import create_engine_instance
from sqlalchemy.orm import sessionmaker
from mtg_card_db_models import Base, OracleCard
from alive_progress import alive_bar

# get bulk data download urls
scryfall_bulk_data_url = "https://api.scryfall.com/bulk-data"
scryfall_bulk_urls_data = requests.get(scryfall_bulk_data_url)
scryfall_bulk_url_json_data = json.loads(scryfall_bulk_urls_data.text)

#  get url specifically for oracle cards.
'''
 From Scryfall:
 description: A JSON file containing one Scryfall card object
            for each Oracle ID on Scryfall. The chosen sets for
            the cards are an attempt to return the most up-to-date
            recognizable version of the card.
'''


def get_oracle_cards_url():
    oracle_cards_download_url = ""
    for bulk_uri in scryfall_bulk_url_json_data['data']:
        if bulk_uri['name'] == 'Oracle Cards':
            oracle_cards_download_url = bulk_uri['download_uri']
        else:
            continue
        print(f"Using {oracle_cards_download_url} as bulk download URL")
    return oracle_cards_download_url


# all card data
card_data = requests.get(get_oracle_cards_url())
card_data_json = json.loads(card_data.text)


def get_complete_scryfall_ids(card_type):
    scryfall_card_ids = []
    for card in card_data_json:
        if card['layout'] == card_type:
            scryfall_card_ids.append(card['id'])
    return scryfall_card_ids


# get the data I want for each card.
def stage_normal_card_data():
    cards = []
    for stage_card in card_data_json:
        if stage_card['layout'] == "normal" and stage_card['id'] in new_scryfall_ids:
            cards.append(
                {
                    'scryfall_id': stage_card['id'],
                    'oracle_id': stage_card['oracle_id'],
                    'name': stage_card['name'],
                    'power': stage_card.get('power') if stage_card.get('power', '') != "" else None,
                    'toughness': stage_card.get('toughness') if stage_card.get('toughness', '') != "" else None,
                    'released_at': stage_card['released_at'],
                    'mana_cost': stage_card['mana_cost'] if stage_card['mana_cost'] != "" else None,
                    'cmc': stage_card['cmc'],
                    'type_line': stage_card['type_line'],
                    'colors': ', '.join(stage_card.get("colors", [])) if "colors" in stage_card else None,
                    'color_identity': ', '.join(
                        stage_card.get("color_identity", [])) if "color_identity" in stage_card else None,
                    'oracle_text': stage_card['oracle_text'],
                    'keywords': ', '.join(stage_card.get("keywords", [])) if "keywords" in stage_card else None
                }
            )
    return cards


# TODO: same function but for tokens, then populate token table


if __name__ == "__main__":
    # replace these arguments with your db info
    engine = create_engine_instance('root', '', 'localhost', 'mtg')
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)

    try:
        with Session() as session:
            existing_scryfall_ids = session.query(OracleCard.scryfall_id).all()
            cleaned_existing_ids = [i[0] for i in existing_scryfall_ids]
            new_scryfall_ids = [value for value in get_complete_scryfall_ids('normal') if value not in cleaned_existing_ids]

            cards_to_insert = []
            total_iterations = len(new_scryfall_ids)
            with alive_bar(total_iterations, force_tty=True) as bar:
                for i, card_data in enumerate(stage_normal_card_data()):
                    cards_to_insert.append(card_data)
                    bar()

        if cards_to_insert:
            staged_cards_len = len(cards_to_insert)
            session.add_all([OracleCard(**card) for card in cards_to_insert])
            session.commit()
            print(f"{staged_cards_len} cards inserted successfully")
        else:
            print("No new records to insert.")

    except Exception as e:
        print(f"Error: {e}")
