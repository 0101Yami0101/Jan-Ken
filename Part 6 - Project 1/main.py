#Rock Paper and scissor game....

import random

def GameRes(comp,your):
    if comp == 'r':
        if your == 'r':
            return None
        elif your == 'p':
            return True
        elif your == 's':
            return False
    elif comp == 'p':
        if your == 'r':
            return False
        elif your == 'p':
            return None
        elif your == 's':
            return True
    elif comp == 's':
        if your == 'r':
            return True
        elif your == 'p':
            return False
        elif your == 's':
            return None




print("Rock(r), Paper(p) and Scissors(s) ... Computer is picking.. ")

randomno = random.randint(1,3)

if randomno == 1:
    comp = 'r'
elif randomno == 2:
    comp = 'p'
elif randomno == 3:
    comp = 's'

your = input("Enter Your Pick:- ")


Result = GameRes(comp,your)
if Result == None:
    print("Tie !!")
elif Result == True:
    print("You Win !!")
else:
    print("You Lose !!")

print("Computer has picked",comp)




