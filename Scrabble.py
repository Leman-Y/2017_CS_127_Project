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
-We need to add the 1-15 y-axis and a-z for the top
-Fix score function to be dictionary
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

basket_of_letters = ["a", 9, "b", 2, "c", 2, "d", 4, "e", 12, 
                    "f", 2, "g", 3, "h", 2, "i", 9, "j", 1,
                    "k", 1, "l", 4, "m", 2, "n", 6, "o", 8,
                    "p", 2, "q", 1, "r", 6, "s", 4, "t", 6, 
                    "u", 4, "v", 2, "w", 2, "x", 1, "y", 2, 
                    "z", 1, "#", 2 ]
# '#'=Blank


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

def randomtile():
    

TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10), (7,7))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

def make_scrabble_board():
    '''
    Makes scrabble board
    '''
    board=[]
    for i in range(15):
        line=[]
        for i in range(15):
            line.append('_')
        board.append(line)

    for r,c in TRIPLE_WORD_SCORE:
        board[r][c] = 'T'

    for r,c in DOUBLE_WORD_SCORE:
        board[r][c] = 'D'

    for r,c in TRIPLE_LETTER_SCORE:
        board[r][c]='t'

    for r,c in DOUBLE_LETTER_SCORE:
        board[r][c] = 'd'
    return board


def print_board(b):  #Organizes the lines so it looks like a board
    for line in b:
        print ( ' '.join(line))

print_board(make_scrabble_board())

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