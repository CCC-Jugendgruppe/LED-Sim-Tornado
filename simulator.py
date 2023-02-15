"""
Simulator for the LED-Strips
"""
import tkinter as tk
from tkinter import ttk
from led import LEDStripsManager

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

        self.mgr = LEDStripsManager(self.frame,
                                    amount_columns=amount_columns,
                                    leds_per_column=leds_per_column)
        btn = ttk.Button(self,
                         text="effekt ausführen",
                         command=lambda: self.mgr.run_effect("rainbow"))
        btn.pack(side="top")
