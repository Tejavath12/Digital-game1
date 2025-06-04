from tkinter import *
import time

def update():
    current = time.strftime("%H:%M:%S")
    label.config(text=current)
    label.after(1000, update)

root = Tk()
root.title("Digital Clock")
label = Label(root, font=("Arial", 60), fg="green")
label.pack()
update()
root.mainloop()
