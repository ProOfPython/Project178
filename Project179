from tkinter import *
from tkinter import font
import random as rng

root = Tk()
root.title('Random Color Game')
root.geometry('450x450')
root.config(bg = 'snow')

score = 0
text = ('Black', 'Purple', 'Green', 'Blue', 'Red')
color = ('black', 'purple', 'green', 'blue', 'red')

def alter():
    lblColor['text'] = text[rng.randint(0, len(text) - 1)]
    lblColor['fg'] = color[rng.randint(0, len(color) - 1)]

def check(guess):
    global score
    if guess == lblColor['fg']:
        score += 1
    else:
        score -= 1
    lblScore['text'] = f'Score: { score }'

lblColor = Label(root, bg = 'light blue', font = ('Segoe UI', 25))
lblScore = Label(root, bg = 'light blue', text = 'Score: 0')
lblColor.place(relx = 0.5, rely = 0.4, anchor = CENTER)
lblScore.place(relx = 0.5, rely = 0.6, anchor = CENTER)

entColor = Entry(root)
entColor.place(relx = 0.5, rely = 0.5, anchor = CENTER)

btnAlter = Button(root, text = 'Alter Label', command = lambda: alter())
btnColor = Button(root, text = 'Check Guess', command = lambda: check(entColor.get()))
btnAlter.place(relx = 0.3, rely = 0.6, anchor = CENTER)
btnColor.place(relx = 0.7, rely = 0.6, anchor = CENTER)

root.mainloop()
