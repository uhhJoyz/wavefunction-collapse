import imageio as iio
from PIL import ImageColor


def convert_hex(rgb):
    sum = 0
    for val in rgb:
        sum += val
        sum = sum << 8
    return "#{:06x}".format(sum >> 8)


def read_tileset(filename="tileset.png", dx=3, dy=3, numtiles=9):
    img = iio.v2.imread(filename)

    legend = set()
    for row in img:
        for pixel in row:
            hexval = convert_hex(pixel)
            legend.add(hexval)

    legend = {val : i for (i, val) in enumerate(legend)}
    map = []
    for row in img:
        temp = []
        for p in row:
            temp.append(legend[convert_hex(p)])
        map.append(temp)

    tileset = []
    i, j = 0, 0
    while j < len(map) and len(tileset) < numtiles:
        while i < len(map[0]):
            temp = [map[j1][i:i+dx] for j1 in range(j, j+dy)]
            tileset.append(temp)
            i += dx
        i = 0
        j += dy

    colors = list(legend.keys())
    colors = [ImageColor.getcolor(c, "RGB") for c in colors]

    return tileset, colors
