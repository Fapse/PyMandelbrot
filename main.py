import tkinter as tk
from PIL import ImageTk
from PIL.ImageOps import expand

from mandelbrot import Mandelbrot

class MandelbrotWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyMandelbrot")
        self._frame_mandelbrot_image = tk.Frame(master=self, width=512, height=512)
        self._frame_mandelbrot_image.pack(side=tk.LEFT, expand=False)
        self._frame_control_area = tk.Frame(master=self)
        self._frame_control_area.pack(side=tk.LEFT, expand=False)
        self._frame_pan_buttons = tk.Frame(master=self._frame_control_area)
        self._frame_zoom_buttons = tk.Frame(master=self._frame_control_area)
        self._frame_go_reset_buttons = tk.Frame(master=self._frame_control_area)
        self._my_mandelbrot = Mandelbrot()
        self._request_mandelbrot_image()
        self._create_buttons()

    def _request_mandelbrot_image(self):
        ph = ImageTk.PhotoImage(self._my_mandelbrot.create_mandelbrot())
        for widget in self._frame_mandelbrot_image.winfo_children():
            widget.destroy()
        mandelbrot_image = tk.Label(self._frame_mandelbrot_image, image=ph)
        mandelbrot_image.image = ph
        mandelbrot_image.pack()

    def _up_click(self):
        print("Up clicked")
        self._my_mandelbrot.move_up()

    def _left_click(self):
        print("Left clicked")
        self._my_mandelbrot.move_left()

    def _right_click(self):
        print("Right clicked")
        self._my_mandelbrot.move_right()

    def _down_click(self):
        print("Down clicked")
        self._my_mandelbrot.move_down()

    def _plus_click(self):
        print("Plus clicked")
        self._my_mandelbrot.zoom_in()

    def _minus_click(self):
        print("Minus clicked")
        self._my_mandelbrot.zoom_out()

    def _go_click(self):
        print("Go clicked")
        self._request_mandelbrot_image()

    def _create_buttons(self):
        #display_frame = tk.Frame(master=self)
        button1=tk.Button(self._frame_pan_buttons, text="U", command=self._up_click)
        button1.grid(row=0, column=1)
        button2=tk.Button(self._frame_pan_buttons, text="L", command=self._left_click)
        button2.grid(row=1, column=0)
        button3=tk.Button(self._frame_pan_buttons, text="R", command=self._right_click)
        button3.grid(row=1, column=2)
        button4=tk.Button(self._frame_pan_buttons, text="D", command=self._down_click)
        button4.grid(row=2, column=1)
        self._frame_pan_buttons.pack()
        button5=tk.Button(self._frame_zoom_buttons, text="-", command=self._minus_click)
        button5.grid(row=0, column=0)
        button6=tk.Button(self._frame_zoom_buttons, text="+", command=self._plus_click)
        button6.grid(row=0, column=1)
        self._frame_zoom_buttons.pack()
        button6=tk.Button(self._frame_go_reset_buttons, text="GO", command=self._go_click)
        button6.grid(row=0, column=0)
        self._frame_go_reset_buttons.pack()
        #display_frame.pack(side=tk.LEFT, expand=False)

if __name__ == "__main__":
    mb_window = MandelbrotWindow()
    mb_window.mainloop()