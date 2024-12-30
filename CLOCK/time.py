import tkinter as tk
# import time
from time import strftime

root = tk.Tk()
root.title("PAIN-XER DIGITAL CLOCK")

def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text = string)
    label.after(1000, time)

label = tk.Label(root, font = ('calibri', 40, 'bold'), background = 'pink', foreground = 'white')
label.pack(anchor = 'center')

time()

root.mainloop()