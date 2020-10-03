from tkinter import *
from tkinter import ttk


class Calculator(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Sample Application')
        self.grid()
        self.mainframe = ttk.Frame(self, padding="30")
        self.mainframe.grid(column=0, row=0)
        self.screen_frame = ttk.Frame(self.mainframe, padding="1 1 1 30")
        self.screen_frame.grid(column=0, row=0)

        self.function_label = ttk.Label(self.screen_frame)
        self.function_label.grid()

        self.screen_label = ttk.Label(self.screen_frame, text="0")
        self.screen_label.grid()

        self.button_frame = ttk.Frame(self.mainframe)
        self.button_frame.grid(column=0, row=1)
        self.create_widget()

    def add_value_to_screen(self, value):
        prev_text = self.screen_label.cget("text")

        if prev_text == "0" and value == 0:
            return

        if prev_text == "0":
            prev_text = ""
        self.screen_label.config(text=f"{prev_text}{value}")

    def add_operator_to_screen(self, operator):
        prev_text = self.screen_label.cget("text")

        if prev_text.strip()[-1] in ["+", "-", "/", "*"]:
            return
        else:
            self.screen_label.config(text=f"{prev_text} {operator} ")

    def reset_calculator(self):
        self.screen_label.config(text="0")
        self.function_label.config(text="")

    def get_items(self):
        items = []
        operators = ["+", "-", "*", "/"]

        text = self.screen_label.cget("text")
        self.function_label.config(text=text)
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

    def get_result(self):
        items = self.get_items()

        if len(items) < 3:
            return items[0]

        while "*" in items or "/" in items:
            index = 1
            for x in items[1:]:
                if x == "*":
                    items[index - 1] = items[index - 1] * items[index + 1]
                    del (items[index + 1])
                    del (items[index])
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
                    del (items[index + 1])
                    del (items[index])
                    index -= 2
                elif x == "-":
                    items[index - 1] = items[index - 1] - items[index + 1]
                    del (items[index + 1])
                    del (items[index])
                    index -= 2
                index += 1
        return items[0]

    def calculate(self):
        result = self.get_result()
        self.screen_label.config(text=f"{result}")

    def create_widget(self):
        ttk.Button(self.button_frame, text="+", command=lambda: self.add_operator_to_screen("+")).grid(row=0, column=3)
        ttk.Button(self.button_frame, text="-", command=lambda: self.add_operator_to_screen("-")).grid(row=0, column=2)
        ttk.Button(self.button_frame, text="*", command=lambda: self.add_operator_to_screen("*")).grid(row=0, column=1)
        ttk.Button(self.button_frame, text="/", command=lambda: self.add_operator_to_screen("/")).grid(row=0, column=0)
        ttk.Button(self.button_frame, text="C", command=self.reset_calculator).grid(row=1, column=3)
        ttk.Button(self.button_frame, text="=", padding="1 27 1 25", command=self.calculate).grid(row=2, column=3, rowspan=3)

        ttk.Button(self.button_frame, text="0", command=lambda: self.add_value_to_screen(0), padding="77 1 77 1") \
            .grid(row=4, column=0, columnspan=3)
        ttk.Button(self.button_frame, text="1", command=lambda: self.add_value_to_screen(1)).grid(row=1, column=0)
        ttk.Button(self.button_frame, text="2", command=lambda: self.add_value_to_screen(2)).grid(row=1, column=1)
        ttk.Button(self.button_frame, text="3", command=lambda: self.add_value_to_screen(3)).grid(row=1, column=2)
        ttk.Button(self.button_frame, text="4", command=lambda: self.add_value_to_screen(4)).grid(row=2, column=0)
        ttk.Button(self.button_frame, text="5", command=lambda: self.add_value_to_screen(5)).grid(row=2, column=1)
        ttk.Button(self.button_frame, text="6", command=lambda: self.add_value_to_screen(6)).grid(row=2, column=2)
        ttk.Button(self.button_frame, text="7", command=lambda: self.add_value_to_screen(7)).grid(row=3, column=0)
        ttk.Button(self.button_frame, text="8", command=lambda: self.add_value_to_screen(8)).grid(row=3, column=1)
        ttk.Button(self.button_frame, text="9", command=lambda: self.add_value_to_screen(9)).grid(row=3, column=2)


app = Calculator()
app.mainloop()
