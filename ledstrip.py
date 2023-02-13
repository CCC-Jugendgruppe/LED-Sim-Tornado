"""
enthält LED Strip Klasse
"""
from led import LED
import tkinter as tk

class LEDStrip(tk.Frame):
    """
    LED Strip Klasse, um die LEDs zu verwalten
    """
    def __init__(self, frame, num_leds: int = 0, from_array: list = []):
        self.frame = frame
        self.num_leds = num_leds
        self.leds = []
        self.create_leds()

    def create_leds(self):
        """
        Erstellt array aus beschreibbaren LED Objekten
        """
        for _ in range(self.num_leds):
            led = LED(self.frame, "black")
            led.pack()
            self.leds.append(led)

    def update_all(self, color):
        """
        Setzt alle LEDs auf eine Farbe
        """
        for i in range(self.num_leds):
            self.leds[i].config(bg=color)

    def update(self, index, color):
        """
        Setzt bestimmte LED auf eine Farbe
        """
        self.leds[index].config(bg=color)
