import random

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}


class Card:
    def __init__(self, suit, rank, is_ace):
        # defining the card's suit, face value, and value of the card
        self.suit = suit
        self.rank = rank
        self.is_ace = is_ace

    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def show(self):
        print(f"{self.rank} of {self.suit}")
    


card = Card(suits[random.randint(0, 3)], ranks[random.randint(0, 13)], False)
card.show() 


class Deck:
    def __init__(self):
        self.cards = []
        
    def build_deck(self):    
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank, False)
                self.cards.append(card)

    def show_deck(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        print("Shuffling the deck...")
        random.shuffle(self.cards)
        print("Deck shuffled!")

    def draw(self):
        return self.cards.pop()
    

deck = Deck()
deck.build_deck()
deck.shuffle()
print(deck.draw())

class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.value = 0
        self.aces = 0

    def add_card(self, deck):
        card = deck.draw()
        self.hand.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
        print(values[card.rank])

    def remove_card(self):
        self.hand.pop(0)
        self.value -= values[self.hand[0].rank]
        if self.hand[0].rank == "Ace":
            self.aces -= 1
        print(values[self.hand[0].rank])

    def hit(self, card):
        card = self.cards.pop(0)
        self.cards.append(card)
        self.value += values[card.rank]

    def stand(self):
        pass

bob = Player("Bob")
bob.add_card(deck)

class Dealer:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def deal(self):
        self.cards.append(self.deck.cards.pop(0))
        return self.cards.pop(0)
    
    def hit(self):
        pass

    def stand(self):
        pass
           




# def main():
#     print("Welcome to Blackjack: ALL OR NOTHING EDITION")