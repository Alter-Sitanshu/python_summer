import tkinter as tk
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
    data = df.to_dict(orient="records")
else:
    data = df.to_dict(orient="records")
random_word = {}
timer = None
#-------defining the functionality--------
def know() -> None:
    data.remove(random_word)
    new_df = pd.DataFrame(data)
    new_df.to_csv("data/to_learn.csv", index=None)
    screen.after_cancel(timer)
    new_word()
def dont_know():
    screen.after_cancel(timer)
    new_word()
def new_word() -> None:
    global data, random_word, timer
    random_word = random.choice(data)
    canvas.itemconfig(card_image, image= card_front)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=random_word["French"], fill="black")
    timer = screen.after(3000, flip)
def flip() -> None:
    canvas.itemconfig(card_image, image= card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=random_word["English"], fill="white")
#-----Making the GUI for the app-----
screen = tk.Tk()
screen.minsize(width=600, height=500)
screen.title("Flash Card")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(master=screen, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image= card_front)
title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 252, text="Word", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

yes_img = tk.PhotoImage(file="images/right.png")
no_img = tk.PhotoImage(file="images/wrong.png")
yes = tk.Button(master=screen, image=yes_img, highlightthickness=0, command=know)
no = tk.Button(master=screen, image=no_img, highlightthickness=0, command=dont_know)
yes.grid(column=0, row=1)
no.grid(column=1, row=1)



new_word()
screen.mainloop()