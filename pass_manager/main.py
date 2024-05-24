import tkinter as tk
from tkinter import messagebox
FONT = ("Courier", 14, "bold")

#----------Appending to the data file---------
def save(website, email, password):
    with open("data.txt",'a') as file:
        file.write(f"{website} | {email} | {password}\n")
        web_text.delete(0, tk.END)
        gen_pass_text.delete(0, tk.END)
        messagebox.showinfo(title="Succes", message="Saved Successfully")
def confirmation():
    website = web_text.get()
    email = email_text.get()
    password = gen_pass_text.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="WARNING", message="The fields cannot be Empty")
    elif len(password)<8:
        messagebox.showwarning(title="WARNING",message="Password should be atleast 8 characters")
    else:
        is_ok = messagebox.askyesno(title=website, message="Are you sure ?")
        if is_ok:
            save(website, email, password)


#---------Random password generator----------
def random_pass():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letters_list+symbols_list+numbers_list
    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    gen_pass_text.insert(0, string=password)


#-------Creating GUI for the app----------
screen = tk.Tk()
screen.minsize(width=500, height=400)
screen.config(padx=100, pady=50)
screen.title("Password Manager")

canvas = tk.Canvas(master=screen, width=200,height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

web_label = tk.Label(master=screen, text="Website :", font=FONT)
email_label = tk.Label(master=screen, text="Email :", font=FONT)
gen_pass_label = tk.Label(master=screen, text="Password :", font=FONT)
web_label.grid(column=0, row=1, pady=5)
email_label.grid(column=0, row=2, pady=5)
gen_pass_label.grid(column=0, row=3, pady=5)

web_text = tk.Entry(master=screen, font=FONT, width=35)
web_text.focus()
email_text = tk.Entry(master=screen, font=FONT, width=35)
email_text.insert(0, string="sitanshu5@gmail.com")
gen_pass_text = tk.Entry(master=screen, font= FONT, width=24)
web_text.grid(column=1, row=1, columnspan=2, pady=5)
email_text.grid(column=1, row=2, columnspan=2, pady=5)
gen_pass_text.grid(column=1, row=3, pady=5)

generate = tk.Button(text="Generate Password", pady=3, command=random_pass)
add = tk.Button(text="Add", width=54, command=confirmation)
generate.grid(column=2, row=3, padx=5)
add.grid(column=1, row=4, columnspan=2, pady=5)

screen.mainloop()
