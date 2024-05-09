def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2


# taking the input from the user about the numbers
num1 = eval(input("Enter the first number : "))
num2 = eval(input("Enter the second number : "))

while(True):
    operations = {"+":add,"-":subtract,"*":multiply,"/":divide}
    for symbols in operations:
        print(symbols,end=" ")
    symbol = input("Choose a operation : ")
    answer = operations[symbol](num1,num2)
    print(f"{num1} {symbol} {num2} = {answer}")

    breakout = input("Do you want to continue ?(yes/no)").lower()
    if(breakout != "no"):
        loop = input(f"Do you want to continue with {answer} ?(yes/no)").lower()
        if(loop=="yes"):
            num1 = answer
            num2 = eval(input("Enter the second number : "))
        else:
            num1 = eval(input("Enter the first number : "))
            num2 = eval(input("Enter the second number : "))
    else:
        break
    
