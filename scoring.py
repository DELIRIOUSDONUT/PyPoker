import pyCardDeck
# noinspection PyCompatibility
from typing import List
from pyCardDeck.cards import PokerCard

## Give a score to each hand, judge hands based on score

class Scorer():

    # Card value mapping
    CARD_VALUES = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
        '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    # Hand rankings from lowest to highest
    HAND_RANKINGS = [
        'High Card', 'One Pair', 'Two Pair', 'Three of a Kind', 
        'Straight', 'Flush', 'Full House', 'Four of a Kind', 
        'Straight Flush', 'Royal Flush'
    ]

    def __init__(self, hand: List[PokerCard], table_cards: List[PokerCard]):
        # Cards are in descending order
        self.cards = sorted(hand + table_cards, key=lambda x: self.CARD_VALUES[x[:-1]], reverse=True)
        self.ranks = [card[:-1] for card in self.cards]
        self.suits = [card[-1] for card in self.cards]

        self.suits = self._count_suits()
        self.ranks = self._count_ranks()

    def _count_suits(self):
        counts = {}
        for card in self.cards:
            counts[card.suit] = counts.get(card.suit, 0) + 1
        return counts
    
    def _count_ranks(self):
        counts = {}
        for card in self.cards:
            counts[card.rank] = counts.get(card.rank, 0) + 1
        return counts
    


    def flush(self):
        cards = []
        for suit, count in self.ranks.items():
            if count >= 5 :
                cards = [card for card in self.cards if card[-1] == suit]
                return {
                    'name': 'Flush',
                    'cards': sorted(cards, key=lambda x: self.CARD_VALUES[x[:-1]], reverse=True)[:5]
                }
            
        return None


    
    def straight(self):

        sorted_vals =  sorted(set(self.CARD_VALUES[rank] for rank in self.ranks))
        # Check for consecutive values
        for i in range(len(sorted_vals) - 4):
            if sorted_vals[i+4] - sorted_vals[i] == 4:
                # Find the actual cards that match these values
                straight_cards = [
                    card for card in self.cards 
                    if self.CARD_VALUES[card[:-1]] in sorted_vals[i:i+5]
                ]
                return {
                    'name': 'Straight',
                    'cards': sorted(straight_cards, key=lambda x: self.CARD_VALUES[x[:-1]], reverse=True)
                }
            
        # Check for Ace-low straight (A-2-3-4-5)
        if set(sorted_vals) >= {14, 2, 3, 4, 5}:
            low_straight_ranks = {'A', '2', '3', '4', '5'}
            straight_cards = [
                card for card in self.cards 
                if card[:-1] in low_straight_ranks
            ]
            return {
                'name': 'Straight',
                'cards': sorted(straight_cards, key=lambda x: self.CARD_VALUES[x[:-1]], reverse=True)
            }
        
        return None
    
    
    def high_card_search(self):
        # Gets highest ranking card in number form
        return {'name': "High Card",
                'cards': self.cards[0]}

    def one_pair(self):
        for i in range(len(self.cards), 1, -1):
            if self.CARD_VALUES[self.cards[i][:-1]] == self.CARD_VALUES[self.cards[i-1][:-1]]:
                # Highest pair found
                return {'name': "Pair",
                        'cards': self.cards[i-1] + self.cards[i]}
        return None
                
    def two_pair(self):
        pairs = []
        for i in range(len(self.cards), 1, -1):
            if self.CARD_VALUES[self.cards[i][:-1]] == self.CARD_VALUES[self.cards[i-1][:-1]]:
                # Highest pair found, now to find next pair
                pairs.append(self.cards[i-1])
                pairs.append(self.cards[i])
                for j in range(i-2, 1, -1):
                    if self.CARD_VALUES[self.cards[j][:-1]] == self.CARD_VALUES[self.cards[j-1][:-1]]:
                        # Both pairs found
                        pairs.append(self.cards[j-1])
                        pairs.append(self.cards[j])
                        return {'name': "Two Pair",
                                'cards': pairs}
        return None
            
    #TODO: resolving ties? not needed for texas holdem
    #TODO: straight flush, royal flush, four kind, three kind, full house

