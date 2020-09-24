from tkinter import *
from tkinter import ttk


def add_value_to_screen(value):
    prev_text = screen_label.cget("text")

    if prev_text == "0" and value == 0:
        return

    if prev_text == "0":
        prev_text = ""
    screen_label.config(text=f"{prev_text}{value}")


def add_operator_to_screen(operator):
    prev_text = screen_label.cget("text")

    if prev_text.strip()[-1] in ["+", "-", "/", "*"]:
        return
    else:
        screen_label.config(text=f"{prev_text} {operator} ")


def reset_calculator():
    screen_label.config(text="0")


root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="30")
mainframe.grid(column=0, row=0)

screen_frame = ttk.Frame(mainframe, padding="1 1 1 30")
screen_frame.grid(column=0, row=0)

screen_var = "0"

screen_label = ttk.Label(screen_frame, text=screen_var)
screen_label.grid()

button_frame = ttk.Frame(mainframe)
button_frame.grid(column=0, row=1)


ttk.Button(button_frame, text="+", command=lambda: add_operator_to_screen("+")).grid(row=0, column=3)
ttk.Button(button_frame, text="-", command=lambda: add_operator_to_screen("-")).grid(row=0, column=2)
ttk.Button(button_frame, text="*", command=lambda: add_operator_to_screen("*")).grid(row=0, column=1)
ttk.Button(button_frame, text="/", command=lambda: add_operator_to_screen("/")).grid(row=0, column=0)
ttk.Button(button_frame, text="C", command=reset_calculator).grid(row=1, column=3)
ttk.Button(button_frame, text="=", padding="1 27 1 25").grid(row=2, column=3, rowspan=3)

ttk.Button(button_frame, text="0", command=lambda: add_value_to_screen(0), padding="77 1 77 1")\
    .grid(row=4, column=0, columnspan=3)
ttk.Button(button_frame, text="1", command=lambda: add_value_to_screen(1)).grid(row=1, column=0)
ttk.Button(button_frame, text="2", command=lambda: add_value_to_screen(2)).grid(row=1, column=1)
ttk.Button(button_frame, text="3", command=lambda: add_value_to_screen(3)).grid(row=1, column=2)
ttk.Button(button_frame, text="4", command=lambda: add_value_to_screen(4)).grid(row=2, column=0)
ttk.Button(button_frame, text="5", command=lambda: add_value_to_screen(5)).grid(row=2, column=1)
ttk.Button(button_frame, text="6", command=lambda: add_value_to_screen(6)).grid(row=2, column=2)
ttk.Button(button_frame, text="7", command=lambda: add_value_to_screen(7)).grid(row=3, column=0)
ttk.Button(button_frame, text="8", command=lambda: add_value_to_screen(8)).grid(row=3, column=1)
ttk.Button(button_frame, text="9", command=lambda: add_value_to_screen(9)).grid(row=3, column=2)
root.mainloop()

