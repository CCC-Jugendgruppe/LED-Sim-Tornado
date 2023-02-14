"""
Simulator-Fenster für den LED-Strip
"""
import tkinter as tk
from tkinter import ttk
from leds import *

class Simulator(tk.Tk):
    """
    Simulator-Fenster für den LED-Strip und der Funktionalität
    """
    def __init__(self):
        super().__init__()
        ttk.Style().theme_use("clam")
        self.title("Simulator")
        self.geometry("800x600")
        self.resizable(False, False)

        self.frame = tk.Frame(self)

        self.led_strip = LEDStripWrapper(self.frame, leds_per_column=7, column_count=3)

        self.button = ttk.Button(self.frame, text="change color", command=lambda: self.led_strip.update_all("green"))
        self.button.pack()


        self.frame.pack(fill=tk.BOTH, expand=True)


    def run(self):
        """
        Startet den Simulator
        """
        self.led_strip.pack(fill=tk.BOTH, expand=True)
        self.mainloop()
