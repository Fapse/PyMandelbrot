# Draw Mandelbrot sets in Python
# Based on the course on the RealPython website:
# https://realpython.com/mandelbrot-set-python/

from PIL import Image
from PIL import ImageEnhance
from mandelbrot import MandelbrotSet
from viewport import Viewport

mandelbrot_set = MandelbrotSet(max_iterations=256, escape_radius=1000)

image = Image.new(mode="L", size=(512, 512))

for pixel in Viewport(image, center=-0.7435 + 0.1314j, width=0.002):
    c = complex(pixel)
    instability = 1 - mandelbrot_set.stability(c, smooth=True)
    pixel.color = int(instability * 255)

enhancer = ImageEnhance.Brightness(image)
enhancer.enhance(1.25).show()