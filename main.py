import pyCardDeck

from classes import Player, PokerTable

my_deck = pyCardDeck.Deck(cards=[1, 2, 3], name='My Awesome Deck')

my_deck.shuffle()

card = my_deck.draw()

print(card)

player = Player("testplayer")
player2 = Player("t2")
ptable = PokerTable([player, player2])

ptable.texas_holdem()
