import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mbox


class ToolTip:
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0


    def showtip(self, text):
        """
        Display text in a tooltip window.
        """
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox('insert')
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry('+%d+%d' % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
            background='#ffffe0', relief=tk.SOLID, borderwidth=1,
            font=('tahoma', '8', 'normal'))
        label.pack(ipadx=1)

    
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


def createToolTip(widget, text):
    tooltip = ToolTip(widget)
    def enter(event):
        tooltip.showtip(text)
    def leave(event):
        tooltip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


class OOP:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Python GUI')
        self.createWidgets()


    def createWidgets(self):
        self.createTabs()
        self.createContainers()
        self.tab1widgets()
        self.tab2widgets()
        self.tab3widgets()
        self.createMenus()


    def createTabs(self):
        # Add tab controls
        tabControl = ttk.Notebook(self.win)
        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text='Tab 1')
        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text='Tab 2')
        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text='Tab 3')
        tabControl.pack(expand=1, fill='both')


    def createContainers(self):
        # Create a container frame for each tab
        self.monty = ttk.LabelFrame(self.tab1, text=' Monty Python ')
        self.monty.grid(column=0, row=0, padx=8, pady=4)
        self.monty2 = ttk.LabelFrame(self.tab2, text=' The Snake ')
        self.monty2.grid(column=0, row=0, padx=8, pady=4)
        self.monty3 = tk.Frame(self.tab3, bg='blue')
        self.monty3.pack()

    
    def tab1widgets(self):
        # Add a button
        self.action = ttk.Button(
            self.monty, text='Click Me!', command=self.clickMe)
        self.action.grid(column=2, row=1)

        # Add a label
        ttk.Label(
            self.monty, text='Enter a name:').grid(column=0, row=0, sticky='W')

        # Add a textbox entry widget
        self.name = tk.StringVar()
        nameEntered = ttk.Entry(self.monty, width=12, textvariable=self.name)
        nameEntered.grid(column=0, row=1, sticky='W')
        nameEntered.focus()

        # Add a combobox widget
        ttk.Label(self.monty, text='Choose a number:').grid(column=1, row=0)
        self.number = tk.StringVar()
        numberChosen = ttk.Combobox(
            self.monty, width=12, textvariable=self.number, state='readonly')
        numberChosen['values'] = (1, 2, 4, 42, 100)
        numberChosen.grid(column=1, row=1)
        numberChosen.current(0)

        # Add a spinbox widget
        self.spin = tk.Spinbox(
            self.monty, values=(1, 2, 4, 42, 100), width=5, bd=8,
            command=self._spin)
        self.spin.grid(column=0, row=2)
        # Add a tooltip
        createToolTip(self.spin, 'This is a spin control.')

        # Using a scrolled text control
        scrolW = 30
        scrolH = 3
        self.scr = scrolledtext.ScrolledText(
            self.monty, width=scrolW, height=scrolH, wrap=tk.WORD)
        self.scr.grid(column=0, row=5, columnspan=3, sticky='WE')
        # Add a tooltip
        createToolTip(self.scr, 'This is a scrolled text widget.')


    def tab2widgets(self):
        # Add three checkboxes
        self.chVarDis = tk.IntVar()
        check1 = tk.Checkbutton(
            self.monty2, text='Disabled', variable=self.chVarDis,
            state='disabled')
        check1.select()
        check1.grid(column=0, row=4, sticky=tk.W)

        self.chVarUn = tk.IntVar()
        check2 = tk.Checkbutton(
            self.monty2, text='Unchecked', variable=self.chVarUn)
        check2.deselect()
        check2.grid(column=1, row=4, sticky=tk.W)

        self.chVarEn = tk.IntVar()
        check3 = tk.Checkbutton(
            self.monty2, text='Enabled', variable=self.chVarEn)
        check3.select()
        check3.grid(column=2, row=4, sticky=tk.W)

        # Radiobutton globals
        COLOR1 = 'Blue'
        COLOR2 = 'Gold'
        COLOR3 = 'Red'
        self.colors = [COLOR1, COLOR2, COLOR3]

        # Add three radio buttons in a loop
        self.radVar = tk.StringVar()
        self.radVar.set('None')
        for i, color in enumerate(self.colors):
            rad = tk.Radiobutton(
                self.monty2, text=color, variable=self.radVar, value=color,
                command=self.radCall)
            rad.grid(column=i, row=6, sticky=tk.W)

        # Create a container to hold labels
        labelsFrame = ttk.LabelFrame(self.monty2, text=' Labels in a Frame ')
        labelsFrame.grid(column=0, row=7, padx=5, pady=5)

        # Place labels into the container element
        ttk.Label(labelsFrame, text='Label1').grid(column=0, row=0)
        ttk.Label(labelsFrame, text='Label2').grid(column=0, row=1)
        ttk.Label(labelsFrame, text='Label3').grid(column=0, row=2)

        for child in labelsFrame.winfo_children():
            child.grid_configure(padx=8, pady=4)


    def tab3widgets(self):
        for n in range(2):
            canvas = tk.Canvas(self.monty3, width=150, height=80,
                highlightthickness=0, bg='orange')
            canvas.grid(row=n, column=n)

    
    def createMenus(self):
        # Add a menu bar to the window
        menuBar = Menu(self.win)
        self.win.config(menu=menuBar)

        # File menu
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label='New')
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=self.quit)
        menuBar.add_cascade(label='File', menu=fileMenu)

        # Help menu
        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label='About', command=self.msgBox)
        menuBar.add_cascade(label='Help', menu=helpMenu)


    # Message box callback
    def msgBox(self):
        mbox.showinfo('Python Message Info Box',
            'A Pyton GUI created using tkinter:\nThe year is 2016.')
    
    
    # File->Exit callback
    def quit(self):
        self.win.quit()
        self.win.destroy()
        exit()
    
    
    # Spinbox callback
    def _spin(self):
        value = self.spin.get()
        print(value)
        self.scr.insert(tk.INSERT, value + '\n')

    
    # Radiobutton callback
    def radCall(self):
        radSel = self.radVar.get()
        self.monty2.configure(text=radSel)
    
    
    # Button click callback
    def clickMe(self):
        self.action.configure(
            text='Hello ' + self.name.get() + ' ' + self.number.get())


if __name__ == '__main__':
    oop = OOP()
    oop.win.mainloop()

