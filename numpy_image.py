import sys
import numpy as np
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size
print(f"Original image is {width} x {height} pixels")

# Convert image to a numpy array
pixel_array = np.array(img)
max_value = np.max(pixel_array)
print(f"Max value: {max_value}")
x_center = pixel_array.shape[0] / 2
y_center = pixel_array.shape[1] / 2


def mask(x, y, z):
    distance_from_center = np.sqrt(np.square(x - x_center) + np.square(y - y_center))
    max_val = np.max(distance_from_center)
    return distance_from_center / max_val


mask_array: np.ndarray = np.fromfunction(mask, pixel_array.shape)
output_array = np.multiply(mask_array, pixel_array)
output_array = output_array.astype(np.uint8)

# Pillow has built-in support for creating an Image from a numpy array
new_img = Image.fromarray(output_array)
new_img.save(output_path)
