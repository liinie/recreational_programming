import matplotlib.pyplot as plt
import numpy as np

arr = np.random.randint(0, 256, size=(10, 20, 3))


def partition_image(num, image):
    h = image.shape[0]
    w = image.shape[1]
    c = image.shape[2]

    cell_w = np.floor(w/num)
    last_cell_w = cell_w + (w - cell_w*num)
    cell_n = num

    while num>0:
        if num != 1:
            pixel_in_cell = []
            for i in range(h):
                for j in range((cell_n - num)*cell_w, (cell_n - num + 1)*cell_w + 1):
                    pixel_in_cell.append(image[i, j])
            median_c = cell_median(pixel_in_cell)
            for i in range(h):
                for j in range(cell_w + (cell_n - num) * cell_w):
                    image[i, j] = median_c
            num -= 1
        else:
            # TODO: the last cell division
            pass 


def cell_median(cell):
    return np.average(cell)


plt.imshow(arr)
plt.show()

if __name__ == '__main__':
    print(partition_image(1, arr))




