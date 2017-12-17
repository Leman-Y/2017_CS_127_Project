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