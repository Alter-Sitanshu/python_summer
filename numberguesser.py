import random
from replit import clear



while(True):
    number = random.randint(0,100)
    level = input("Select a difficulty level (Easy/Hard) : ").lower()
    if(level == "hard"):
        lives = 5
    else:
        lives = 10
    print(f"You have {lives} lives remaining.")
    while(lives>0):
        guess = int(input("Enter your guess : "))
        if(guess > number):
            print("Too High")
            lives-=1
        elif(guess < number):
            print("Too Low")
            lives-=1
        else:
            print("You Won. Correct Guess !")
            break
        print(f"You have {lives} lives remaining.")
    loop = input("Do you want to play again ?(yes/no) : ").lower()
    if(loop != "yes"):
        break
    else:
        clear()