from PIL import Image
import numpy as np


def generate_image(tileset, tiles, dark=(0, 0, 0), light=(255, 35, 255)):
    img = []
    for row in tiles:
        for i in range(len(tileset[0])):
            temp = []
            for t in row:
                for e in tileset[t][i]:
                    temp.append(e)
            img.append(temp)

    for (i, row) in enumerate(img):
        for (j, p) in enumerate(row):
            if p == 1:
                img[i][j] = light
            else:
                img[i][j] = dark

    img = np.asarray(img, dtype=np.uint8)
    img = Image.fromarray(img)
    img.save("img.png")
