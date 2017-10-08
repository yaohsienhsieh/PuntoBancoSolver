from enum import Enum

class CardType(Enum):
    HEARTS = 1
    SPADES = 2
    DIAMONDS = 3
    CLUBS = 4

class Card:

    def __init__(self, cardType, value):
        self.cardType = cardType
        self.value = value
        self.worth = value
        if self.value == 10 or self.value == 11 or self.value == 12 or self.value == 13:
            self.worth = 0

    def getFriendlyName(self):
        if self.value == 1:
            return "Ace of " + self.getTypeName() + "(" + str(self.worth) + ")"
        if self.value == 11:
            return "Jack of " + self.getTypeName() + "(" + str(self.worth) + ")"
        if self.value == 12:
            return "Queen of " + self.getTypeName() + "(" + str(self.worth) + ")"
        if self.value == 13:
            return "King of " + self.getTypeName() + "(" + str(self.worth) + ")"
        else:
            return str(self.value) + " of " + self.getTypeName()

    def getTypeName(self):
        if self.cardType == CardType.HEARTS:
            return "Hearts"
        if self.cardType == CardType.SPADES:
            return "Spades"
        if self.cardType == CardType.DIAMONDS:
            return "Diamonds"
        if self.cardType == CardType.CLUBS:
            return "Clubs"
