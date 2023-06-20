from lib.compare_tiles import *
from lib.generate_tiles import *
from lib.image_generation import *
from lib.read_tileset import *


TILESET = [
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        [
            [0, 1, 0],
            [0, 1, 2],
            [0, 0, 0]
        ],
        [
            [0, 0, 0],
            [0, 1, 1],
            [0, 1, 0]
        ],
        [
            [0, 0, 0],
            [2, 1, 0],
            [0, 1, 0]
        ],
        [
            [0, 1, 0],
            [1, 1, 0],
            [0, 0, 0]
        ],
        [
            [0, 1, 0],
            [0, 1, 0],
            [0, 2, 0]
        ],
        [
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ],
        [
            [0, 2, 0],
            [1, 1, 1],
            [0, 1, 0]
        ]
    ]

X_DIM = 128
Y_DIM = 128


def wavefunction_collapse(tiles=None, tileset=None, x_dim=None, y_dim=None, dark=None, light=None, color_scheme=None):
    """
    A two color wavefunction collapse image generation algorithm.
    :param tiles: a list of user-defined tiles
    :param tileset: the tileset the user wishes
    :param x_dim: the x dimensions of the image in tiles
    :param y_dim: the y dimensions of the image in tiles
    :param dark: the color of the background of the generation
    :param light: the color of the path of the generation
    :return:
    """

    if tileset is None:
        tileset, color_scheme = read_tileset(numtiles=8)

    if x_dim is None:
        x_dim = X_DIM

    if y_dim is None:
        y_dim = Y_DIM

    comp = generate_compatibility(tileset)
    if tiles is None:
        tiles = [[None for x in range(x_dim)] for y in range(y_dim)]

    generate_tiles(comp, tiles)
    if color_scheme:
        generate_image(tileset, tiles, color_scheme)
    else:
        generate_image(tileset, tiles, [(0,10,10), (255, 255, 255), (255, 0, 0)])


if __name__ == "__main__":
    # tiles = [[0 if 0.25 * X_DIM < x < 0.75 * X_DIM and 0.25 * Y_DIM < y < 0.75 * Y_DIM else None for x in range(X_DIM)] for y in range(Y_DIM)]
    wavefunction_collapse()
