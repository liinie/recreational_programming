import matplotlib.pyplot as plt
import numpy as np

import matplotlib

origin_image = plt.imread('Brown_bear_(Ursus_arctos_arctos)_running.jpg')

image = origin_image.copy()

unsorted_pixels = {(i, j) for i in range(image.shape[0]) for j in range(image.shape[1])}


def cell_partition(start_pixel):
    pass


def set_color():
    pass


if __name__ == '__main__':
    print(unsorted_pixels)



