from typing import List
from .enums import CardSuit, CardRank
from .card import Card
import itertools
from .errors import DeckCheatingError

def generate_deck() -> List[Card]:
    """ generate a standard 52-card deck """
    suits = CardSuit._member_names_
    ranks = CardRank._member_names_
    card_list = list(itertools.product(suits, ranks))
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

def fair_deck(func):
    """ a decorator fn that prevent the deck from containig 2 identical cards"""
    def wrapper(self, *args, **kwargs):
        cards_obj = {}
        card_list = self._cards
        if func.__name__ == "add_card":
            card_list.append(*args)
        for item in card_list:
            if item in cards_obj:
                raise DeckCheatingError("the deck has duplicity of cards")
            cards_obj[item] = 1
        return func(self, *args, **kwargs)
    return wrapper