import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python GUI')

win.resizable(0, 0)

# Modify button click function
def clickMe():
    action.configure(text='Hello ' + name.get() + ' ' + numberChosen.get())

action = ttk.Button(win, text='Click Me!', command=clickMe)
action.grid(column=2, row=1)

# Change the label
ttk.Label(win, text='Enter a name:').grid(column=0, row=0)

# Add a textbox entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
nameEntered.focus()

# Add a combobox widget
ttk.Label(win, text='Choose a number:').grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

win.mainloop()

