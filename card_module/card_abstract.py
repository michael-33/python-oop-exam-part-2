from abc import ABC, abstractmethod
from .enums import CardSuit, CardRank

class CardAbstract(ABC):
    """ 
    abstraction of a Card class.

    attributes:
        _suit (CardSuit): the card's suit.
        _rank (CardRank): the card's rank.
    """

    @abstractmethod
    def get_display_name(self) -> str:
        """ returns the card suit and rank """
        pass

    @property
    @abstractmethod
    def suit(self) -> CardSuit:
        """ return attribute card suit """
        pass

    @property
    @abstractmethod
    def rank(self) -> CardRank:
        """ return attribute card rank """
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """ perform comparison between two Card instances to determine if they are equel"""
        pass

    @abstractmethod
    def __lt__(self, other: object) -> bool:
        """ perform comparison between two Card instances to determine if the first param is smaller than the second one"""
        pass

    @abstractmethod
    def __gt__(self, other: object) -> bool:
        """ perform comparison between two Card instances to determine if the first param is bigger than the second one"""
        pass

    @abstractmethod
    def __hash__(self) -> int:
        """ make the object hashable by creatin a hash value based on suit and rank of the card """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """ return a textual representation of the card """
        pass
    
    @abstractmethod
    def __repr__(self) -> str:
        """ return a printable representation of the card object """
        pass