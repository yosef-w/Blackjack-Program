import random

# class Game:
#     # establish the rules of the game
#     def __init__(self):
#         pass




class Card:
    def __init__(self, suit, card_type, value):
        # defining the card's suit, face value, and value of the card
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        card_type = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}
        self.suit = suit
        self.card_type = card_type
        self.value = value
    
    def __str__(self):
        return f"{self.suit} of {self.card_type} {self.value}"
    
    def __repr__(self):
        pass
    
    def price(self):
        if self.


class Deck:
    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for value in self.value:
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        print("Shuffling the deck...")
        random.shuffle(self.cards)

class Dealer:
    def __init__(self, deck):
        self.cards = []
        self.deck = deck

    def deal(self):
        self.cards.append(self.deck.cards.pop(0))
        return self.cards.pop(0)
    
    def hit(self):
        pass

    def stand(self):
        pass
           


class Player:
    def __init__(self, deck, dealer):
        self.cards = []
        self.deck = deck
        self.dealer = dealer

    def hit(self):

    def stand(self):


def main():
    print("Welcome to Blackjack!")