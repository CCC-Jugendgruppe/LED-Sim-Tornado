import tkinter as tk
from tkinter import ttk
from ledstrip import LEDStrip
from led import LED

class Simulator(tk.Tk):
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
        for i in range(self.led_strip.leds):
            self.led_strip.leds[i].config(bg="red")
        self.mainloop()
