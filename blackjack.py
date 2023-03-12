import random

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def show(self):
        print(f"{self.rank} of {self.suit}")

class Deck:
    def __init__(self):
        self.deck = []
        self.build_deck()
        self.shuffle()

    def build_deck(self):    
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)

    def deal(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            None
        
    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()

class Human:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.value = 0
        self.aces = 0

    def check_ace(self):
        while self.value >= 22 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def deal(self, deck):
        self.hand.append(deck.draw())
        self.hand.append(deck.draw())
        self.show_hand()

    def hit(self,deck):
        card = deck.draw()
        self.hand.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
        self.check_ace
        self.show_hand()

    def calculate_score(self):
        self.value = 0
        self.aces = 0
        for card in self.hand:
            if card.rank == "Ace":
                self.aces += 1
            elif card.rank in ["Jack", "Queen", "King"]:
                self.value += 10
            else:
                self.value += values[card.rank]
        for num in range(self.aces):
            if self.value + 11 >= 22:
                self.value +=1
            else:
                self.value += 11

        return self.value

class Dealer(Human):
    def __init__(self):
        super().__init__("Dealer")
        self.dealer_score = 0

    def show_hand(self, show=False):
        print(f"Dealers's hand:\n")
        if show:
            for card in self.hand:
                print(f"{card.rank} of {card.suit}")
        else:
            print("Hidden Card")
            if len(self.hand) > 1:
                print(f"{self.hand[1].rank} of {self.hand[1].suit}")

    def continue_game(self):
        while True:
            if self.calculate_score() > 17:
                break
            elif self.calculate_score() < 17:
                print("Dealer's score is below 17. Dealer hits...")
                self.hit()
                self.show_hand(show=True)
        

class Player(Human):
    def __init__(self, name):
        super().__init__(name)
        self.player_score = 0

    def show_hand(self):
        print(f"\n{self.name}'s hand:")
        for card in self.hand:
            print(f"{card.rank} of {card.suit}")


def main():
    deck = Deck()
    active = True

    print("WELCOME TO BLACKJACK:")
    opening = input("Would you like to play Blackjack? (y/n) ")
    if opening.lower() == "y":
        name = input("What is your name? ")
        player = Player(name)
        dealer = Dealer()
        while active and name.lower():
            print("The deck is shuffled -- Let's play!")
            dealer.deal(deck)
            player.deal(deck)

            player_score = player.calculate_score()
            dealer_score = dealer.calculate_score()

            if player_score == 21:
                print("BLACKJACK! You win!")
            if dealer_score == 21:
                print("Dealer has blackjack... You lose.")

            while player_score < 21 or dealer_score < 21:
                choice = input("Hit or Stand? ")
                if choice.lower() == "hit":
                    player.hit()
                    dealer.show_hand()
                    player.show_hand()
                    player_score = player.calculate_score()
                    if player_score > 21:
                        print("You scored over 21...Bust! You lose!")
                        active = False
                elif choice.lower() == "stand":
                    dealer_score = dealer.calculate_score()
                    while dealer_score < 17:
                        dealer.continue_game()
                        dealer_score = dealer.calculate_score()
                        if dealer_score > 21:
                            print("Dealer scored over 21... You win!")
                            active = False
                    if dealer_score > player_score:
                        print(f"Dealer wins with a score of {dealer_score}. You lose.")
                        break
                    elif dealer_score < player_score:
                        print(f"You scored {player_score}, you win!")
                        break
                    elif dealer_score == player_score:
                        print("It's a tie!")
                        break
                    break
                else:
                    print("Invalid entry. Please enter 'hit' or'stand'")
            break
        
    elif opening.lower() == "n":
        print("Goodbye! Come if you would like to play again.")
        active = False

    else:
        print("Invalid entry. Please enter 'y' or 'n'" )

main()