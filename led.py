"""
LED Logik
"""
import tkinter as tk
from tkinter import ttk
from util import rgb_perc

class LED(tk.Canvas):
    """
    Repräsentiert eine LED
    """
    def __init__(self, master, color="red", **kwargs):
        super().__init__(master, height=20, width=20, **kwargs, bg=color)

    def set_color(self, color):
        """
        Setzt die Farbe der LED
        """
        self.config(bg=color)


class LEDStrip(ttk.Frame):
    """
    Repräsentiert eine LED-Streifen
    """
    def __init__(self, master, amount_leds=10, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.leds = []
        for i in range(amount_leds):
            led = LED(self)
            led.grid(row=i, column=0)
            self.leds.append(led)

    def set_all(self, color):
        """
        Setzt alle LEDs auf die gleiche Farbe
        """
        for led in self.leds:
            led.set_color(color)

    def set_color(self, index, color):
        """
        Setzt die Farbe einer bestimmten LED
        """
        self.leds[index].set_color(color)


class LEDStripsManager(ttk.Frame):
    """
    Manager für mehrere LED-Streifen
    """
    def __init__(self, master, amount_columns, leds_per_column):
        super().__init__(master)
        self.amount_columns = amount_columns
        self.leds_per_column = leds_per_column
        self.master = master
        for i in range(amount_columns):
            master.columnconfigure(i, weight=1)
        master.rowconfigure(0, weight=1)

        self.strips = []

        for i in range(amount_columns):
            strip = LEDStrip(master, amount_leds=leds_per_column)
            strip.grid(row=0, column=i)
            self.strips.append(strip)


    def set_all(self, color):
        """
        Setzt alle LEDs auf die gleiche Farbe
        """
        for strip in self.strips:
            strip.set_all(color)

    def run_effect(self, effect: str):
        """
        Führt einen Effekt aus
        """
        match effect:
            case "rainbow":
                for i in range(self.amount_columns):
                    for j in range(self.leds_per_column):
                        self.strips[i].set_color(j, rgb_perc(10, 40, 50)) # perc / 100 * 255
            case _:
                pass
