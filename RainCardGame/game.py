import random


deckcolor = ('Srdce', 'Kříže', 'Listy', 'Kule')
deckcard = ('7', '8', '9', '10', 'J', 'Q', 'K', 'A')





class Card:

    def __init__(self, name, rank, color):
        self.name = name
        self.rank = rank
        self.color = color

    def draw_card(self):


    def play_card(self):



def main():
    # Create deck
    paul = Warrior("Paul", 50, 20, 10)
    sam = Warrior("Sam", 50, 20, 10)

    # Create Battle object
    battle = Battle()

    # Initiate Battle
    battle.startFight(paul, sam)

main()
