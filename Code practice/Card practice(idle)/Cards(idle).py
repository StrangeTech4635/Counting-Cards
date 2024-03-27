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

for Spades in range(1,14):
    if Spades == 1:
        Spades = "Ace"
    elif Spades == 11:
        Spades = "Jack"
    elif Spades == 12:
        Spades = "Queen"
    elif Spades == 13:
        Spades = "King"
    for Diamonds in range(1,14):
        if Diamonds == 1:
            Diamonds = "Ace"
        elif Diamonds == 11:
            Diamonds = "Jack"
        elif Diamonds == 12:
            Diamonds = "Queen"
        elif Diamonds == 13:
            Diamonds = "King"
        for Hearts in range(1,14):
            if Hearts == 1:
                Hearts = "Ace"
            elif Hearts == 11:
                Hearts = "Jack"
            elif Hearts == 12:
                Hearts = "Queen"
            elif Hearts == 13:
                Hearts = "King"
            for Clubs in range(1,14):
                if Clubs == 1:
                    Clubs = "Ace"
                elif Clubs == 11:
                    Clubs = "Jack"
                elif Clubs == 12:
                    Clubs = "Queen"
                elif Clubs == 13:
                    Clubs = "King"
                print(Spades, " of Spades" ":", Diamonds, " of Diamonds" ":", Hearts, " of Hearts", ":", Clubs, "Of Clubs",)
