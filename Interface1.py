from tkinter import *
from GoogleSearch import Search

root = Tk()

root.title = ("GUI")
font1 = "Courier"

title = Label(root, text = "What's in your fridge?", font=(font1, 36))
title.pack()
prompt = Label (root, text = "Enter your ingredients separated by a comma:", font = (font1, 12))
prompt.pack()
entry = Entry(root, width = 50)
entry.pack()
entry.focus_set() 
def callback(): 
    ingredients = (entry.get())
    arr = ingredients.strip().split(',')
    s = Search(arr)
    s.googleSearch()
    link = s.links
    vv = Label(root, text = '\n'.join(link), font = (font1, 10))
    vv.pack()
Enterbtn = Button(text = "Enter", command = callback)

Enterbtn.pack()
root.mainloop()

