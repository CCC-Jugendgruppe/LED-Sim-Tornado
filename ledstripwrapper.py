"""
Wrapper for the LED strips to make them easier to use.
"""
import tkinter as tk

class LEDStripWrapper(tk.Frame):
    def __init__(self, master, column_num: int, leds_per_column: int, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.column_num = column_num
        self.leds_per_column = leds_per_column
