"""
Wrapper for the LED strips to make them easier to use.
"""
import tkinter as tk

class LEDStripWrapper(tk.Frame):
    def __init__(self, master, strip, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.strip = strip
        self.leds = []
