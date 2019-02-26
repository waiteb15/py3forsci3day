#!/usr/bin/env python

from card_deck import CardDeck
from jokerdeck import JokerDeck
d1 = CardDeck('Bo')
print(d1.get_dealer())

print(d1.dealer)

d1.shuffle()

print(d1.cards)


j1 = JokerDeck("Bill")

j1.shuffle()

print(j1.cards)