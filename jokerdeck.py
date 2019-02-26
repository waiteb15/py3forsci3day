#!/usr/bin/env python

from card_deck import CardDeck

class JokerDeck(CardDeck):
#    pass # don't do anything -- placeholder

    def _create_deck(self):
        super()._create_deck()
        self._cards.append(('Joker',1))
        self._cards.append(('Joker',2))



