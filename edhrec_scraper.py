import requests
import json
import pandas as pd
import re
import pprint

# base url setup
edhrec_base_url = "https://json.edhrec.com/pages/commanders/%s.json"


def string_to_slug(input_string):
    slug = re.sub(r'[^a-zA-Z0-9 ]', '', input_string).replace(' ', '-').lower()
    return slug


def string_to_snake_case(input_string):
    slug = re.sub(r'[^a-zA-Z0-9 ]', '', input_string).replace(' ', '_').lower()
    return slug

# for testing json
# def get_edhrec_json(commander_name):
#     data = requests.get(edhrec_base_url % string_to_slug(commander_name))
#     json_data = json.loads(data.text)
#     return json_data


def get_recs(commander_name):
    data = requests.get(edhrec_base_url % string_to_slug(commander_name))
    json_data = json.loads(data.text)
    cardviews = json_data["container"]["json_dict"]["cardlists"]
    cardview_length = len(cardviews)

    rec_data = []
    for rec_group in range(cardview_length):
        rec_type = cardviews[rec_group]["header"]
        rec_cards = cardviews[rec_group]["cardviews"]

        for card in rec_cards:
            rec_data.append(
                {
                    "card_type": rec_type,
                    "card_name": card["name"],
                    "synergy_score": card["synergy"] * 100,
                    "inclusion": card["inclusion"],
                    "url": "https://edhrec.com/" + card["url"]

                }
            )
    card_recommendations = pd.DataFrame(rec_data)
    card_recommendations.to_csv(string_to_snake_case(commander_name) + "_edhrecs" + ".csv", index=False)


if __name__ == "__main__":
    # get recs
    get_recs("the locust god")