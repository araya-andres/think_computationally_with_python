import tkinter as tk


def draw(canvas: tk.Canvas, size, color="gray95"):
    w = canvas.winfo_width()
    h = canvas.winfo_height()
    space_x = w / size
    for x in range(0, size + 1):
        pos_x = x * space_x
        canvas.create_line(pos_x, 0, pos_x, h, fill=color)
    space_y = h / size
    for y in range(0, size + 1):
        pos_y = y * space_y
        canvas.create_line(0, pos_y, w, pos_y, fill=color)
