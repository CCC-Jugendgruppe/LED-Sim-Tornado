"""
LED Logik
"""
import time
import tkinter as tk
from tkinter import ttk
from util import rgb_perc

class LED(tk.Canvas):
    """
    Repräsentiert eine LED
    """
    def __init__(self, master, color="black", **kwargs):
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
        self.amount_leds = amount_columns * leds_per_column

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

    def set_led(self, index, color):
        """ setzt eine LED auf eine bestimmte Farbe """
        strip_index = index // self.leds_per_column
        led_index = index % self.leds_per_column
        self.strips[strip_index].set_color(led_index, color)

    def run_effect(self, effect: str):
        """
        Führt einen Effekt aus
        """
        match effect:
            case "rainbow":
                for i in range(self.amount_columns):
                    for j in range(self.leds_per_column):
                        self.strips[i].set_color(j, rgb_perc(10, 40, 50))
            case "main":
                blue = True
                while True:
                    for i in range(100):
                        for j in range(self.amount_columns):
                            if not blue:
                                self.strips[j].set_color(i, rgb_perc(0, 0, 100))
                                self.set_led(i, rgb_perc(0, 0, 100))
                                blue = True
                            else:
                                self.strips[j].set_color(i, rgb_perc(0, 0, 0))
                                blue = False
                            time.sleep(0.1)
                            self.update()
            case "testing":
                for i in range(self.amount_leds):
                    self.set_led(i, rgb_perc(0, 0, 100))
                    time.sleep(0.1)
                    self.update()

            case _:
                pass
