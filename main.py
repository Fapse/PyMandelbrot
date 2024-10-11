import tkinter as tk
from PIL import Image, ImageTk
import mandelbrot

def show_window():
    window = tk.Tk()
    ph = ImageTk.PhotoImage(mandelbrot.create_mandelbrot())
    mandel_img = tk.Label(window, image=ph)
    mandel_img.image = ph
    greeting = tk.Label(text='Hello, Tkinter')
    greeting.pack()
    mandel_img.pack()
    window.mainloop()

if __name__ == "__main__":
    show_window()