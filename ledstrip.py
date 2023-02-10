from led import LED

class LEDStrip():
    def __init__(self, frame, num_leds):
        self.frame = frame
        self.num_leds = num_leds
        self.leds = []
        self.create_leds()

    def create_leds(self):
        for i in range(self.num_leds):
            led = LED(self.frame, "black")
            led.pack()
            self.leds.append(led)

    def update_all(self, color):
        for i in range(self.num_leds):
            self.leds[i].config(bg=color)

    def update(self, index, color):
        self.leds[index].config(bg=color)
