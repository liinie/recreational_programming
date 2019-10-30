import matplotlib.pyplot as plt
import numpy as np


def euclidean_distance(color1, color2):
    print(f'color1: {color1}')
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
    print(f'start color: {start_color}')
    print(f'start pixel: {start_pixel}')
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


def change_color(cell):
    r = 0
    g = 0
    b = 0
    for pixel in cell:
        print(f'red color value: {image[pixel][0]}')
        r += image[pixel][0]
        g += image[pixel][1]
        b += image[pixel][2]
    mean_color = [int(np.mean(r)), int(np.mean(g)), int(np.mean(b))]
    print(f'mean color: {mean_color}')

    for pixel in cell:
        image[pixel] = mean_color


if __name__ == '__main__':
    #
    arr = np.random.randint(256, size=(5, 6, 3))
    #
    # origin_image = plt.imread(arr)
    #
    # image = origin_image.copy()
    #
    # unsorted_pixels = {(i, j) for i in range(image.shape[0]) for j in range(image.shape[1])}
    # pixel_cell = {}
    #
    # # print(image[list(unsorted_pixels)[0]])
    #
    # THREADSHOLD = 100
    #
    # cell_dict = {}
    #
    # count = 0
    # while unsorted_pixels:
    #     start_pixel = list(unsorted_pixels)[0]
    #     cell = flood_fill(start_pixel)
    #     change_color(cell)
    #
    #     cell_num = len(cell_dict)
    #     cell_dict[cell_num] = cell
    #
    #     count += 1
    #
    #     if count % 50 == 0:
    #         print(f'number of pixels to sort: {len(unsorted_pixels)}')


    # settings
    h, w = 10, 10  # for raster image
    nrows, ncols = 5, 4  # array of sub-plots
    figsize = [6, 8]  # figure size, inches

    # prep (x,y) for extra plotting on selected sub-plots
    xs = np.linspace(0, 2 * np.pi, 60)  # from 0 to 2pi
    ys = np.abs(np.sin(xs))  # absolute of sine

    # create figure (fig), and array of axes (ax)
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)

    # # plot simple raster image on each sub-plot
    # for i, axi in enumerate(ax.flat):
    #     # i runs from 0 to (nrows*ncols-1)
    #     # axi is equivalent with ax[rowid][colid]
    #     img = np.random.randint(10, size=(h, w))
    #     axi.imshow(img, alpha=0.25)
    #     # get indices of row/column
    #     rowid = i // ncols
    #     colid = i % ncols
    #     # write row/col indices as axes' title for identification
    #     axi.set_title("Row:" + str(rowid) + ", Col:" + str(colid))

    # one can access the axes by ax[row_id][col_id]
    # do additional plotting on ax[row_id][col_id] of your choice
    ax[0][2].imshow(arr)
    ax[4][3].plot(ys ** 2, xs, color='green', linewidth=3)

    plt.tight_layout(True)
    plt.show()




