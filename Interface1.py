from tkinter import *
from GoogleSearch import Search
import webbrowser

root = Tk()

root.title = ("GUI")
font1 = "Courier"

query = ''

title = Label(root, text = "What's in your fridge?", font=(font1, 36))
title.pack()
prompt = Label (root, text = "Enter your ingredients separated by a comma:", font = (font1, 12))
prompt.pack()
entry = Entry(root, width = 50)
entry.pack()
entry.focus_set() 
websitepromp = Label(root, text = "enter website", font=(font1,36))
website = Entry(root, width = 50)
websitepromp.pack()
website.pack()
website.focus_set()
def clicklink(link):
    webbrowser.open_new(link)
def callback(): 
    ingredients = (entry.get())
    arr = ingredients.strip().split(',')
    query = website.get()
    s = Search(arr)
    s.search(query)
    link = s.links
    for x in link:
        clicklink(x)
    vv = Label(root, text = '\n'.join(link), font = (font1, 10))
    vv.pack()
    # vv.bind("<Button-1>", clicklink)
Enterbtn = Button(text = "Enter", command = callback)

Enterbtn.pack()
root.mainloop()

