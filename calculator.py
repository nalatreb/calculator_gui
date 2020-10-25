from tkinter import *
from tkinter import ttk

from screen_frame import ScreenFrame


class Calculator(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.erase = False
        self.master.title('Sample Application')
        self.grid()
        self.mainframe = ttk.Frame(self, padding="30")
        self.mainframe.grid(column=0, row=0)
        self.screen_frame = ScreenFrame(self.mainframe)

        self.button_frame = ttk.Frame(self.mainframe)
        self.button_frame.grid(column=0, row=1)
        self.create_widget()
        self.items = []

    def add_value_to_screen(self, value):
        if self.erase:
            self.reset_calculator()
        self.screen_frame.add_value(value)

    def add_operator_to_screen(self, operator):
        if self.erase:
            self.erase = False
        self.screen_frame.add_operator(operator)

    def reset_calculator(self):
        self.erase = False
        self.screen_frame.set_screen_label("0")
        self.screen_frame.set_function_label("")

    def set_items(self):
        operators = ["+", "-", "*", "/"]

        text = self.screen_frame.get_screen_label()
        self.screen_frame.set_function_label(text)
        text = text.replace(" ", "")
        for x in text:
            if len(self.items) == 0:
                self.items.append(int(x))
            elif x in operators:
                self.items.append(x)
            elif self.items[len(self.items) - 1] in operators:
                self.items.append(int(x))
            else:
                self.items[len(self.items) - 1] = int(f'{self.items[len(self.items) - 1]}{x}')

        if self.items[len(self.items) - 1] in operators:
            self.items = self.items[:-1]

    def get_result(self):
        self.set_items()

        if len(self.items) < 3:
            return self.items[0]

        while "*" in self.items or "/" in self.items:
            index = 1
            for x in self.items[1:]:
                if x == "/" and self.items[index + 1] == 0:
                    return "error"
                index = self.handle_arithmetic(["*", "/"], index, x)

        if len(self.items) == 1:
            return self.items[0]

        while "+" in self.items or "-" in self.items:
            index = 1
            for x in self.items[1:]:
                index = self.handle_arithmetic(["+", "-"], index, x)

        return self.items[0]

    def handle_arithmetic(self, arithmetics, index, value):
        if value in arithmetics:
            exec(f"self.items[index - 1] = self.items[index - 1] {value} self.items[index + 1]")
            del (self.items[index + 1])
            del (self.items[index])
            index -= 2
        index += 1
        return index

    def calculate(self):
        self.erase = True
        result = self.get_result()
        self.items = []
        self.screen_frame.set_screen_label(f"{result}")

    def create_widget(self):
        ttk.Button(self.button_frame, text="+", command=lambda: self.add_operator_to_screen("+")).grid(row=0, column=3)
        ttk.Button(self.button_frame, text="-", command=lambda: self.add_operator_to_screen("-")).grid(row=0, column=2)
        ttk.Button(self.button_frame, text="*", command=lambda: self.add_operator_to_screen("*")).grid(row=0, column=1)
        ttk.Button(self.button_frame, text="/", command=lambda: self.add_operator_to_screen("/")).grid(row=0, column=0)
        ttk.Button(self.button_frame, text="C", command=self.reset_calculator).grid(row=1, column=3)
        ttk.Button(self.button_frame, text="=", padding="1 27 1 25", command=self.calculate).grid(row=2, column=3,
                                                                                                  rowspan=3)

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
