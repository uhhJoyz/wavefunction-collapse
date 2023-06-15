import random


# returns up, right, down, left
def get_adjacent(tiles, y, x):
    a = tiles[y-1][x] if y - 1 >= 0 else None
    b = tiles[y][x+1] if x + 1 < len(tiles[y]) else None
    c = tiles[y+1][x] if y + 1 < len(tiles) else None
    d = tiles[y][x-1] if x - 1 >= 0 else None

    return [a, b, c, d]


def overlapping_comp(comp, adj):
    s = None
    for (i, t) in enumerate(adj):
        if (not s) and (not t is None):
            s = set(comp[t][i])
        elif (not t is None):
            s = s.intersection(set(comp[t][i]))
    if not s:
        s = set(range(7))
    return random.sample(list(s), 1)[0]


def generate_tiles(comp, tiles):
    for (i, row) in enumerate(tiles):
        for (j, t) in enumerate(row):
            if not t:
                adj = get_adjacent(tiles, i, j)
                tiles[i][j] = overlapping_comp(comp, adj)
    return

