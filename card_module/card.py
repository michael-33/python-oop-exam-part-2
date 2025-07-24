from .card_abstract import CardAbstract
from .enums import CardSuit, CardRank

class Card(CardAbstract):
    """
    a class to represent a card. inherit from CardAbstract class.

    attributes:
        _suit (CardSuit): the card's suit.
        _rank (CardRank): the card's rank.
    """

    def __init__(self, suit: CardSuit, rank: CardRank) -> None:
        """
        constructs all the necessary attributes for the card object.

        parameters:
            suit (CardSuit): the card's suit.
            rank (CardRank): the card's rank.
        """
        self._suit = suit
        self._rank = rank

    def get_display_name(self) -> str:
        """ returns the card suit and rank """
        return f"{self.rank.name} of {self.suit.name}"
    
    @property
    def suit(self) -> CardSuit:
        """ return attribute card suit """
        return self._suit
    
    @property
    def rank(self) -> CardRank:
        """ return attribute card rank """
        return self._rank

    def __eq__(self, other: object) -> bool:
        """ perform comparison between two Card instances to determine if they are equel """
        if not isinstance(other, Card):
            raise ValueError("one of the compared object is not a Card")
        return (self._rank.value == other._rank.value and self._suit.value == other._suit.value)
    
    def __lt__(self, other: object) -> bool:
        """ perform comparison between two Card instances to determine if the first param is smaller than the second one """
        if not isinstance(other, Card):
            raise ValueError("one of the compared object is not a Card")
        if (self._rank.value == other._rank.value):
            return self._suit.value < other._suit.value
        return self._rank.value < other._rank.value

    def __gt__(self, other: object) -> bool:
        """ perform comparison between two Card instances to determine if the first param is bigger than the second one """
        if not isinstance(other, Card):
            raise ValueError("one of the compared object is not a Card")
        if (self._rank.value == other._rank.value):
            return self._suit.value > other._suit.value
        return self._rank.value > other._rank.value
    
    def __hash__(self) -> int:
        """ make the object hashable by creatin a hash value based on suit and rank of the card """
        return hash((self._rank, self._suit))
    
    def __str__(self) -> str:
        """ return a textual representation of the card """
        return f"{self._rank.name} of {self._suit.name}"
    
    def __repr__(self) -> str:
        """ return a printable representation of the card object """
        cls_name = self.__class__.__name__
        return f"{cls_name}(rank={self._rank}, suit={self._suit})"