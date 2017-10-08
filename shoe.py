from deck import Deck
class Shoe:

    def __init__(self):
        self.numberOfDecks = 6
        self.cards = []

        for x in range(0, self.numberOfDecks):
            deck = Deck()
            while len(deck.cards) != 0:
                self.cards.append(deck.cards.pop())

    def printShoe(self):
        i = 0
        for card in self.cards:
            print(i, card.getFriendlyName(), card.cardType)
            i += 1
