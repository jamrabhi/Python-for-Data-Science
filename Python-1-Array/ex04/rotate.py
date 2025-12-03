'''
Program that loads an image, cuts a square from it, grayscales it, and
transposes it.
'''
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def transpose(img_array: np.ndarray) -> np.ndarray:
    '''Transposes the image.'''
    reshaped_img = img_array.reshape((400,400))
    transposed_img = reshaped_img.transpose()
    print(f"New shape after Transpose: {transposed_img.shape}")
    return transposed_img


def zoom(img_array: np.ndarray) -> np.ndarray:
    '''Zooms the image, converts to grayscale reshapes it.'''
    if img_array.shape[0] < 500 or img_array.shape[1] < 850:
        raise AssertionError("Image is too small.")

    sliced = img_array[100:500, 450:850, :]
    gray_img = np.mean(sliced, axis=2).astype(np.uint8)
    zoomed = gray_img.reshape((400, 400, 1))

    print(f"The shape of the image is: {zoomed.shape} or {gray_img.shape}")
    return zoomed


def main():
    '''Main function to load image, apply transpose and display it.'''
    try:
        img_array = ft_load("animal.jpeg")
        if img_array is None:
            return

        zoomed_img = zoom(img_array)
        print(zoomed_img)

        transposed_img = transpose(zoomed_img)
        print(transposed_img)
        plt.imshow(transposed_img, cmap='gray')
        plt.show()

    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
