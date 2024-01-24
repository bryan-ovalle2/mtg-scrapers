from sqlalchemy import Column, String, Integer, Date, Boolean, Text
from sqlalchemy.orm import declarative_base
from database_config import create_engine_instance

Base = declarative_base()


class OracleCard(Base):
    __tablename__ = "scryfall_cards"

    scryfall_id = Column("scryfall_id", String(255), primary_key=True)
    oracle_id = Column("oracle_id", String(255))
    name = Column("name", String(255))
    power = Column("power", String(255))
    toughness = Column("toughness", String(255))
    released_at = Column("released_at", Date)
    mana_cost = Column("mana_cost", String(255))
    cmc = Column("cmc", Integer)
    type_line = Column("type_line", String(255))
    colors = Column("colors", String(255))
    color_identity = Column("color_identity", String(255))
    oracle_text = Column("oracle_text", Text)
    keywords = Column("keywords", String(255))

    def __init__(self, oracle_id, scryfall_id, name, power, toughness, released_at, mana_cost,
                 cmc, type_line, colors, color_identity, oracle_text, keywords):
        self.oracle_id = oracle_id
        self.scryfall_id = scryfall_id
        self.name = name
        self.power = power
        self.toughness = toughness
        self.released_at = released_at
        self.mana_cost = mana_cost
        self.cmc = cmc
        self.type_line = type_line
        self.colors = colors
        self.color_identity = color_identity
        self.oracle_text = oracle_text
        self.keywords = keywords


class CardImageUrls(Base):
    __tablename__ = "scryfall_image_urls"

    scryfall_id = Column("scryfall_id", String(50), primary_key=True)
    oracle_id = Column("oracle_id", String(50))
    small_image_url = Column("small_image_url", String(150))
    normal_image_url = Column("normal_image_url", String(150))
    large_image_url = Column("large_image_url", String(150))

    def __init__(self, oracle_id, small_image_url, normal_image_url, large_image_url):
        self.oracle_id = oracle_id
        self.small_image_url = small_image_url
        self.normal_image_url = normal_image_url
        self.large_image_url = large_image_url


class CardLegalities(Base):
    __tablename__ = "card_legalities"

    scryfall_id = Column("scryfall_id", String(50), primary_key=True)
    oracle_id = Column("oracle_id", String(50))
    is_legal_in_standard = Column("is_legal_in_standard", Boolean)
    is_legal_in_future = Column("is_legal_in_future", Boolean)
    is_legal_in_historic = Column("is_legal_in_historic", Boolean)
    is_legal_in_timeless = Column("is_legal_in_timeless", Boolean)
    is_legal_in_gladiator = Column("is_legal_in_gladiator", Boolean)
    is_legal_in_pioneer = Column("is_legal_in_pioneer", Boolean)
    is_legal_in_explorer = Column("is_legal_in_explorer", Boolean)
    is_legal_in_modern = Column("is_legal_in_modern", Boolean)
    is_legal_in_legacy = Column("is_legal_in_legacy", Boolean)
    is_legal_in_pauper = Column("is_legal_in_pauper", Boolean)
    is_legal_in_vintage = Column("is_legal_in_vintage", Boolean)
    is_legal_in_penny = Column("is_legal_in_penny", Boolean)
    is_legal_in_commander = Column("is_legal_in_commander", Boolean)
    is_legal_in_oathbreaker = Column("is_legal_in_oathbreaker", Boolean)
    is_legal_in_brawl = Column("is_legal_in_brawl", Boolean)
    is_legal_in_historicbrawl = Column("is_legal_in_historicbrawl", Boolean)
    is_legal_in_alchemy = Column("is_legal_in_alchemy", Boolean)
    is_legal_in_paupercommander = Column("is_legal_in_paupercommander", Boolean)
    is_legal_in_duel = Column("is_legal_in_duel", Boolean)
    is_legal_in_oldschool = Column("is_legal_in_oldschool", Boolean)
    is_legal_in_premodern = Column("is_legal_in_premodern", Boolean)
    is_legal_in_predh = Column("is_legal_in_predh", Boolean)

    def __init__(self, is_legal_in_historic, is_legal_in_timeless, is_legal_in_gladiator, is_legal_in_pioneer,
                 is_legal_in_explorer, is_legal_in_modern, is_legal_in_legacy, is_legal_in_pauper, is_legal_in_vintage,
                 is_legal_in_penny, is_legal_in_commander, is_legal_in_oathbreaker, is_legal_in_brawl,
                 is_legal_in_historicbrawl, is_legal_in_alchemy, is_legal_in_paupercommander, is_legal_in_duel,
                 is_legal_in_oldschool, is_legal_in_premodern, is_legal_in_predh):
        self.is_legal_in_historic = is_legal_in_historic
        self.is_legal_in_timeless = is_legal_in_timeless
        self.is_legal_in_gladiator = is_legal_in_gladiator
        self.is_legal_in_pioneer = is_legal_in_pioneer
        self.is_legal_in_explorer = is_legal_in_explorer
        self.is_legal_in_modern = is_legal_in_modern
        self.is_legal_in_legacy = is_legal_in_legacy
        self.is_legal_in_pauper = is_legal_in_pauper
        self.is_legal_in_vintage = is_legal_in_vintage
        self.is_legal_in_penny = is_legal_in_penny
        self.is_legal_in_commander = is_legal_in_commander
        self.is_legal_in_oathbreaker = is_legal_in_oathbreaker
        self.is_legal_in_brawl = is_legal_in_brawl
        self.is_legal_in_historicbrawl = is_legal_in_historicbrawl
        self.is_legal_in_alchemy = is_legal_in_alchemy
        self.is_legal_in_paupercommander = is_legal_in_paupercommander
        self.is_legal_in_duel = is_legal_in_duel
        self.is_legal_in_oldschool = is_legal_in_oldschool
        self.is_legal_in_premodern = is_legal_in_premodern
        self.is_legal_in_predh = is_legal_in_predh


class TokensForCreatures(Base):
    __tablename__= "tokens_for_creatures"

    scryfall_id = Column("scryfall_id", String(50), primary_key=True)
    parent_scryfall_id = Column("parent_scryfall_id", String(50))
    name = Column("token_name", String(100))
    type_line = Column("type_line", String(60))
    power_toughness = Column("power_toughness", String(5))

