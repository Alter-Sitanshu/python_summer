import random
from replit import clear
from higherlower.data import *

score = 0
a = random.randrange(0,len(data))
b = random.randrange(0,len(data))
if(a == b):
    b = random.randrange(0,len(data))

compA = data[a]
compB = data[b]
print(compA , compB)
def game():
    print(logo)
    print(f"Compare A : {compA["name"]} a {compA["description"]} from {compA["country"]}")
    print(vs)
    print(f"Compare A : {compB["name"]} a {compB["description"]} from {compB["country"]}")
    guess = input("Higher or Lower ? : ").lower()
    if((compA["follower_count"]>compB["follower_count"] and guess == "higher") or (compA["follower_count"]<compB["follower_count"] and guess == "lower") ):
        score += 1
        compA = compB
        compB = data[random.randrange(0,len(data))]
        if(compA == compB):
            compB = data[random.randrange(0,len(data))]
        clear()
        game()
    else:
        print(f"You Lost ! Your Score is {score}")
        score = 0
        loop = input("Do you want to play again ?(yes/no) : ").lower()
        if(loop == "yes"):
            compA = data[random.randrange(0,len(data))]
            compB = data[random.randrange(0,len(data))]
            if(compA == compB):
                compB = data[random.randrange(0,len(data))]
            game()
        else:
            return


game()