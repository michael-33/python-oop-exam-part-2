from .deck_abstract import DeckAbstract
from .card import Card
from typing import List, Iterator
from .utils import generate_deck, fair_deck
import random

class Deck(DeckAbstract):
    """
    a class to represent a deck of cards. inherit from DeckAbstract class.

    attributes:
        _cards (List[Card]): a deck of cards.
    """

    def __init__(self, shuffle: bool = True) -> None:
        """
        constructs all the necessary attributes for the deck object.

        variables:
            cards (List[Card]): a deck of cards, auto-generated.
        """
        cards = generate_deck()
        if shuffle:
            random.shuffle(cards)
        self._cards = cards

    @property
    @fair_deck
    def cards(self) -> List[Card]:
        """ return a copy of the deck """
        return self._cards.copy()
    
    def shuffle(self) -> None:
        """ shuffle the crads in the deck """
        random.shuffle(self._cards)

    def draw(self) -> Card | None:
        """ remove and return a card from the beginning of the deck. if deck is empty returns None """
        if len(self._cards) == 0:
            return None
        return self._cards.pop(0)
    
    @fair_deck
    def add_card(self, card: Card) -> None:
        """ add a card to end the deck. """
        self._cards.append(card)

    def __len__(self) -> int:
        """ returns the amount of cards in the deck """
        return len(self._cards)
    
    def __getitem__(self, index: int) -> Card:
        """ return a card by its index in the deck """
        if index > len(self._cards) - 1:
            raise IndexError(f"Index out of range.")
        return self._cards[index]
    
    def __iter__(self) -> Iterator[Card]:
        """ make the deck iterable """
        for card in self._cards:
            yield card

    def __str__(self) -> str:
        """ return a textual representation of the card """
        return self._cards.__str__()
