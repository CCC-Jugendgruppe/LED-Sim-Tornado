"""
Simulator-Fenster für den LED-Strip
"""
import tkinter as tk
from tkinter import ttk
from ledstrip import LEDStrip

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
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.button = ttk.Button(self.frame, text="Click Me")
        self.button.pack()

        self.led_strip = LEDStrip(self.frame, 21)


    def run(self):
        """
        Startet den Simulator
        """
        self.led_strip.update_all("red")
        self.mainloop()
