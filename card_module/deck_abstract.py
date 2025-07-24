from abc import ABC, abstractmethod
from typing import List, Iterator
from .card import Card

class DeckAbstract(ABC):
    """ 
    a class that is an abstraction of a deck of cards.

    attributes:
        _cards (List[Card]): a deck of cards.
    """

    @property
    @abstractmethod
    def cards(self) -> List[Card]:
        """ return a copy of the deck """
        pass

    @abstractmethod
    def shuffle(self) -> None:
        """ shuffle the crads in the deck """
        pass

    @abstractmethod
    def draw(self) -> Card | None:
        """ remove and return a card from the beginning of the deck. if deck is empty returns None """
        pass

    @abstractmethod
    def add_card(self, card: Card) -> None:
        """ adds a card to the end of the deck. """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """ returns the amount of cards in the deck """
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> Card:
        """ return a card by its index in the deck """
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[Card]:
        """ make the deck iterable """
        pass