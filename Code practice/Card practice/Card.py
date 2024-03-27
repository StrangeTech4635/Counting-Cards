"""
    Obtain a Card and go up the 52 cards
    Jiovanny
    3/25/24
"""


#Annotate variables
Spades: int
Diamonds: int
Hearts: int
Clubs: int

def GetCardType(card):
    if card == 1:
        return "Ace"
    elif card == 11:
        return "Jack"
    elif card == 12:
        return "Queen"
    elif card == 13:
        return "King"
    else:
        return card

for Spades in range(1,14):
    for Diamonds in range(1,14):
        for Hearts in range(1,14):
            for Clubs in range(1,14):
                print(GetCardType(Spades), " of Spades" ":", GetCardType(Diamonds), " of Diamonds" ":", GetCardType(Hearts), " of Hearts", ":", GetCardType(Clubs), "Of Clubs",)
