from tkinter import *
from tkinter import ttk


class ScreenFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.screen_frame = ttk.Frame(master, padding="1 1 1 30")
        self.screen_frame.grid(column=0, row=0)

        self.function_label = ttk.Label(self.screen_frame, font=("Courier", 12))
        self.function_label.grid()

        self.screen_label = ttk.Label(self.screen_frame, text="0", font=("Courier", 18))
        self.screen_label.grid()

    def add_value(self, value):
        prev_text = self.screen_label.cget("text")

        if prev_text == "0" and value == 0:
            return

        if prev_text == "0":
            prev_text = ""
        self.screen_label.config(text=f"{prev_text}{value}")

    def add_operator(self, operator):
        prev_text = self.screen_label.cget("text")

        if prev_text.strip()[-1] in ["+", "-", "/", "*"]:
            return
        else:
            self.screen_label.config(text=f"{prev_text} {operator} ")

    def get_function_label(self):
        return self.function_label.cget("text")

    def set_function_label(self, value):
        self.function_label.config(text=value)

    def get_screen_label(self):
        return self.screen_label.cget("text")

    def set_screen_label(self, value):
        self.screen_label.config(text=value)
