import tkinter as tk
from tkinter import ttk
import string as sg
from string import *
win = tk.Tk()
win.title("Rhythm's GUI")

# Modification of label

aLabel = ttk.Label(win, text="what would you like to encrypt??")
aLabel.grid(column=0, row=0)

# Button Click event Function
def encrypt():
	action.configure(text='Hello, the outcome is \n' + i)
	aLabel.configure(foreground='red')
	aLabel.configure(text='A red Label')


# adding a textbox
plainText = input()
plainText_entered = tk.Entry(win, width=12, textvariable = plainText)
plainText_entered.grid(column = 0, row = 1)

#code for reverse cypher
i = len(plainText) - 1
while i >= 0:
	translated = translated + plainText[i]
	i = i - 1

# Adding a Button
action = ttk.Button(win, text="encrypt", command=encrypt)
action.grid(column= 1, row=1)
plainText_entered.focus() #place your name into entry


win.mainloop()
