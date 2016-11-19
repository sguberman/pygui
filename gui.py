import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python GUI')

win.resizable(0, 0)

# Modify adding a label
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

# Button click Event Callback Function
def clickMe():
    action.configure(text='** I have been clicked! **')
    aLabel.configure(foreground='red')

action = ttk.Button(win, text='Click Me!', command=clickMe)
action.grid(column=1, row=0)

win.mainloop()

