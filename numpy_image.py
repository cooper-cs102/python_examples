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
print(f"numpy array dimensions before transpose: {pixel_array.shape}")

# Transform the array
pixel_array = np.transpose(pixel_array, axes=[1, 0, 2])
print(f"numpy array dimensions after transpose: {pixel_array.shape}")

# Pillow has built-in support for creating an Image from a numpy array
new_img = Image.fromarray(pixel_array)
new_img.save(output_path)
