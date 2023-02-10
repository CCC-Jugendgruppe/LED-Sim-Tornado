import tkinter as tk

class LED(tk.Canvas):
    def __init__(self, frame, color):
        super().__init__(frame, width=20, height=20, bg=color)
