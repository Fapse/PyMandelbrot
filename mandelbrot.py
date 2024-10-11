# Draw Mandelbrot sets in Python
# Based on the course on the RealPython website:
# https://realpython.com/mandelbrot-set-python/

from mandelbrotset import MandelbrotSet
from PIL import Image
from PIL.ImageColor import getrgb
from viewport import Viewport

def hsb(hue_degrees: int, saturation: float, brightness: float):
    return getrgb(
        f"hsv({hue_degrees % 360},"
        f"{saturation * 100}%,"
        f"{brightness * 100}%)"
    )

def create_mandelbrot() -> Image:
    mandelbrot_set = MandelbrotSet(max_iterations=450, escape_radius=1000)
    image = Image.new(mode="RGB", size=(512, 512))
    #for pixel in Viewport(image, center=-0.75, width=3.5): # display complete mandelbrot set
    for pixel in Viewport(image, center=-0.7435 + 0.1314j, width=0.002):
        stability = mandelbrot_set.stability(complex(pixel), smooth=False)
        pixel.color = (
            (0, 0, 0)
            if stability == 1
            else hsb(
                hue_degrees=int(stability * 360 + 80),
                saturation=stability,
                brightness=1,
            )
        )
    return image

if __name__ == "__main__":
    print("This might take a while...")
    create_mandelbrot().show()