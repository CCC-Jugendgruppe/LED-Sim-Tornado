import tkinter as tk

class LED(tk.Canvas):
    def __init__(self, frame, color):
        super().__init__(frame, width=width, height=height, bg=color)
