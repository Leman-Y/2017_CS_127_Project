'''
Scrabble Project Outline
----------------------

What we did:

-Ask player: Scrabble is a 2-4 player game so when you input 1 then we should repeat the question until they give us 2-4!

What we need to do:

-Draw for first play. The player with the letter closest to "A" plays first. A blank tile beats any letter. Return the letters to the pool and remix.
    -All players draw seven new letters and place them on their racks.
    -If two players tie for first, repeat
-Add function that allows the user to pull up the rules.txt file when needed
-Each word will go through a dictionary library to see if it is part of the english dictionary.
'''

players = {}
num_p = 0

alpha = "abcdefghijklmnopqrstuvwxyz"

letter_score = {"#" : "0",
                "aeioulnrst":"1", 
                "dg":"2", 
                "bcmp":"3", 
                "fhvwy":"4",
                "k":"5",
                "jx":"8",
                "qz":"10"}

basket_of_letters = ["a", 9, "b", 2, "c", 2, "d", 4, "e", 12
                    "f", 2, "g", 3, "h", 2, "i", 9, "j", 1,
                    "k", 1, "l", 4, "m", 2, "n", 6, "o", 8,
                    "p", 2, "q", 1, "r", 6, "s", 4, "t", 6, 
                    "u", 4, "v", 2, "w", 2, "x", 1, "y", 2, 
                    "z", 1, "#", 2 ]


def ask_player():
    '''
        Ask how many players are playing
        then makes a "score board" in dict
        in form of {Player #: score}
        0 < player # <= 4
    '''
    global num_p
    while (num_p < 1 or num_p > 4):
        num_p = int(input("How many players will there be? "))
    for i in range(int(num_p)):
        players.setdefault(i+1,0)
    print(players)

ask_player()