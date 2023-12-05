from tkinter import *
import random as rng

root = Tk()
root.title('Color')
root.geometry('450x450')
root.config(bg = 'snow')

text = ('Black', 'Purple', 'Green', 'Blue', 'Red')
color = ('black', 'purple', 'green', 'blue', 'red')

def alter():
    lblColor['text'] = text[rng.randint(0, len(text) - 1)]
    lblColor['fg'] = color[rng.randint(0, len(color) - 1)]

lblColor = Label(root, bg = 'snow', font = ('Arial', 25))
lblColor.place(relx = 0.5, rely = 0.4, anchor = CENTER)
btnColor = Button(root, text = 'Alter Label', command = lambda: alter())
btnColor.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()