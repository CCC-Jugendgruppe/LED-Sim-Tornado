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
