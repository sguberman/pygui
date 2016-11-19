import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


win = tk.Tk()
win.title('Python GUI')

#win.resizable(0, 0)

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

# Add three checkboxes
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text='Disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text='Unchecked', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text='Enabled', variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# Radiobutton globals
COLOR1 = 'Blue'
COLOR2 = 'Gold'
COLOR3 = 'Red'
colors = [COLOR1, COLOR2, COLOR3]

# Radiobutton callback
def radCall():
    radSel = radVar.get()
    win.configure(background=radSel)

# Add three radio buttons in a loop
radVar = tk.StringVar()
radVar.set('None')
for i, color in enumerate(colors):
    rad = tk.Radiobutton(
        win, text=color, variable=radVar, value=color, command=radCall)
    rad.grid(column=i, row=5, sticky=tk.W)

# Using a scrolled text control
scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

# Create a container to hold labels
labelsFrame = ttk.LabelFrame(win, text=' Labels in a Frame ')
labelsFrame.grid(column=0, row=7, padx=20, pady=40)

# Place labels into the container element
ttk.Label(labelsFrame, text='Label1').grid(column=0, row=0)
ttk.Label(labelsFrame, text='Label2').grid(column=0, row=1)
ttk.Label(labelsFrame, text='Label3').grid(column=0, row=2)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)

win.mainloop()

