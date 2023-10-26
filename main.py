import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random

class RealTimeSpaceData(ThemedTk):

    def __init__(self):
        super().__init__()

        # Using a modern theme
        self.set_theme("arc")

        self.title("Real-time Space Data")
        self.geometry("900x600")

        # Create a frame for better arrangement
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(pady=20, padx=20, expand=True, fill="both")

        # Data initialization
        self.time_data = list(range(10))
        self.temperature_data = [random.randint(0, 100) for _ in range(10)]
        self.air_movement = {'North': 0, 'East': 0, 'South': 0, 'West': 0}

        # Line chart for temperature
        self.temp_fig, self.temp_ax = plt.subplots(figsize=(5, 4))
        self.temp_canvas = FigureCanvasTkAgg(self.temp_fig, self.main_frame)
        self.temp_canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10)

        # Pie chart for air movement
        self.air_fig, self.air_ax = plt.subplots(figsize=(5, 4))
        self.air_canvas = FigureCanvasTkAgg(self.air_fig, self.main_frame)
        self.air_canvas.get_tk_widget().grid(row=0, column=1, padx=10, pady=10)

        self.update_charts()

    def update_charts(self):

        # Simulate new data
        self.time_data.append(self.time_data[-1] + 1)
        self.temperature_data.append(self.temperature_data[-1] + random.randint(-2, 2))
        movement = random.choice(['North', 'East', 'South', 'West'])
        self.air_movement[movement] += 1

        # Update temperature chart
        self.temp_ax.clear()
        self.temp_ax.plot(self.time_data[-10:], self.temperature_data[-10:])
        self.temp_ax.set_title("Temperature over Time")
        self.temp_ax.set_xlabel("Time")
        self.temp_ax.set_ylabel("Temperature (°C)")

        # Update air movement pie chart
        self.air_ax.clear()
        self.air_ax.pie(self.air_movement.values(), labels=self.air_movement.keys(), autopct='%1.1f%%', startangle=90)
        self.air_ax.set_title("Air Movement Directions")

        self.temp_canvas.draw()
        self.air_canvas.draw()

        # Schedule next update
        self.after(1000, self.update_charts)


if __name__ == "__main__":
    app = RealTimeSpaceData()
    app.mainloop()
