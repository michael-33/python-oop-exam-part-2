from card_module import Deck, cards_stats, max_card, Card, CardSuit, CardRank

deck = Deck()
# print(deck)

# print("deck size", len(deck))
# card = deck.draw()
# print("card", card)
# print("deck size", len(deck))
# new_card = Card(CardSuit(1), CardRank(2))
# print("adding new card")
# deck.add_card(new_card)
# print("deck size", len(deck))

# test validation
# print(deck.cards)
# deck.add_card(Card(CardSuit(1), CardRank(2)))


# # accessing by index
# print("Accessing cards directly by index:")
# for i in range(5):
#     print(f"Card at index {i}: {deck[i]}")

# # iterate the cards in the deck
# print("Iterating through all cards in the deck:")
# for card in deck:
#     print(card)

# # return the highest card
# highest_card = max_card(*deck.cards)
# print("highest_card", highest_card)

# # prtint lowest card
# print("lowest card", min(*deck.cards))

# # get statistics
# stats = cards_stats(*deck.cards, max=2, min=1, len=1)
# print("stats", stats)