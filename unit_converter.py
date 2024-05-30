import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def mileToKm():
    try:  
        miles = eval(entry_1.get())
    except SyntaxError:
        messagebox.showwarning("Null Error", "No Value Was Entered")
    else:
        km = miles * 1.609
        entry_2.delete(0, tk.END)
        entry_2.insert(index=0,string=str(km))

def celsToFarh():
    try:
        cels = eval(entry_1.get())
    except SyntaxError:
        messagebox.showwarning("Null Error", "No Value Was Entered")
    else:
        farh = 32 + (9 * cels / 5)
        entry_2.delete(0, tk.END)
        entry_2.insert(index=0,string=str(farh))

def converter():
    option = combo.get()
    if option == "Miles To Km":
        mileToKm()
    elif option == "Cels To Farh":
        celsToFarh()
    else:
        messagebox.showwarning("WARNING", "Select a Converter")

def setconverter(event):
    option = combo.get()
    if option == "Miles To Km":
        first_label.config(text="Miles")
        second_label.config(text="Km")
    else:
        first_label.config(text="Celsius")
        second_label.config(text="Fahrenheit")


screen = tk.Tk()
screen.wm_minsize(height=300, width=500)
screen.config(padx=50, pady=100)

#Creating labels for the input field
first_label = tk.Label(master=screen, text="From", font=("Helvetica", 16, "bold"))
second_label = tk.Label(master=screen, text="To", font=("Helvetica", 16, "bold"))
first_label.grid(column=0,row=0)
second_label.grid(column=0,row=3)

#Creating the Entry elements respective to their labels
entry_1 = tk.Entry(master=screen, width=30, font=("Helvetica", 16, "bold"))
entry_2 = tk.Entry(master=screen, width=30, font=("Helvetica", 16, "bold"))
entry_1.grid(column=2,row=0, padx=5)
entry_2.grid(column=2,row=3, padx=5)

#Creating the button to calculate the conversion
calc = tk.Button(text="Convert", font=("Helvetica", 8, "bold"), padx=10, pady=10, command=converter)
calc.grid(column=2, row=4, pady=20)

#Creating radiobuttons to make a universal convertor
# radio_state = tk.IntVar()
# radiobutton1 = tk.Radiobutton(text="Miles->Km", value=1, variable=radio_state, command=setconverter, font=("Helvetica", 14, "bold"))
# radiobutton2 = tk.Radiobutton(text="Cels->Farh", value=2, variable=radio_state, command=setconverter, font=("Helvetica", 14, "bold") )
# radiobutton1.grid(column=2, row=5, pady=10)
# radiobutton2.grid(column=2, row=6, pady=0)

#Creating a combobox
combo = ttk.Combobox(master=screen, values=["Miles To Km","Cels To Farh"])
combo.grid(column=2, row=5, pady=10)
combo.set("Select units to convert")
combo.bind("<<ComboboxSelected>>",func=setconverter)


screen.mainloop()