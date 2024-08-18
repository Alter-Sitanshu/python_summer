import tkinter as tk
from tkinter import ttk

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None
#functions used
def start_count_down():
    global REPS
    REPS += 1

    if REPS%2 !=0:
        title_label.config(text="Work")
        count_down(WORK_MIN*60-1)

    elif REPS%8 == 0:
        title_label.config(text="Long Break")
        count_down(LONG_BREAK_MIN*60 -1)
    else:
        title_label.config(text="Short Break")
        count_down(SHORT_BREAK_MIN*60 -1)

def count_down(secs):
    mins = secs//60
    sec = secs%60
    if sec <10 :
        sec = f"0{sec}"
    if mins <10 :
        mins = f"0{mins}"
    canvas.itemconfig(timer_text, text=f"{mins}:{sec}")
    if secs > 0:
        global timer
        timer = screen.after(1000, count_down, secs-1)
    else:
        mark = ""
        work_sessions = REPS//2
        for _ in range(work_sessions):
            mark += "✔"
        marks.config(text=mark)
        start_count_down()
    
def reset_timer():
    global REPS
    REPS = 0
    screen.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    marks.config(text="")

#Setting up GUI for the pomodoro app
screen = tk.Tk()
screen.minsize(width=500, height=400)
screen.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(master=screen, text="Timer", font=(FONT_NAME, 32, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1,row=0)

canvas = tk.Canvas(master=screen, width=200, height=224, highlightthickness=0, bg=YELLOW)
tomato_img = tk.PhotoImage(file='pomodoro\\tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1,row=1)

start_button = tk.Button(text="Start", padx=5, pady=5, font=(FONT_NAME, 14, "bold"), command=start_count_down)
start_button.grid(column=0, row=2, pady=20)
reset_button = tk.Button(text="Reset", padx=5, pady=5, font=(FONT_NAME, 14, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2, pady=20)

#check marks
marks = tk.Label(master=screen, text="", fg=GREEN, bg=YELLOW)
marks.grid(column=1,row=3)
screen.mainloop()