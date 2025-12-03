'''
Program that loads an image, slices a specific region, converts it to grayscale
and displays the new image.
'''
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom(img_array: np.ndarray) -> np.ndarray:
    '''Zooms the image, converts to grayscale, reshapes and displays it.'''
    if img_array.shape[0] < 500 or img_array.shape[1] < 850:
        raise AssertionError("Image is too small.")

    sliced = img_array[100:500, 450:850, :]
    gray_img = np.mean(sliced, axis=2).astype(np.uint8)
    zoomed = gray_img.reshape((400, 400, 1))

    plt.imshow(zoomed, cmap='gray')
    print(f"New shape after slicing: {zoomed.shape} or {gray_img.shape}")
    return zoomed


def main():
    '''Main function to load image, apply zoom and display it.'''
    try:
        img_array = ft_load("animal.jpeg")
        if img_array is None:
            return

        print(img_array)
        print(zoom(img_array))
        plt.show()

    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
