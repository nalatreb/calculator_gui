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
    function_label.config(text="")


def get_items():
    items = []
    operators = ["+", "-", "*", "/"]

    text = screen_label.cget("text")
    function_label.config(text=text)
    text = text.replace(" ", "")
    for x in text:
        if len(items) == 0:
            items.append(int(x))
        elif x in operators:
            items.append(x)
        elif items[len(items) - 1] in operators:
            items.append(int(x))
        else:
            items[len(items) - 1] = int(f'{items[len(items) - 1]}{x}')

    if items[len(items) - 1] in operators:
        items = items[:-1]

    return items


def get_result():
    items = get_items()

    if len(items) < 3:
        return items[0]

    while "*" in items or "/" in items:
        index = 1
        for x in items[1:]:
            if x == "*":
                items[index - 1] = items[index - 1] * items[index + 1]
                del(items[index + 1])
                del(items[index])
                index -= 2
            elif x == "/":
                if items[index + 1] == 0:
                    return "error"
                items[index - 1] = items[index - 1] / items[index + 1]
                del (items[index + 1])
                del (items[index])
                index -= 2
            index += 1

    if len(items) == 1:
        return items[0]

    while "+" in items or "-" in items:
        index = 1
        for x in items[1:]:
            if x == "+":
                items[index - 1] = items[index - 1] + items[index + 1]
                del(items[index + 1])
                del(items[index])
                index -= 2
            elif x == "-":
                items[index - 1] = items[index - 1] - items[index + 1]
                del (items[index + 1])
                del (items[index])
                index -= 2
            index += 1
    return items[0]


def calculate():
    result = get_result()
    screen_label.config(text=f"{result}")


root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="30")
mainframe.grid(column=0, row=0)

screen_frame = ttk.Frame(mainframe, padding="1 1 1 30")
screen_frame.grid(column=0, row=0)

function_label = ttk.Label(screen_frame)
function_label.grid()

screen_label = ttk.Label(screen_frame, text="0")
screen_label.grid()

button_frame = ttk.Frame(mainframe)
button_frame.grid(column=0, row=1)


ttk.Button(button_frame, text="+", command=lambda: add_operator_to_screen("+")).grid(row=0, column=3)
ttk.Button(button_frame, text="-", command=lambda: add_operator_to_screen("-")).grid(row=0, column=2)
ttk.Button(button_frame, text="*", command=lambda: add_operator_to_screen("*")).grid(row=0, column=1)
ttk.Button(button_frame, text="/", command=lambda: add_operator_to_screen("/")).grid(row=0, column=0)
ttk.Button(button_frame, text="C", command=reset_calculator).grid(row=1, column=3)
ttk.Button(button_frame, text="=", padding="1 27 1 25", command=calculate).grid(row=2, column=3, rowspan=3)

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

