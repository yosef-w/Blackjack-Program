import random
import time

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
values = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}

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
            return "None"
        
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
        return self.hand

    def hit(self,deck):
        card = deck.draw()
        self.hand.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
        self.check_ace()

    def new_hand(self, deck):
        self.hand =[]

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
        print(f"\nDealers's hand:\n")
        if show:
            for card in self.hand:
                print(f"{card.rank} of {card.suit}")
            print("\n" + '*' * 25)
        else:
            print("Hidden Card")
            if len(self.hand) > 1:
                print(f"{self.hand[1].rank} of {self.hand[1].suit}")
            print("\n" + '*' * 25)

    def continue_game(self, deck):
        while True:
            if self.calculate_score() > 17:
                break
            elif self.calculate_score() < 17:
                print("Dealer's score is below 17. Dealer hits...")
                time.sleep(1)
                self.hit(deck)
                self.show_hand(show=True)
                break
        

class Player(Human):
    def __init__(self):
        super().__init__('Player')
        self.player_score = 0

    def show_hand(self):
        print(f"\n{self.name}'s hand:\n")
        for card in self.hand:
            print(f"{card.rank} of {card.suit}")
        print("=" * 40)


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.active = True

                
    def play_again(self):            
        retry = input("Would you like to play again? (y/n) ")
        if retry.lower() == "n":
            print("Goodbye! Come back if you would like to play again.")
            exit()
        elif retry.lower() == "y":
            self.deck = Deck()
            self.dealer.new_hand(self.deck)
            self.player.new_hand(self.deck)
            self.active = True
            self.play()
        else:
            print("Invalid entry. Please enter 'y' or 'n'")
            self.play_again()


    def play(self):
        print("\nWELCOME TO BLACKJACK:")
        opening = input("Would you like to play Blackjack? (y/n) ")
        if opening.lower() == "y":
            # name = input("What is your name? ")
            # player = Player()
            # dealer = Dealer()
            while self.active:
                self.deck.shuffle()
                print("\nThe deck is shuffled -- Let's play!")
                time.sleep(1)
                self.dealer.deal(self.deck)
                self.player.deal(self.deck)

                player_score = self.player.calculate_score()
                dealer_score = self.dealer.calculate_score()

                if player_score == 21:
                    print("BLACKJACK! You win!")
                    self.play_again()

                    
                if dealer_score == 21:
                    print("Dealer has blackjack... You lose.")
                    self.play_again()

                while player_score < 21 and dealer_score < 21:
                    choice = input("Hit or Stand? ")
                    if choice.lower() == "hit":
                        self.player.hit(self.deck)
                        time.sleep(1)
                        self.dealer.show_hand()
                        self.player.show_hand()
                        player_score = self.player.calculate_score()
                        if player_score > 21:
                            print("You scored over 21...Bust! You lose!")
                            self.play_again()
                        elif player_score == 21:
                            print("BLACKJACK! You win!")
                            self.play_again()



                    elif choice.lower() == "stand":
                        dealer_score = self.dealer.calculate_score()
                        time.sleep(1)
                        self.dealer.show_hand(show=True)
                        time.sleep(1)
                        print(f"Dealer's score is: {dealer_score}")
                        while dealer_score < 17:
                            self.dealer.continue_game(self.deck)
                            dealer_score = self.dealer.calculate_score()
                            self.player.show_hand()
                            if dealer_score > 21:
                                print("Dealer scored over 21... You win!")
                                self.play_again()
                                
                        if dealer_score > player_score and dealer_score < 22:
                            print(f"Dealer wins with a score of {dealer_score}. You lose.")
                            self.play_again()
                            
                        elif dealer_score < player_score and player_score < 22:
                            print(f"You scored {player_score}, you win!")
                            self.play_again()
                            
                        elif dealer_score == player_score:
                            print("It's a tie!")
                            self.play_again()                   

                    else:
                        print("Invalid entry. Please enter 'hit' or'stand'")

        elif opening.lower() == "n":
            print("Goodbye! Come back if you would like to play Blackjack.")
            active = False

def main():
    game = Game()
    game.play()

main()