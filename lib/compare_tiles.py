# get the column from the tile
def get_col(tile, col):
    return [row[col] for row in tile]


def goes(t1, t2, dir):
    if dir == 0:
        return goes_above(t1, t2)
    elif dir == 1:
        return goes_right(t1, t2)
    elif dir == 2:
        return goes_below(t1, t2)
    elif dir == 3:
        return goes_left(t1, t2)


# true if tile_1 can go above tile_2
def goes_above(tile_1, tile_2):
    return tile_1[-1] == tile_2[0]


# true if tile_1 can go below tile_2
def goes_below(tile_1, tile_2):
    return tile_2[-1] == tile_1[0]


# true if tile_1 can go to the left of tile_2
def goes_left(tile_1, tile_2):
    return get_col(tile_1, -1) == get_col(tile_2, 0)


def goes_right(tile_1, tile_2):
    return get_col(tile_2, -1) == get_col(tile_1, 0)


# stored in above, right, below, left
def generate_compatibility(tileset):
    comp = [[[] for j in range(4)] for k in range(len(tileset))]
    for (i, t1) in enumerate(tileset):
        for (j, t2) in enumerate(tileset):
            for k in range(4):
                comp[i][k].append(j) if goes(t1, t2, k) else None
    return comp