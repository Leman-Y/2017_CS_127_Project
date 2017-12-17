import random
import enchant


#a='abcd'

#print(random.choice(a))

basket_of_letters = ["a", 9, "b", 2, "c", 2, "d", 4, "e", 12, 
                    "f", 2, "g", 3, "h", 2, "i", 9, "j", 1,
                    "k", 1, "l", 4, "m", 2, "n", 6, "o", 8,
                    "p", 2, "q", 1, "r", 6, "s", 4, "t", 6, 
                    "u", 4, "v", 2, "w", 2, "x", 1, "y", 2, 
                    "z", 1, "#", 2 ]
letter = ''
print('\n--------------------------\n')

def randomtile(basket_of_letters):
    '''
    -use random.choice works with strings and lists
    -use the basket and multiple i and i+1 together to get a,2 to 'aa' then random.choice to get a random character

    Input:
    -Basket of letters
    Output:
    -Random character tile
    '''
    newbasket=''
    
    
    for i in range(len(basket_of_letters)-1):
        if type(basket_of_letters[i])==int:
            pass
        else:
            newbasket+=(basket_of_letters[i]*basket_of_letters[i+1])
            #basket_of_letters[i+1]=basket_of_letters[i+1]-1
    
    newtile=random.choice(newbasket)
    index=basket_of_letters.index(newtile)
    basket_of_letters[index+1]=basket_of_letters[index+1]-1
    
    
    
    #print(basket_of_letters.index(newtile))
    #global letter
    #letter=newtile
    #for index, value in enumerate(basket_of_letters)
    
    
    return newtile

'''
#print("Which tile did you get?")
#tile=input()
#print(tile)
'''

print(randomtile(basket_of_letters))
#print(letter)

#print(basket_of_letters.index(letter))

#indexofnumber=basket_of_letters.index(letter)
#basket_of_letters[indexofnumber+1]=basket_of_letters[indexofnumber+1]-1

print(basket_of_letters)



