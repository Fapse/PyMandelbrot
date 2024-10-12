# Draw Mandelbrot sets in Python
# Based on the course on the RealPython website:
# https://realpython.com/mandelbrot-set-python/

from mandelbrotset import MandelbrotSet
from PIL import Image
from PIL.ImageColor import getrgb
from viewport import Viewport

class Mandelbrot:

    def __init__(self):
        self.center_real: float = -0.75
        self.center_im: float = 0.0
        self.width: float = 3.5
        self.max_iterations: int = 25
        self.escape_radius: int = 1000
        self.image_width: int = 512
        self.image_height: int = 512

    @staticmethod
    def hsb(hue_degrees: int, saturation: float, brightness: float) -> tuple[int, int, int] | tuple[int, int, int, int]:
        return getrgb(
            f"hsv({hue_degrees % 360},"
            f"{saturation * 100}%,"
            f"{brightness * 100}%)"
        )

    def create_mandelbrot(self) -> Image:
        mandelbrot_set = MandelbrotSet(max_iterations=self.max_iterations, escape_radius=self.escape_radius)
        image = Image.new(mode="RGB", size=(self.image_width, self.image_height))
        #for pixel in Viewport(image, center=-0.75, width=3.5): # display complete mandelbrot set
        for pixel in Viewport(image, center=complex(self.center_real, self.center_im), width=self.width):
            stability = mandelbrot_set.stability(complex(pixel), smooth=True)
            pixel.color = (
                (0, 0, 0)
                if stability == 1
                else Mandelbrot.hsb(
                    hue_degrees=int(stability * 360 + 80),
                    saturation=stability,
                    brightness=1,
                )
            )
        return image

if __name__ == "__main__":
    my_mandelbrot = Mandelbrot()
    print("This might take a while...")
    my_mandelbrot.create_mandelbrot().show()