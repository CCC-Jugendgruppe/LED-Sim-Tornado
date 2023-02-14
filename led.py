import tkinter as tk
from tkinter import ttk

class LED(tk.Canvas):
    def __init__(self, master, color="red", **kwargs):
        super().__init__(master, height=20, width=20, **kwargs, bg=color)

    def set_color(self, color):
        self.config(bg=color)


class LEDStrip(ttk.Frame):
    def __init__(self, master, amount_leds=10, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.leds = []
        for i in range(amount_leds):
            led = LED(self)
            led.grid(row=i, column=0)
            self.leds.append(led)

    def set_all_color(self, color):
        for led in self.leds:
            led.set_color(color)

    def set_color(self, index, color):
        self.leds[index].set_color(color)


class LEDStripsManager(ttk.Frame):
    def __init__(self, master, amount_columns, leds_per_column):
        for i in range(amount_columns):
            master.columnconfigure(i, weight=1)
        master.rowconfigure(0, weight=1)

        self.strips = []

        for i in range(amount_columns):
            strip = LEDStrip(master, amount_leds=leds_per_column)
            strip.grid(row=0, column=i)
            self.strips.append(strip)