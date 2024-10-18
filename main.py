import tkinter as tk
from tkinter import font
from PIL import ImageTk
from mandelbrot import Mandelbrot

class MandelbrotWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyMandelbrot")
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

    def _up_click(self):
        print("Up clicked")

    def _left_click(self):
        print("Left clicked")

    def _right_click(self):
        print("Right clicked")

    def _down_click(self):
        print("Down clicked")

    def _plus_click(self):
        print("Plus clicked")

    def _minus_click(self):
        print("Minus clicked")

    def _go_click(self):
        print("Minus clicked")

    def _create_buttons(self):
        display_frame = tk.Frame(master=self)
        button1=tk.Button(display_frame, text="U", command=self._up_click)
        button1.grid(row=0, column=1)
        button2=tk.Button(display_frame, text="L", command=self._left_click)
        button2.grid(row=1, column=0)
        button3=tk.Button(display_frame, text="R", command=self._right_click)
        button3.grid(row=1, column=2)
        button4=tk.Button(display_frame, text="D", command=self._down_click)
        button4.grid(row=2, column=1)
        button5=tk.Button(display_frame, text="-", command=self._minus_click)
        button5.grid(row=3, column=0)
        button6=tk.Button(display_frame, text="+", command=self._plus_click)
        button6.grid(row=3, column=2)
        button6=tk.Button(display_frame, text="GO", command=self._go_click)
        button6.grid(row=4, column=1)

        display_frame.pack(side=tk.LEFT, expand=False)

if __name__ == "__main__":
    mb_window = MandelbrotWindow()
    mb_window.mainloop()