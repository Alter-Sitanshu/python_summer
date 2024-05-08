import random
from replit import clear
from hangman.hangman_art import *
print(logo)
random_word = random.choice(word)
length = len(random_word)

hidden = []
for i in range(length):
    hidden.append("_")

lives = 6
while(True):
    guess = input("Guess the letter : ").lower()
    clear()
    for letter in range(length):
        if random_word[letter] == guess:
            hidden[letter] = guess
        else:
            continue
    for i in range(length):
        print(hidden[i],end=" ")
    if(guess not in random_word):
        lives-=1
        print(stages[lives])
        if(lives==0):
            print("YOU LOST !")
            break
    if("_" not in hidden):
        print("YOU WON !")
        break

