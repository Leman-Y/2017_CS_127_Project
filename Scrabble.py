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
-Merriam-Webster's Official Scrabble® Players Dictionary, Fourth Edition (OSPD4) Thats the dictionary scrabble uses
-

'''


players = {}
num_p = 0

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