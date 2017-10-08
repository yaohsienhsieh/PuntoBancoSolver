from random import shuffle
from card import Card
from card import CardType

class Deck:

    def __init__(self):
        self.cards = []
        for cardType in CardType:
            for value in range(1, 14):
                card = Card(cardType, value)
                self.cards.append(card)
        shuffle(self.cards)

    def printDeck(self):
        self.i = 0
        for card in self.cards:
            print(i, card.getFriendlyName(), card.cardType)
            i += 1
