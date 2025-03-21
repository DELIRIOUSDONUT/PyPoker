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
        hand = [PokerCard("Hearts", "9", "Nine"), PokerCard("Hearts", "10", "Ten")]
        field = [
            PokerCard("Spades", "9", "Nine"), PokerCard("Spades", "K", "King"),
            PokerCard("Spades", "A", "Ace"), PokerCard("Spades", "2", "Two"),
            PokerCard("Spades", "10", "Ten")
        ]
        scorer = Scorer(hand, field)
        result = scorer.high_card_search()
        self.assertEqual(result['cards'], PokerCard("Spades", "A", "Ace"))

    def testOnePair(self):
        hand = [PokerCard("Hearts", "9", "Nine"), PokerCard("Diamonds", "9", "Nine")]
        field = [
            PokerCard("Spades", "K", "King"), PokerCard("Clubs", "A", "Ace"),
            PokerCard("Hearts", "2", "Two"), PokerCard("Diamonds", "3", "Three"),
            PokerCard("Clubs", "4", "Four")
        ]
        scorer = Scorer(hand, field)
        result = scorer.one_pair()
        self.assertEqual(result['name'], "Pair")

    def testTwoPair(self):
        hand = [PokerCard("Hearts", "9", "Nine"), PokerCard("Diamonds", "9", "Nine")]
        field = [
            PokerCard("Spades", "K", "King"), PokerCard("Clubs", "K", "King"),
            PokerCard("Hearts", "2", "Two"), PokerCard("Diamonds", "3", "Three"),
            PokerCard("Clubs", "4", "Four")
        ]
        scorer = Scorer(hand, field)
        result = scorer.two_pair()
        self.assertEqual(result['name'], "Two Pair")

    def testThreeOfAKind(self):
        hand = [PokerCard("Hearts", "9", "Nine"), PokerCard("Diamonds", "9", "Nine")]
        field = [
            PokerCard("Spades", "9", "Nine"), PokerCard("Clubs", "K", "King"),
            PokerCard("Hearts", "2", "Two"), PokerCard("Diamonds", "3", "Three"),
            PokerCard("Clubs", "4", "Four")
        ]
        scorer = Scorer(hand, field)
        result = scorer.three_of_a_kind()
        self.assertEqual(result['name'], "Three of a kind")

    def testFourOfAKind(self):
        hand = [PokerCard("Hearts", "9", "Nine"), PokerCard("Diamonds", "9", "Nine")]
        field = [
            PokerCard("Spades", "9", "Nine"), PokerCard("Clubs", "9", "Nine"),
            PokerCard("Hearts", "2", "Two"), PokerCard("Diamonds", "3", "Three"),
            PokerCard("Clubs", "4", "Four")
        ]
        scorer = Scorer(hand, field)
        result = scorer.four_of_a_kind()
        self.assertEqual(result['name'], "Four of a kind")

    def testFullHouse(self):
        hand = [PokerCard("Hearts", "9", "Nine"), PokerCard("Diamonds", "9", "Nine")]
        field = [
            PokerCard("Spades", "K", "King"), PokerCard("Clubs", "K", "King"),
            PokerCard("Diamonds", "K", "King"), PokerCard("Hearts", "2", "Two"),
            PokerCard("Diamonds", "3", "Three")
        ]
        scorer = Scorer(hand, field)
        result = scorer.full_house()
        self.assertEqual(result['name'], "Full House")

    def testFlush(self):
        hand = [PokerCard("Hearts", "9", "Nine"), PokerCard("Hearts", "K", "King")]
        field = [
            PokerCard("Hearts", "A", "Ace"), PokerCard("Hearts", "2", "Two"),
            PokerCard("Hearts", "3", "Three"), PokerCard("Diamonds", "4", "Four"),
            PokerCard("Clubs", "5", "Five")
        ]
        scorer = Scorer(hand, field)
        result = scorer.flush()
        self.assertEqual(result['name'], "Flush")

    def testStraight(self):
        hand = [PokerCard("Hearts", "9", "Nine"), PokerCard("Diamonds", "10", "Ten")]
        field = [
            PokerCard("Spades", "J", "Jack"), PokerCard("Clubs", "Q", "Queen"),
            PokerCard("Diamonds", "K", "King"), PokerCard("Hearts", "2", "Two"),
            PokerCard("Diamonds", "3", "Three")
        ]
        scorer = Scorer(hand, field)
        result = scorer.straight()
        self.assertEqual(result['name'], "Straight")

    def testStraightFlush(self):
        hand = [PokerCard("Hearts", "9", "Nine"), PokerCard("Hearts", "10", "Ten")]
        field = [
            PokerCard("Hearts", "J", "Jack"), PokerCard("Hearts", "Q", "Queen"),
            PokerCard("Hearts", "K", "King"), PokerCard("Diamonds", "2", "Two"),
            PokerCard("Clubs", "3", "Three")
        ]
        scorer = Scorer(hand, field)
        result = scorer.straight_flush()
        self.assertEqual(result['name'], "Straight Flush")

    def testRoyalFlush(self):
        hand = [PokerCard("Hearts", "10", "Ten"), PokerCard("Hearts", "J", "Jack")]
        field = [
            PokerCard("Hearts", "Q", "Queen"), PokerCard("Hearts", "K", "King"),
            PokerCard("Hearts", "A", "Ace"), PokerCard("Diamonds", "2", "Two"),
            PokerCard("Clubs", "3", "Three")
        ]
        scorer = Scorer(hand, field)
        result = scorer.royal_flush()
        self.assertEqual(result['name'], "Royal Flush")