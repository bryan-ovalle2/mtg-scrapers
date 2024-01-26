# MTG Scrapers

### Overview
Here are just a couple of python scripts I use to compile data on cards to help me brew commander decks. I primarily work in Python and SQL so this just works for me.
These scripts are meant to be run locally in an IDE.

#### Archidekt Deck Scraper
Creates a csv file of your deck from Archidekt.

#### EDH Rec Scraper
This quickly pulls all cards from edhrec for a given commander.

#### Scryfall to MTG
The meat and potatoes is in the gather_scryfall_oracle_cards.py script. This will allow you to maintain a local MySQL database of distinct cards. I don't really care about
different versions of cards until _after_ I'm done brewing. This script will do the initial load of cards, as well as update your database with new cards on every run.
