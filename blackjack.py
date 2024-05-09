import random
from replit import clear

def cardraw():
    card = cards[random.randrange(len(cards))]
    return card
    
cards = [1,2,3,4,5,6,7,8,9,10,10,10,10,"A"]

def game():
    print("NEW GAME !")
    while(True):
        player = [cardraw(),cardraw()]
        computer = [cardraw(),cardraw()]
        total_player = 0
        print("Your Cards are : ",end=" ")
        for cards in player:
            print(cards,end=" ")

        print()
        for i in player:
                if(i=="A"):
                    ace = int(input("What value do you want to assign your ace card ?(1/11)"))
                    total_player+=ace
                else:
                    total_player+=i
        print(f"Computer Cards are : {computer[0]} __")
        total_computer = 0
        for i in computer:
            if(i=="A"):
                ace = random.randint(0,1)
                if(ace==0):
                    ace = 1
                else:
                    ace = 11
                total_computer+=ace
            else:
                total_computer+=i
        reply = input("Do you want to draw another card ?(yes/no) ").lower()
        if(reply == "yes"):
            new_card = cardraw()
            print(f"New card is : {new_card}")
            if(new_card == "A"):
                ace = int(input("What value do you want to assign this card ?(1/11)"))
                player.append(ace)
                total_player+= ace
            else:
                player.append(new_card)
                total_player+= new_card
            if(total_player>21):
                print("You Lose !")
                break
            else:
                print("Computer cards are : ")
                for cards in computer:
                    print(cards,end=" ")
                print()
                print(f"Your Total is : {total_player}")
                print(f"Computer Total is : {total_computer}")
                if(total_computer>21):
                    print("You Won !")
                    break
                else:
                    if((21-total_computer)>(21-total_player)):
                        print("You Won !")
                        break
                    else:
                        print("You Lose !")
                        break
        else:
            print("Computer cards are : ")
            for cards in computer:
                print(cards,end=" ")
            print()
            print(f"Your Total is : {total_player}")
            print(f"Computer Total is : {total_computer}")
            if(total_computer>21):
                print("You Won !")
                break

            else:
                if((21-total_computer)>(21-total_player)):
                    print("You Won !")
                    break
                else:
                    print("You Lose !")
                    break
    loop = input("Do you want to play Again ?(yes/no) ").lower()
    if(loop == "yes"):
        clear()
        game()
game()


    