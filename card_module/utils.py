from typing import List
from .enums import CardSuit, CardRank
from .card import Card
import itertools

def generate_deck() -> List[Card]:
    """ generate a standard 52-card deck """
    suit_names = CardSuit._member_names_
    rank_names = CardRank._member_names_
    card_list = list(itertools.product(suit_names, rank_names))
    deck = [Card(CardSuit[suit], CardRank[rank]) for suit, rank in card_list]
    return deck

def max_card(*args: Card) -> Card:
    """ accepts a number of cards and returns the highest card """
    return max(args)

def cards_stats(*args: Card, **kwargs: int) -> dict[str, List[Card] | int]:
    """ accepts a number of cards and return statistics """
    response: dict[str, List[Card] | int] = {}
    sorted_card_list = sorted(list(args))

    if kwargs["len"]:
        response["len"] = len(args)
    if kwargs["max"]:
        list_size = len(sorted_card_list)
        response["max"] = sorted_card_list[list_size - kwargs["max"]:list_size][::-1]
    if kwargs["min"]:
        response["min"] = sorted_card_list[0:kwargs["min"]]
    return response
