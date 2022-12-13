import tkinter as tk
import random

txt = True

def func():
    l = tk.Label(root, text='Din mamma!')
    l.place(x=random.randint(0,400), y=random.randint(0,400))

root = tk.Tk()

myLabel = tk.Label(root, text='Hello world')
myButton = tk.Button(root, text='Click me!', command=func)

myLabel.pack()
myButton.pack()

root.minsize(400, 400)
root.mainloop()