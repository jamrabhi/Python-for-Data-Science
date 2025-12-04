import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    '''Inverts the color of the image received.'''
    if array is None:
        return None

    inverted = 255 - array

    plt.imshow(inverted)
    plt.show()
    return inverted


def ft_red(array):
    '''Keeps only the red channel of the image.'''
    if array is None:
        return None

    red = array * np.array([1, 0, 0])

    plt.imshow(red)
    plt.show()
    return red


def ft_green(array):
    '''Keeps only the green channel of the image.'''
    if array is None:
        return None

    green = array.copy()
    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]

    plt.imshow(green)
    plt.show()
    return green


def ft_blue(array):
    '''Keeps only the blue channel of the image.'''
    if array is None:
        return None

    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0

    plt.imshow(blue)
    plt.show()
    return blue


def ft_grey(array):
    '''Converts the image to greyscale.'''
    if array is None:
        return None

    grey = array.copy()
    grey_value = np.sum(array, axis=2) / 3
    grey[:, :, 0] = grey_value
    grey[:, :, 1] = grey_value
    grey[:, :, 2] = grey_value

    plt.imshow(grey)
    plt.show()
    return grey
