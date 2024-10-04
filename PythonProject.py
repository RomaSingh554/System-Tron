import tkinter as tk
import math
import time


class PythonProject:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Analog Clock")
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="black")  # Dark background for better contrast
        self.canvas.pack()

        # Clock settings
        self.clock_radius = 180
        self.hour_hand_length = self.clock_radius * 0.7
        self.minute_hand_length = self.clock_radius * 0.8
        self.second_hand_length = self.clock_radius * 0.9
        self.number_radius = self.clock_radius * 0.85

        # Create clock face
        self.canvas.create_oval(200 - self.clock_radius, 200 - self.clock_radius,
                                200 + self.clock_radius, 200 + self.clock_radius)

        # Draw hour marks and numbers
        for i in range(1, 13):
            angle = i * 30 * math.pi / 180
            x = 200 + math.cos(angle) * self.clock_radius * 0.9
            y = 200 - math.sin(angle) * self.clock_radius * 0.9
            self.canvas.create_line(200, 200, x, y, fill="white")
            self.canvas.create_text(x, y, text=str(i), fill="white", font=("Arial", 12))

        # Start clock updates
        self.update_clock()

    def update_clock(self):
        now = time.localtime()

        # Draw clock hands
        hour_angle = (now.tm_hour % 12 + now.tm_min / 60) * 30 * math.pi / 180
        minute_angle = now.tm_min * 6 * math.pi / 180
        second_angle = now.tm_sec * 6 * math.pi / 180

        self.canvas.create_line(200, 200,
                                200 + math.cos(hour_angle) * self.hour_hand_length,
                                200 - math.sin(hour_angle) * self.hour_hand_length,
                                fill="white", width=3)
        self.canvas.create_line(200, 200,
                                200 + math.cos(minute_angle) * self.minute_hand_length,
                                200 - math.sin(minute_angle) * self.minute_hand_length,
                                fill="white", width=2)
        self.canvas.create_line(200, 200,
                                200 + math.cos(second_angle) * self.second_hand_length,
                                200 - math.sin(second_angle) * self.second_hand_length,
                                fill="red", width=1)

        # Update clock display
        self.root.after(20, self.update_clock)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    clock = PythonProject()
    clock.run()
