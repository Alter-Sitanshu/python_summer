alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caeser(message,shift,cipher_direction):
    temp = ""
    if (cipher_direction == "decode"):
        shift *= -1
    for letter in message:
        if(letter not in alphabet):
            temp += letter
            continue
        index = alphabet.index(letter)
        new_index = (index+shift)%len(alphabet)
        temp += alphabet[new_index]
    return temp
loop = True
while(loop):
    message = input("Enter your message : ").lower()
    shift = int(input("Enter the shift : "))
    encrypt = caeser(message=message,shift=shift,cipher_direction="encode")
    decrypt = caeser(message=encrypt,shift=shift,cipher_direction="decode")

    print(encrypt,decrypt,sep="\t")
    y_n = input("Continue again ?(yes/no)").lower()
    if(y_n == "no"):
        loop = False
print("Goodbye !")