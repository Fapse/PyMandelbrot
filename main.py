import tkinter as tk
from tkinter import font
from PIL import ImageTk
from mandelbrot import Mandelbrot

class MandelbrotWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyMandelbrot")
        #self._cells = {}
        self._create_mandelbrot_display()
        self._create_mandelbrot_image()
        self._create_buttons()

    def _create_mandelbrot_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Mandelbrot",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()

    def _create_mandelbrot_image(self):
        display_frame = tk.Frame(master=self)
        my_mandelbrot = Mandelbrot()
        ph = ImageTk.PhotoImage(my_mandelbrot.create_mandelbrot())
        mandel_img = tk.Label(display_frame, image=ph)
        mandel_img.image = ph
        mandel_img.pack()
        display_frame.pack(side=tk.LEFT, expand=False)
        self.display.pack()

    def _create_buttons(self):
        display_frame = tk.Frame(master=self)
        for x in range(3):
            for y in range(3):
                frame = tk.Frame(
                    master=display_frame,
                    relief=tk.RAISED,
                    borderwidth=1
                )
                frame.grid(row=y, column=x, padx=3, pady=3)
                label = tk.Label(master=frame, text=f"Row {y}\nColumn {x}")
                label.pack()
        display_frame.pack(side=tk.LEFT, expand=False)

if __name__ == "__main__":
    mb_window = MandelbrotWindow()
    mb_window.mainloop()