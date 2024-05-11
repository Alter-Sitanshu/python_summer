from recipe import *
from replit import clear

SALES = 0
print(logo)
def coffee():
    global SALES
    order_complete = False
    print("MENU : espresso , latte , cappucino")
    while not order_complete:
        money = 0
        order = input("What would you like to have ? ").lower()
        while order == "report":
            for resource in resources:
                print(f"{resource} : {resources[resource]}")
            order = input("What would you like to have ? ").lower()
        if order in MENU.keys():
            bill = MENU[order]["cost"]
            print("Please make the payment in BILLS only")
            rupee_10 = int(input("Number of 10 rupee notes : "))
            rupee_100 = int(input("Number of 100 rupee notes : "))
            rupee_50 = int(input("Number of 50 rupee notes : "))
            money = 10*rupee_10 + 100*rupee_100 + 50*rupee_50
            if money < bill:
                print("Transaction unsuccessful. Money refunded")
                order_complete = True
                money = 0
            else:
                ingredients = MENU[order]["ingredients"]
                for resource in resources:
                    if resources[resource]-ingredients[resource] > 0:
                        continue
                    else:
                        order_complete = True
                        break
                if order_complete == True:
                    print("Insufficient ingridients. Sorry !!")
                    break
                for resource in resources:
                    if resources[resource]-ingredients[resource] > 0:
                        resources[resource]-=ingredients[resource]
                SALES += bill
                print("Your order is Ready !!!")
                print(f"Here is your change {money-bill}")
                order_complete = True
        elif order == "off":
            return
        else:
            print("Wrong Order !!")
            coffee()
    loop = input("Do you want to place another order ?(yes/no) ").lower()
    if loop == "yes":
        clear()
        coffee()
    else:
        view_sales = input("Do you want to view sales ?").lower()
        if view_sales == "yes":
            print(f"Today's sales are : {SALES}")
        return

def restock(ingredient, amount):
    resources[ingredient] += amount
    more = input("Do you want to restock anything more ? ").lower()
    if more == "yes":
        ingredient = input("Enter the ingredient : ")
        amount = eval(input("Enter amount : "))
        restock(ingredient,amount)
    else:
        return


action = input("What do you want to do ?(restock/order) ").lower()
if action == "order":
    coffee()
elif action == "restock":
    ingredient = input("Enter the ingredient : ").lower()
    amount = eval(input("Enter amount : "))
    restock(ingredient,amount)
elif action == "off":
    print("Turning off machine")