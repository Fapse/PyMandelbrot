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
        self._image_area = ImageArea(self)
        self._control_area = ControlArea(self)
        self.pack()

    def request_mandelbrot_image(self, max_iterations: int):
        ph = ImageTk.PhotoImage(self.my_mandelbrot.create_mandelbrot(int(max_iterations)))
        for widget in self._image_area.winfo_children():
            widget.destroy()
        mandelbrot_image = tk.Label(self._image_area, image=ph)
        mandelbrot_image.image = ph
        mandelbrot_image.pack()

if __name__ == "__main__":
    root = tk.Tk()
    mb_window = MandelbrotWindow(root)
    root.mainloop()