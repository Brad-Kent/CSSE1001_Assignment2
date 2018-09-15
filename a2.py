#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""

__author__ = "Bradley Kent 45355194"
from enum import Enum
from random import random

# Write your classes here


class Deck:# TODO: Testing Ready

    def __init__(self, starting_cards: list=None):
        if starting_cards is None:
            self._cards = []
        else:  # Probs don't need the else
            self._cards: list = starting_cards

    def get_cards(self) -> list:
        return self._cards

    def get_amount(self) -> int:
        return len(self._cards)

    def shuffle(self):
        # Todo: Shuffle
        return self._cards

    def pick(self, amount: int=1):
        # Done_Todo: not sure if i need to check the amount
        if amount < 1 or len(self._cards) < amount:
            return None
        else:
            cards = self._cards[-amount:]
            for card in cards:
                self._cards.remove(card)
            return cards

    def add_card(self, card: 'Card'):
        self._cards.append(card)

    def add_cards(self, cards: list):
        for card in cards:
            self._cards.append(card)

    def top(self):
        if len(self._cards) < 1:
            return None
        # Todo: Not sure if i should be returning a pointer/ ref :/
        return self._cards[-1]


class Player:

    def __init__(self, name: str):
        self._name = name
        self._deck: Deck = Deck()

    def get_name(self) -> str:
        return self._name

    def get_deck(self) -> Deck:
        return self._deck

    def is_playable(self):
        raise NotImplementedError('Fucked')

    def has_won(self):
        return True if self._deck.get_amount() <= 0 else False

    def pick_card(self, putdown_pile: Deck):
        raise NotImplementedError


class HumanPlayer(Player):
    def __init__(self, name: str):
        Player.__init__(self, name)

    def is_playable(self):
        return True

    def pick_card(self, putdown_pile: Deck):
        return None


class ComputerPlayer(Player):
    def __init__(self, name: str):
        super().__init__(name)

    def is_playable(self):
        return False

    def pick_card(self, putdown_pile: Deck):
        pass # some how i have to pick a card


class Card:

    def __init__(self, number: int, color: str):
        self._number = number
        self._color = color

    def __str__(self):
        return 'Card({}, {})'.format(self._number, self._color)

    def __repr__(self):
        return self.__str__()

    def play(self, player: Player, game):
        pass

    def get_colour(self):
        return self._color

    def get_number(self) -> int:
        return self._number

    def set_number(self, number: int):
        self._number = number

    def set_color(self, color):
        self._color = color

    def get_pickup_amount(self):
        return 1

    def matches(self, card: 'Card'):
        pass


class SkipCard(Card):
    pass


class ReverseCard(Card):
    pass


class Pickup2Card(Card):
    def get_pickup_amount(self):
        return 2


class Pickup4Card(Card):
    def get_pickup_amount(self):
        return 4


def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()

