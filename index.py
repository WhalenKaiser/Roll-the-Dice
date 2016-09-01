#mini-project, a dice rolling simulator, will use random,
#integer, print and while loops
import random

sup = None
numr = None

def roll():
    numr = random.randint(1, 6)
    return numr

while sup != 'done':
    sup = input("Say roll or done: ")
    if sup == 'roll':
        print (roll())
    else:
        print ('Try again')

print ('I guess we are done here.')
