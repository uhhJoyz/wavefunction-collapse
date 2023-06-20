from PIL import Image
import numpy as np


def generate_image(tileset, tiles, color_scheme):
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
            img[i][j] = color_scheme[p]

    img = np.asarray(img, dtype=np.uint8)
    img = Image.fromarray(img)
    img.save("img.png")
