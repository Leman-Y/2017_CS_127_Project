'''
import random
import enchant

def closest_to_a(list):
    l=[]
    for item in list:
        if item=='#':                         #Whoever gets blank gets to go first
            pass
        l.append(abs(ord('a')-ord(item)))      #finds the difference of each letter from a
    
    return l.index(min(l))                     #Give the minimum value

l=['g','b','c','z','g','a']

print(closest_to_a(l))
'''
'''
2. Grab the code from classcode under the scrabble folder. It makes a scrabble board. Write a routine add_word_across(board,word,r,c)
which will add the word word to the board board going across starting at r,c. It should return the score for the word.
This should be the scrabble score that accounts for double letter, double word, triple letter, and triple word squares.
Squares with lower case letter 'd' and 't' are double and triple letter squares and upper case are for double and triple word.
You'll replace those square and blanks with the letters of the word.

Then write added_word_down(board,word,r,c) which does the same but adds the word from top to bottom starting at r,c

'''

TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10), (7,7))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

def make_scrabble_board():
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

#x=make_scrabble_board()
#print_board(x)
        
def score(w):
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
    scoreofword=score(word)
    sumofscore=0
    
    for count, letter in enumerate(word): #Tell me the position of each letter in the word & the letter itself
       # print(count, letter)
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
            
        board[r][c+count]=word[count] #I am able to put the word on the board. Position of the square is changed to the position of the word.
        #print(r)
        #print(c+count)
        #print(board[r][c+count]) #I determined that the letter is now assigned to a position on the board
        #print(word[count])
        
    print(sumofscore)
    
    #print(score(word))
    print(print_board(board))
        #print(count,letter)
    
def add_word_down(board,word,r,c):
    scoreofword=score(word)
    sumofscore=0
    
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
            
        board[r+count][c]=word[count] #I am able to put the word on the board. Position of the square is changed to the position of the word.
        #print(r)
        #print(c+count)
        #print(board[r][c+count]) #I determined that the letter is now assigned to a position on the board
        #print(word[count])
        
    print(sumofscore)
    
    #print(score(word))
    print(print_board(board))
        #print(count,letter)
    
'''
Notes 10/29/17:
-1. Replace the squares of the board with the letters
-2. Count the letters the length
-3. R,C position of board then add r,c+i. i=position of the letter in the word
-4. If letter is in one of the special cases (d,D,t,T) reflect that in the score
-5. r is y-axis
-6. c is x-axis

Test case:
Hello: h= 4 , e=1, l=1 , l=1 , 0=1
-If I do (add_word_across(board,'hello',1,0)), I should get 4+16+1+1+1=23
-Now this hello is added to the board as well. How do I just have the board itself. Make different boards for each.
-Board and Board1 are now different, bc the function affected the boards. But if we make them different values then you get a brand new board for each. 
'''
    
board=make_scrabble_board()
#print_board(board)
alpha="abcdefghijklmnopqrstuvwxyz#"

(add_word_across(board,'hello',1,((alpha.index('a'))+1))) #Run the function. The board is manipualted
board1=make_scrabble_board()
board2=make_scrabble_board()
board3=make_scrabble_board()
#print_board(board1)
print('-----------------------------------')

#(add_word_across(board,'hello',1,0))

print('------------------------------------')

#(add_word_down(board2,'hello',0,0)) #Should get 29
