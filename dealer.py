from shoe import Shoe
import time

class Dealer:

    def __init__(self):
        self.shoe = Shoe()

    def deal(self):
        self.puntoPoints = 0
        self.bancoPoints = 0
        self.puntoCards = []
        self.bancoCards = []

        # Draw two cards for both
        for i in range(0, 4):
            if i % 2 == 0:
                self.drawCardPunto()
            else:
                self.drawCardBanco()

        self.initialDealCheck()
        self.puntoPass()
        self.puntoThirdCard()
        self.announceScore()

    def drawCardPunto(self):
        self.selectedCard = self.shoe.cards.pop()
        self.puntoCards.append(self.selectedCard)
        self.puntoPoints += self.selectedCard.worth
        self.puntoPoints = self.puntoPoints % 10

    def drawCardBanco(self):
        self.selectedCard = self.shoe.cards.pop()
        self.bancoCards.append(self.selectedCard)
        self.bancoPoints += self.selectedCard.worth
        self.bancoPoints = self.bancoPoints % 10

    def initialDealCheck(self):
        if self.puntoPoints > 7 and self.bancoPoints < 8:
            print("Punto wins")
            return

        if self.bancoPoints > 7 and self.puntoPoints < 8:
            print("Banco wins")
            return

    def puntoPass(self):
        if self.puntoPoints is 6 or self.puntoPoints is 7:
            print("Punto: " + str(self.puntoPoints) + " Punto pass...")

            if self.bancoPoints is 6 or self.bancoPoints is 7:
                print("Banco: " + str(self.bancoPoints) + " Banco pass...")

            if self.bancoPoints < 6:
                print("Banco: " + str(self.bancoPoints) + " Banco gets another card...")
                self.drawCardBanco()

    def puntoThirdCard(self):
        if self.puntoPoints < 6:
            self.drawCardPunto()
            self.selectedCard = self.puntoCards[-1]

            if self.bancoPoints is 6:
                if self.selectedCard.worth is 6 or self.selectedCard.worth is 7:
                    self.drawCardBanco()
                    return
            if self.bancoPoints is 5:
                if self.selectedCard.worth >= 4 or self.selectedCard.worth <= 7:
                    self.drawCardBanco()
                    return
            if self.bancoPoints is 4:
                if self.selectedCard.worth >= 2 or self.selectedCard.worth <= 7:
                    self.drawCardBanco()
                    return
            if self.bancoPoints is 3:
                if self.selectedCard.worth != 8:
                    self.drawCardBanco()
                    return
            if self.bancoPoints < 3:
                self.drawCardBanco()
                return

    def announceScore(self):
        self.card = ""
        while len(self.bancoCards) is not 0:
            self.card = self.card + self.bancoCards.pop().getFriendlyName() + ", "

        self.card = self.card + " || "

        while len(self.puntoCards) is not 0:
            self.card = self.card + self.puntoCards.pop().getFriendlyName() + ", "

        print(self.card)
        if self.puntoPoints > self.bancoPoints:
            print("Punto wins")
        if self.bancoPoints > self.puntoPoints:
            print("Banco wins")
        if self.bancoPoints == self.puntoPoints:
            print("Egalite")
