#!/usr/bin/env python

import random

class CardDeck():
 # data
    SUITS = 'Clubs Diamomnds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


    def __init__(self,dealer): #constrcuctor is namaed init
        self._dealer = dealer
        self.color = "Blue"
        self._create_deck()


    #private function
    def _create_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if len(self) == 0:
            raise ValueError("No more cards")
        return self._cards.pop()


    def get_suits(self):
        return self.SUITS

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        name = type(self).__name__
        return "{}({})".format(name,len(self))



#operators
    def __add__(self, other):
        tmp = CardDeck(self.dealer)
        tmp._cards = self.cards + other.cards


    @property
    def cards(self):
        return self._cards
    #option 1: getter method

    def get_dealer(self):
        return self._dealer

    #option 2: getter property
    @property
    def dealer(self):
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):
        self._dealer = dealer
    # foo.get_dealer() method
    # foo.dealer () prop


if __name__ == '__main__':
    d1 = CardDeck("Joe")