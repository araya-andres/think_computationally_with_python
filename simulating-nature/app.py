import math
import tkinter as tk

import grid


class App:
    """Main class"""

    def __init__(self):
        # Make the tkinter window.
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("1000x1000")

        self.canvas = tk.Canvas(self.window, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.update()

        self.draw()

        self.window.focus_force()
        self.window.mainloop()

    def kill_callback(self):
        """A callback to destroy the tkinter window."""
        self.window.destroy()

    def draw(self):
        # Remove any previous widgets.
        self.canvas.delete("all")
        grid.draw(self.canvas, 20)


App()
