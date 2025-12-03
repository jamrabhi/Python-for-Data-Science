import os
from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    '''Load an image, prints its format and its pixels content in RGB.'''
    try:
        if not isinstance(path, str):
            raise AssertionError("Path must be a string")
        if not os.path.isfile(path):
            raise AssertionError("File not found")
        ext = os.path.splitext(path)[1].lower()
        if ext not in [".jpg", ".jpeg"]:
            raise AssertionError("File must be JPG or JPEG")

        with Image.open(path) as img:
            if img.format != "JPEG":
                raise AssertionError("File content is not JPEG")

            img_array = np.array(img)
            print(f"The shape of image is: {img_array.shape}")
            return img_array

    except AssertionError as err:
        print(f"AssertionError: {err}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
