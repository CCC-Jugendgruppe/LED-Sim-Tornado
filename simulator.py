"""
Simulator-Fenster für den LED-Strip
"""
import tkinter as tk
from tkinter import ttk
from ledstripwrapper import LEDStripWrapper

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

        self.button = ttk.Button(self.frame, text="change color")#, command=lambda: self.led_strip.update_all("green"))
        self.button.pack()

        self.led_strip = LEDStripWrapper(self.frame, 21)

        self.frame.pack(fill=tk.BOTH, expand=True)


    def run(self):
        """
        Startet den Simulator
        """
        # self.led_strip.update_all("red")
        self.mainloop()
