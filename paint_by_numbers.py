import matplotlib.pyplot as plt
import numpy as np

import matplotlib


def euclidean_distance(color1, color2):
    # print(f'color1: {color1}')
    r1, g1, b1 = color1
    r2, g2, b2 = color2

    return np.sqrt((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2)


#  return single cell of the similar color'
def neighbors(current_pixel):
    neighbors = set()
    if current_pixel[0] > 0:
        neighbors.add((current_pixel[0]-1, current_pixel[1]))
    elif current_pixel[0] < image.shape[0] - 1:
        neighbors.add((current_pixel[0]+1, current_pixel[1]))
    elif current_pixel[1] > 0:
        neighbors.add((current_pixel[0], current_pixel[1]-1))
    elif current_pixel[1] < image.shape[1] -1:
        neighbors.add((current_pixel[0], current_pixel[1]+1))

    return neighbors


def flood_fill(start_pixel):
    start_color = image[start_pixel]
    # print(f'start color: {start_color}')
    # print(f'start pixel: {start_pixel}')
    to_search = set()
    to_search.add(start_pixel)
    cell = set()
    non_liked_color_pixel = set()

    while to_search:
        current_pixel = to_search.pop()
        print(f'current pixel: {current_pixel}')

        if euclidean_distance(image[current_pixel], start_color) < THREADSHOLD:
            cell.add(current_pixel)
            unsorted_pixels.remove(current_pixel)

            for n in neighbors(current_pixel):
                if n in unsorted_pixels and n not in non_liked_color_pixel:
                    to_search.add(n)

        else:
            non_liked_color_pixel.add(current_pixel)

    return cell


if __name__ == '__main__':

    origin_image = plt.imread('Brown_bear_(Ursus_arctos_arctos)_running.jpg')

    image = origin_image.copy()

    unsorted_pixels = {(i, j) for i in range(image.shape[0]) for j in range(image.shape[1])}
    pixel_cell = {}

    # print(image[list(unsorted_pixels)[0]])

    THREADSHOLD = 20

    cell_dict = {}

    count = 0
    while unsorted_pixels:
        start_pixel = list(unsorted_pixels)[0]
        cell = flood_fill(start_pixel)

        cell_num = len(cell_dict)
        cell_dict[cell_num] = cell

        count += 1

        if count % 50 == 0:
            print(f'number of pixels to sort: {len(unsorted_pixels)}')

    plt.imshow(image)




