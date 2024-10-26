import tkinter as tk
from PIL import ImageTk

class ImageArea(tk.Frame):
    def __init__(self, parent):
        super().__init__(width=512, height=512)
        self._parent = parent
        self.pack(side=tk.LEFT, expand=False)

    def paint_mandelbrot_image(self, ph: ImageTk.PhotoImage):
        for widget in self.winfo_children():
            widget.destroy()
        mandelbrot_image = tk.Label(self, image=ph)
        mandelbrot_image.image = ph
        mandelbrot_image.pack()