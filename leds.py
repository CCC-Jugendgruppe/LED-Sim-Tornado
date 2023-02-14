"""
enthält die LED Klasse
"""
import tkinter as tk

class LED(tk.Canvas):
    """
    LED Klasse für das Anzeigen von den LEDs
    """
    def __init__(self, frame, color):
        super().__init__(frame, width=20, height=20, bg=color)


class LEDStrip(tk.Frame):
    """
    LED Strip Klasse, um die LEDs zu verwalten
    """
    def __init__(self, frame, num_leds: int = 0, *args, **kwargs):
        super().__init__(frame, *args, **kwargs)
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


class LEDStripWrapper(tk.Frame):
    def __init__(self, master, column_count: int, leds_per_column: int, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.column_num = column_count
        self.leds_per_column = leds_per_column
        self.led_strips = []
        # creates array of LED strips
        for _ in range(column_count):
            for i in range(leds_per_column):
                led_strip = LEDStrip(self, leds_per_column)
                self.led_strips.append(led_strip)

    def pack(self, *args, **kwargs):
        # packs the LED strips
        for strip in self.led_strips:
            strip.pack()

        # packs self
        super().pack(*args, **kwargs)

    def update_all(self, color):
        for strip in self.led_strips:
            strip.update_all(color)
