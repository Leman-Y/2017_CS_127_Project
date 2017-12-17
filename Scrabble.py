import random
import enchant
'''
DOWNLOADS NEEDED IN ORDER TO RUN:
pip install pyenchant


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
-We need to add the 1-15 y-axis and a-z for the top
-Fix score function to be dictionary
'''

players = {}
num_p = 0
letter_count = 100
alpha = "abcdefghijklmnopqrstuvwxyz#"

letter_score = {"#" : "0",
                "aeioulnrst":"1", 
                "dg":"2", 
                "bcmp":"3", 
                "fhvwy":"4",
                "k":"5",
                "jx":"8",
                "qz":"10"}

basket_of_letters = ["a", 9, "b", 2, "c", 2, "d", 4, "e", 12, 
                    "f", 2, "g", 3, "h", 2, "i", 9, "j", 1,
                    "k", 1, "l", 4, "m", 2, "n", 6, "o", 8,
                    "p", 2, "q", 1, "r", 6, "s", 4, "t", 6, 
                    "u", 4, "v", 2, "w", 2, "x", 1, "y", 2, 
                    "z", 1, "#", 2 ]
# '#'=Blank
TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10), (7,7))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))


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
        players.setdefault(i+1,[0,""])
    print(players)

def randomtile(basket_of_letters):
    '''
    12/8/17, Gives a random tile from the basket
    -use random.choice works with strings and lists
    -use the basket and multiple i and i+1 together to get a,2 to 'aa' then random.choice to get a random character
    Problem:
    Remove a tile from basket_of_letters
    

    Input:
    -Basket of letters
    Output:
    -Random character tile
    '''
    newbasket='' #Empty string
    for i in range(len(basket_of_letters)-1):  #Index of each position 
        if type(basket_of_letters[i])==int:    #If the type of value is a int
            pass                               #Pass and move to else
        else: 
            newbasket+=(basket_of_letters[i]*basket_of_letters[i+1]) #Ex. Add the '##' from #,2 to the empty string\
            
    #print(newbasket)
    newtile=random.choice(newbasket)                    #Randomly choose a character from the newbasket
    index=basket_of_letters.index(newtile)              #Index of newtile in original basket 
    basket_of_letters[index+1]=basket_of_letters[index+1]-1       #Change the value of how many of the random letters there are -1.
     
    return newtile  #Return a random tile
    



def make_scrabble_board():
    '''
    Makes scrabble board
    12/7 9:45 pm UPDATE made it os board has numbers and letters on side
    '''
    board=[]
    
    for i in range(16):
        line=[] # each line of the board
        if (i != 0): # prints numbers on y axis of board
            if (i < 10): # helps align the single and double digit numbers ie 9 vs 10
                hello = str(i) + " " 
                line.append(hello)
            else:
                line.append(str(i))
        for j in range(16): 
            if (i ==0 and j ==0): # (0,0) is a " "
                line.append('  ')
            elif (i == 0 and  j < 17): #add letters to x axis
                line.append(alpha[j-1])
            elif (j < 15): #makes rest of board
                line.append('_')
        board.append(line)

    # adds the cap and lower letter to board vvv
    for r,c in TRIPLE_WORD_SCORE:
        board[r+1][c+1] = 'T' 

    for r,c in DOUBLE_WORD_SCORE:
        board[r+1][c+1] = 'D'

    for r,c in TRIPLE_LETTER_SCORE:
        board[r+1][c+1]='t'

    for r,c in DOUBLE_LETTER_SCORE:
        board[r+1][c+1] = 'd'
    return board


def print_board(b):  #Organizes the lines so it looks like a board
    for line in b:
        print (' '.join(line))

def score(w):
  '''
  Input: letter
  Output: Score of letter
  '''
  sum1=0
  for ch in w:
    if ch.lower() in 'aeioulnrst':
      sum1+=1
    if ch.lower() in 'dg':
      sum1+=2
    if ch.lower() in 'bcmp':
      sum1+=3
    if ch.lower() in 'fhvwy':
      sum1+=4
    if ch.lower() in 'k':
      sum1+=5
    if ch.lower() in 'jx':
      sum1+=8
    if ch.lower() in 'qz':
      sum1+=10
  return sum1

def add_word_across(board,word,r,c):
    '''
    Input: board, word, r, c
    Output: board with word on it
    '''
    scoreofword=score(word)
    sumofscore=0
    
    for count, letter in enumerate(word): #Tell me the position of each letter in the word & the letter itself
        if board[r][c+count]=='T': #3*score of word
            sumofscore+=score(word)*3
            
        if board[r][c+count]=='D':#2*score of word
            sumofscore+=score(word)*2
            
        if board[r][c+count]=='t': #3*score of letter
            sumofscore+=score(word[count])*3
            
        if board[r][c+count]=='d': #2*score of letter
            sumofscore+=score(word[count])*2
            
        if board[r][c+count]=='_': #If square is _
            sumofscore+=score(word[count])
            
        board[r][c+count]=word[count]
        
def add_word_down(board,word,r,c):
    scoreofword=score(word)
    sumofscore=0
    '''
    Input: board, word, r, c
    Output: board with word on it
    ''' 
    for count, letter in enumerate(word): #Tell me the position of each letter in the word & the letter itself
        if board[r+count][c]=='T': #3*score of word
            sumofscore+=score(word)*3
            
        if board[r+count][c]=='D':#2*score of word
            sumofscore+=score(word)*2
            
        if board[r+count][c]=='t': #3*score of letter
            sumofscore+=score(word[count])*3
            
        if board[r+count][c]=='d': #2*score of letter
            sumofscore+=score(word[count])*2
            
        if board[r+count][c]=='_': #If square is _
            sumofscore+=score(word[count])
        board[r+count][c]=word[count]
        
def check_hands(): # checks hands of each player
    global players
    not_empty = []
    for key,value in players.items():
        if len(value[1]) > 0: # if their hand is not empty then add it to a list of players
            not_empty.append(key) 
    return not_empty

def hand_out(): # hands out tiles initial hand 
    for key, value in players.items():
        i = 6
        while (i > 0):
            tile = randomtile(basket_of_letters)
            value[1] += tile
            i = i - 1
        print(value[1])
            
def main():
    print(basket_of_letters)
    ask_player()
    hand_out()
    not_empty = check_hands()
    print(players)
    while(letter_count > 0 or len(not_empty) > 0): # condition to keep playing
        for p in not_empty: # can exchange, place, pass
            word = ""
            while (len(word) <= 0):
                word = input("What do you want to do? You can place a word, exchange, or pass? (type 'place', 'exchange', 'pass') ") 
                word = word.lower()
                if (word == "place"):
                    print("place")
                elif (word == "exchange"):
                    print("exchange")
                elif (word == "pass"):
                    print("pass")
                else:
                    word = ""

print_board(make_scrabble_board())
main()
