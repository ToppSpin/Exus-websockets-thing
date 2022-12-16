import tkinter as tk

txt = True

def func():
    global txt
    if txt:
        myLabel.config(text="Hej")
        txt = False
    else:
        myLabel.config(text="Din mamma")
        txt=True


root = tk.Tk()

myLabel = tk.Label(root, text="du", anchor='n')
myLabel.pack(side=tk.TOP)
myButton = tk.Button(root, command=func, text='CLICK ME!')
myButton.pack(side=tk.LEFT)
root.minsize(1000, 400)
root.mainloop()