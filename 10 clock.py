from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("clock")
root.geometry("680x60")

label = Label(root, background = "black", foreground = "#FF0000")
label.pack(anchor='center')

def time():
    string = strftime('%Y/%m/%d %I:%M:%S %p')
    label.config(text=string, width = "30", font=("aerial", 44))
    label.after(1000, time)
time()

mainloop()