from enum import Enum

class CardSuit(Enum):
    """ An Enum that represent card suit in a standard 52-card deck """
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

class CardRank(Enum):
    """ An Enum that represent card rank in a standard 52-card deck """
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14