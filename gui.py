import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu


win = tk.Tk()
win.title('Python GUI')

# Add tab controls
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill='both')

#win.resizable(0, 0)

# Create a container frame for each tab
monty = ttk.LabelFrame(tab1, text=' Monty Python ')
monty.grid(column=0, row=0, padx=8, pady=4)
monty2 = ttk.LabelFrame(tab2, text=' The Snake ')
monty2.grid(column=0, row=0, padx=8, pady=4)

# Modify button click function
def clickMe():
    action.configure(text='Hello ' + name.get() + ' ' + numberChosen.get())

action = ttk.Button(monty, text='Click Me!', command=clickMe)
action.grid(column=2, row=1)

# Change the label
ttk.Label(monty, text='Enter a name:').grid(column=0, row=0, sticky='W')

# Add a textbox entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky='W')
nameEntered.focus()

# Add a combobox widget
ttk.Label(monty, text='Choose a number:').grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(
    monty, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# Add three checkboxes
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(
    monty2, text='Disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(
    monty2, text='Unchecked', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(
    monty2, text='Enabled', variable=chVarEn)
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
    monty2.configure(text=radSel)

# Add three radio buttons in a loop
radVar = tk.StringVar()
radVar.set('None')
for i, color in enumerate(colors):
    rad = tk.Radiobutton(
        monty2, text=color, variable=radVar, value=color, command=radCall)
    rad.grid(column=i, row=6, sticky=tk.W)

# Using a scrolled text control
scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, row=5, columnspan=3, sticky='WE')

# Create a container to hold labels
labelsFrame = ttk.LabelFrame(monty2, text=' Labels in a Frame ')
labelsFrame.grid(column=0, row=7, padx=5, pady=5)

# Place labels into the container element
ttk.Label(labelsFrame, text='Label1').grid(column=0, row=0)
ttk.Label(labelsFrame, text='Label2').grid(column=0, row=1)
ttk.Label(labelsFrame, text='Label3').grid(column=0, row=2)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)

def _quit():
    win.quit()
    win.destroy()
    exit()

# Add a menu bar to the window
menuBar = Menu(win)
win.config(menu=menuBar)

# File menu
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label='New')
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=_quit)
menuBar.add_cascade(label='File', menu=fileMenu)

# Help menu
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label='About')
menuBar.add_cascade(label='Help', menu=helpMenu)

win.mainloop()

