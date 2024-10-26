import tkinter as tk
from PIL import ImageTk
from control_area import ControlArea
from image_area import ImageArea
from mandelbrot import Mandelbrot

class MandelbrotWindow(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.winfo_toplevel().title("PyMandelbrot")
        self._parent = parent
        self.my_mandelbrot = Mandelbrot()
        self.image_area = ImageArea(self)
        self._control_area = ControlArea(self)
        self.pack()

if __name__ == "__main__":
    root = tk.Tk()
    mb_window = MandelbrotWindow(root)
    root.mainloop()