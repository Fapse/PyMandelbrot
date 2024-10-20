import tkinter as tk
from PIL import ImageTk
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
        self._frame_input_area = tk.Frame(master=self._frame_control_area)
        self._frame_go_reset_buttons = tk.Frame(master=self._frame_control_area)
        self._label1=tk.Label(self._frame_input_area, text="Pan step:")
        self._label1.grid(row=0, column=0)
        self._tf_pan_factor = tk.Entry(master=self._frame_input_area)
        self._tf_pan_factor.grid(row=1, column=0)
        self._label2=tk.Label(self._frame_input_area, text="Zoom step:")
        self._label2.grid(row=2, column=0)
        self._tf_zoom_factor=tk.Entry(master=self._frame_input_area)
        self._tf_zoom_factor.grid(row=3, column=0)
        self._label3 = tk.Label(self._frame_input_area, text="Max. iterations:")
        self._label3.grid(row=4, column=0)
        self._tf_max_iterations = tk.Entry(master=self._frame_input_area)
        self._tf_max_iterations.grid(row=5, column=0)
        self._my_mandelbrot = Mandelbrot()
        self._go_reset()
        self._create_buttons()

    def _request_mandelbrot_image(self):
        ph = ImageTk.PhotoImage(self._my_mandelbrot.create_mandelbrot(int(self._tf_max_iterations.get())))
        for widget in self._frame_mandelbrot_image.winfo_children():
            widget.destroy()
        mandelbrot_image = tk.Label(self._frame_mandelbrot_image, image=ph)
        mandelbrot_image.image = ph
        mandelbrot_image.pack()

    def _up_click(self):
        print("Up clicked")
        self._my_mandelbrot.move_up(float(self._tf_pan_factor.get()))

    def _left_click(self):
        print("Left clicked")
        self._my_mandelbrot.move_left(float(self._tf_pan_factor.get()))

    def _right_click(self):
        print("Right clicked")
        self._my_mandelbrot.move_right(float(self._tf_pan_factor.get()))

    def _down_click(self):
        print("Down clicked")
        self._my_mandelbrot.move_down(float(self._tf_pan_factor.get()))

    def _plus_click(self):
        print("Plus clicked")
        self._my_mandelbrot.zoom_in(float(self._tf_zoom_factor.get()))

    def _minus_click(self):
        print("Minus clicked")
        self._my_mandelbrot.zoom_out(float(self._tf_zoom_factor.get()))

    def _go_click(self):
        print("Go clicked")
        self._request_mandelbrot_image()

    def _go_reset(self):
        print("Reset clicked")
        self._tf_zoom_factor.delete(0,'end')
        self._tf_zoom_factor.insert(0,"0.1")
        self._tf_pan_factor.delete(0,'end')
        self._tf_pan_factor.insert(0,"0.1")
        self._tf_max_iterations.delete(0,'end')
        self._tf_max_iterations.insert(0,"25")
        self._my_mandelbrot.reset_image()
        self._request_mandelbrot_image()

    def _create_buttons(self):
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
        self._frame_input_area.pack()
        button6=tk.Button(self._frame_go_reset_buttons, text="GO", command=self._go_click)
        button6.grid(row=0, column=0)
        button7 = tk.Button(self._frame_go_reset_buttons, text="RS", command=self._go_reset)
        button7.grid(row=0, column=1)
        self._frame_go_reset_buttons.pack()

if __name__ == "__main__":
    mb_window = MandelbrotWindow()
    mb_window.mainloop()