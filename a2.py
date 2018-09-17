#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""

__author__ = "Bradley Kent 45355194"

from enum import Enum
from random import random
from typing import Union
# Write your classes here


class Player:
    """The base type of player which is not meant to be initiated.
            * Abstract class
    """

    def __init__(self, name: str):
        self._name = name
        self._deck: Deck = Deck()

    def get_name(self) -> str:
        return self._name

    def get_deck(self) -> 'Deck':
        return self._deck

    def is_playable(self):
        raise NotImplementedError('Base Class(Player) not playable')

    def has_won(self) -> bool:
        return True if self._deck.get_amount() <= 0 else False

    def pick_card(self, putdown_pile: 'Deck'):
        raise NotImplementedError('Base Class(Player) has not imp Pick')


class HumanPlayer(Player):
    """A human player that selects cards to play using the GUI."""
    def __init__(self, name: str):
        Player.__init__(self, name)

    def is_playable(self):
        return True

    def pick_card(self, putdown_pile: 'Deck'):
        return None


class ComputerPlayer(Player):
    def __init__(self, name: str):
        super().__init__(name)

    def is_playable(self):
        return False

    def pick_card(self, putdown_pile: 'Deck') -> Union['Card', None]:
        played_card: Union['Card', None] = putdown_pile.top()

        index = 0
        for card in self._deck.get_cards():
            if card.matches(played_card):
                del self._deck.get_cards()[index]
                return card
            index += 1

        return None


class Deck:  # TODO: Testing Ready

    def __init__(self, starting_cards: list=None):
        if starting_cards is None:
            self._cards: list = []
        else:  # Probs don't need the else
            self._cards: list = starting_cards

    def get_cards(self) -> list:
        return self._cards

    def get_amount(self) -> int:
        return len(self._cards)

    def shuffle(self):
        # Todo: Shuffle w/ Random
        return self._cards

    def pick(self, amount: int=1):
        # Done_Todo: not sure if i need to check the amount

        if amount < 1 or len(self._cards) < amount:
            #raise ValueError
            #return None
            print("No Cards")
            #return None

        cards = self._cards[-amount:]
        for _ in cards:
            del self._cards[-amount]
            amount -= 1
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
        #print("This should not be an error:", self._cards[-1], "Type:", type(self._cards[-1]))
        return self._cards[-1]


class Card:
    """ A card represents a card in the uno game which has colour and number attributes. """

    def __init__(self, number: int, color: str):
        self._number = number
        self._color = color

    def __str__(self):
        return 'Card({}, {})'.format(self._number, self._color)

    def __repr__(self):
        return self.__str__()

    def get_number(self) -> int:
        return self._number

    def get_colour(self) -> str:
        return self._color

    def set_number(self, number: int):
        self._number = number

    def set_color(self, color: str):
        self._color = color

    def get_pickup_amount(self) -> int:
        return 1

    def matches(self, card: 'Card') -> bool:
        # Todo: This could be a single bool
        is_legal_color = False
        is_legal_num = False

        if self._color == card.get_colour():
            is_legal_color = True
        if self._number == card.get_number():
            is_legal_num = True

        return is_legal_color or is_legal_num

    def play(self, player: Player, game):
        pass  # Pass as specified by Documentation


class SkipCard(Card):  # Todo: Write inheritance into class comment
    """A card which skips the turn of the next player. Matches with cards of the same colour."""
    def __str__(self):
        return 'SkipCard({}, {})'.format(self._number, self._color)

    def __repr__(self):
        return self.__str__()

    def play(self, player: Player, game):
        game.skip()

    def matches(self, card: 'Card') -> bool:
        return self._color == card.get_colour()


class ReverseCard(Card):
    """A card which reverses the order of turns. Matches with cards of the same colour."""

    def __str__(self):
        return 'ReverseCard({}, {})'.format(self._number, self._color)

    def __repr__(self):
        return self.__str__()

    def play(self, player: Player, game):
        game.reverse()

    def matches(self, card: 'Card') -> bool:
        return self._color == card.get_colour()


class Pickup2Card(Card):
    """A card which makes the next player pickup two cards. Matches with cards of the same colour"""

    def __str__(self):
        return 'Pickup2Card({}, {})'.format(self._number, self._color)

    def __repr__(self):
        return self.__str__()

    def get_pickup_amount(self):
        return 2

    def play(self, player: Player, game):
        pickup_cards = game.pickup_pile.pick(self.get_pickup_amount())
        game.next_player().get_deck().add_cards(pickup_cards)

    def matches(self, card: 'Card'):
        return self._color == card.get_colour()


class Pickup4Card(Card):
    def __str__(self):
        return 'Pickup4Card({}, {})'.format(self._number, self._color)

    def __repr__(self):
        return self.__str__()

    def get_pickup_amount(self) -> int:
        return 4

    def play(self, player: Player, game):
        pickup_cards = game.pickup_pile.pick(self.get_pickup_amount())
        game.next_player().get_deck().add_cards(pickup_cards)

    def matches(self, card: 'Card'):
        return True


def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()

