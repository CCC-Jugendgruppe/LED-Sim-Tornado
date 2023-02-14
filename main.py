"""
Der LED-Simulator ist ein Simulator um die Effekte für den Tornado zu testen.
"""
from simulator import Simulator

if __name__ == "__main__":
    app = Simulator(amount_columns=3, leds_per_column=7)
    app.run()
