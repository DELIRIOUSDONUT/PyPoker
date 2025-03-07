from unittest import TestCase
from scoring import Scorer

#imports from scoring
import pyCardDeck
# noinspection PyCompatibility
from typing import List
from pyCardDeck.cards import PokerCard
from collections import OrderedDict


class TestScoring(TestCase):
    def testHighCard(self):
        # Create hand and community cards
        hand = []
        field = []
        
        hand.append(PokerCard("Hearts", "9", "Nine"))
        hand.append(PokerCard("Hearts", "10", "Ten"))

        field.append(PokerCard("Spades", "9", "Nine"))
        field.append(PokerCard("Spades", "K", "King"))
        field.append(PokerCard("Spades", "A", "Ace"))
        field.append(PokerCard("Spades", "2", "2"))
        field.append(PokerCard("Spades", "10", "Ten"))

        # Init scorer

        scorer = Scorer(hand, field)

        result = scorer.high_card_search()

        self.assertEqual(result['cards'], PokerCard("Spades", "A", "Ace"))