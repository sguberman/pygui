import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python GUI')

win.resizable(0, 0)

# Modify button click function
def clickMe():
    action.configure(text='Hello ' + name.get())

action = ttk.Button(win, text='Click Me!', command=clickMe)
action.grid(column=1, row=1)

# Change the label
ttk.Label(win, text='Enter a name:').grid(column=0, row=0)

# Add a textbox entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
nameEntered.focus()

win.mainloop()

