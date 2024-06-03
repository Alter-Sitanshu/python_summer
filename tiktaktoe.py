import tkinter as tk
import random as rnd
from tkinter import messagebox
GAME_BG = "#bfe072"
winning_sequences: tuple = (((0,0),(0,1),(0,2)),((0,0),(1,1),(2,2)),((0,0),(1,0),(2,0)),((1,0),(1,1),(1,2))
                            ,((2,0),(2,1),(2,2)),((1,0),(1,1),(1,2)),((0,2),(1,2),(2,2)),((0,2),(1,1),(2,0)))
player_choices: list = []
computer_choices: list = []
class game:
    buttons: dict[str, tk.Button] = {}
    @classmethod
    def boardInitiator(cls) -> None:
        global player_choices, computer_choices
        player_choices = []
        computer_choices = []
        for _ in range(9):
            cls.buttons[f"b{_}"] = tk.Button(master=screen, width=20, height=10, command= lambda b=_: cls.buttonclicked(b))
            col = _%3
            row = _//3
            cls.buttons[f"b{_}"].grid(column=col, row=row, padx=5, pady=5)

#----button click handling------
    @classmethod
    def buttonclicked(cls, b: int) -> None:
        global player_choices
        col = b%3
        row = b//3
        coord: tuple = (row,col)
        if (coord not in player_choices) and (coord not in computer_choices):
            player_choices.append(coord)
            cls.buttons[f"b{b}"].config(text="O", font=("Ariel", 9, "bold"))
            if not gameOver():
                cls.compMove(cls)
#-----Move generator---------
    def compMove(cls) -> None:
        global player_choices, computer_choices
        col = rnd.randint(0,2)
        row = rnd.randint(0,2)
        if len(computer_choices+player_choices) != 9:
            while (row,col) in player_choices or (row,col) in computer_choices:
                col = rnd.randint(0,2)
                row = rnd.randint(0,2)
            id = (row*3) + col
            computer_choices.append((row,col))
            cls.buttons[f"b{id}"].config(text="X", font=("Ariel", 9, "bold"))
            gameOver()
#------checking game over conditions------
    @classmethod
    def check(cls, sequence: list) -> bool:
        if len(sequence) < 3:
            return False
        else:
            for seq in winning_sequences:
                count: int = 0
                for points in seq:
                    if points in sequence:
                        count+=1
                if count == 3:
                    return True
            else:
                return False
#-----terminating game-------
def gameOver() -> bool:
    if game.check(sequence= player_choices):
        repeat = messagebox.askyesno(title="Again ?", message="You Won\nPlay Again ?")
        if not repeat:
            screen.destroy()
            return True
        else:
            screen.destroy()
            GUI()

    elif game.check(sequence= computer_choices):
        repeat = messagebox.askyesno(title="Again ?", message="You Lost\nPlay Again ?")
        if not repeat:
            screen.destroy()
            return True
        else:
            screen.destroy()
            GUI()

    elif len(player_choices+computer_choices) == 9:
        repeat = messagebox.askyesno(title="Again ?", message="Draw\nPlay Again ?")
        if not repeat:
            screen.destroy()
            return True
        else:
            screen.destroy()
            GUI()

#----building the GUI for the game-----
screen = None
def GUI() -> None:
    global gameOver_label,screen
    screen = tk.Tk()
    screen.minsize(width=800, height=700)
    screen.title("Tik-Tak-Toe")
    screen.config(padx=200, pady=100, bg=GAME_BG)

    game.boardInitiator()
    screen.mainloop()

#----initialising the program-------
GUI()