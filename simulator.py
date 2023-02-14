import tkinter as tk
from led import LEDStripsManager
from tkinter import ttk

class Simulator(tk.Tk):
    """
    LED-Strip Simulator fenster
    """
    def __init__(self, amount_columns: int, leds_per_column: int):
        super().__init__()
        self.title("My App")
        self.geometry("500x500")
        self.resizable(False, False)

        # Create a frame
        self.frame = ttk.Frame(self)
        # split the frame into three parts next to each other
        self.frame.pack(side="top", fill="both", expand=True)

        self.mgr = LEDStripsManager(self.frame, amount_columns=amount_columns, leds_per_column=leds_per_column)
        btn = ttk.Button(self, text="farbe setzen", command=lambda: self.mgr.set_all("green"))
        btn.pack(side="top")
