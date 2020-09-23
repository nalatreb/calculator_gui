from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="30")
mainframe.grid(column=0, row=0)

ttk.Button(mainframe, text="1").grid()
ttk.Button(mainframe, text="2").grid(row=0, column=1)
ttk.Button(mainframe, text="3").grid(row=0, column=2)
ttk.Button(mainframe, text="4").grid(row=1, column=0)
ttk.Button(mainframe, text="5").grid(row=1, column=1)
ttk.Button(mainframe, text="6").grid(row=1, column=2)
ttk.Button(mainframe, text="7").grid(row=2, column=0)
ttk.Button(mainframe, text="8").grid(row=2, column=1)
ttk.Button(mainframe, text="9").grid(row=2, column=2)
root.mainloop()
