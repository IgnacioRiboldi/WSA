# Assigment 2: Card Draw
# By Ignacio Riboldi

import requests
from collections import Counter

# Shyffle URL
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(shuffle_url).json()

deck_id = response["deck_id"]
print(f"Deck ID: {deck_id}")

# Draw 5 cards
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
cards_response = requests.get(draw_url).json()

cards = cards_response["cards"]

print("\nYour cards:")
values = []
suits = []

for card in cards:
    print(f"- {card['value']} of {card['suit']}")
    values.append(card["value"])
    suits.append(card["suit"])

#Special cards mapping

value_map = {
    "ACE": 14,
    "KING": 13,
    "QUEEN": 12,
    "JACK": 11
}

numeric_values = []
for v in values:
    if v in value_map:
        numeric_values.append(value_map[v])
    else:
        numeric_values.append(int(v))

value_counts = Counter(values)
suit_counts = Counter(suits)

# Check for pair and triple
has_pair = 2 in value_counts.values()
has_triple = 3 in value_counts.values()

# Check for flush (same suit)
has_flush = 5 in suit_counts.values()

# Check for straight
numeric_values.sort()
has_straight = numeric_values == list(
    range(numeric_values[0], numeric_values[0] + 5)
)

# Final Results

print("\nResults:")

if has_triple:
    print("🎉 Congratulations! You got a TRIPLE!")
elif has_pair:
    print("🎉 Congratulations! You got a PAIR!")

if has_straight:
    print("🎉 Congratulations! You got a STRAIGHT!")

if has_flush:
    print("🎉 Congratulations! All cards are the SAME SUIT!")

if not (has_pair or has_triple or has_straight or has_flush):
    print("No special hand this time — try again! 😄")
