# -*- coding: utf-8 -*-
"""
Program Name: Prequel Reference Ha Ha Funny
Author: Luke Henriksen
Version: 1.24.2020.1

"""
from tkinter import *

root = Tk()
root.title('Obi Wan')
root.geometry('500x100')

def greivous():
    messagebox.showinfo("General Grievous", "General Kenobi")
    
button = Button(root, text="Hello there", command=greivous)

button.pack()

root.mainloop()