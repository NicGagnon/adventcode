from collections import deque

A = open('20.in').read().split('\n')[:-1]
max_row_length = max(map(len, A))
grid = [['' for _ in range(max_row_length)] for _ in range(len(A))]
outer_edge = []
outer_warps, inner_warps, all_positions = {}, {}, {}
for y, row in enumerate(A):
    for x, value in enumerate(row):
        if y == 2 or y == len(A)-3 or x == 2 or x == max_row_length-3:
            outer_edge.append((y,x))
        grid[y][x] = value


def get_neighboring_value(y, x):
    """
    return the neighboring value for the gate code
    :param y:
    :param x:
    :return:
    """
    h_directions = [(y-1, x, 'S'), (y+1, x, 'N')]
    v_directions = [(y, x-1, 'W'), (y, x+1, 'E')]
    for d in h_directions:
        if 0 <= d[0] <= len(A)-1:
            if grid[d[0]][d[1]].isupper():
                return grid[d[0]][d[1]], d[2]
    for d in v_directions:
        if 0 <= d[1] <= max_row_length-1:
            if grid[d[0]][d[1]].isupper():
                return grid[d[0]][d[1]], d[2]
    raise EnvironmentError("FUCK")


def get_start_pos(y, x, d):
    """
    Return the coordinates of the neighboring position for that gate
    :param y:
    :param x:
    :return:
    """
    if d == "N":
        # check if in grid and then check if .
        if y-1 > 0:
            if grid[y-1][x] == ".":
                return y-1, x
        return y+2, x
    elif d == "S":
        if y+1 < len(A):
            if grid[y+1][x] == ".":
                return y+1, x
        return y - 2, x
    elif d == "W":
        if x + 1 < max_row_length:
            if grid[y][x+1] == ".":
                return y, x+1
        return y, x-2
    else:
        if x - 1 > 0:
            if grid[y][x-1] == ".":
                return y, x-1
        return y, x+2


def alphabetize(a, b):
    return "".join([b, a]) if a > b else "".join([a, b])


def get_available_tiles(y, x, l):
    directions = [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]
    a_tiles = []
    if (y, x) in outer_warps:
        if l > 0:
            a_tiles.append((outer_warps[(y, x)], l - 1))
    elif (y, x) in inner_warps:
        if l < 25:
            a_tiles.append((inner_warps[(y, x)], l + 1))

    for d in directions:
        if grid[d[0]][d[1]] == ".":
            a_tiles.append((d, l))
    return a_tiles


def get_matching_tag(location):
    tag = all_positions[location]
    ohne_loc = [x for x in all_positions if x != location]
    for loc in ohne_loc:
        if all_positions[loc] == tag:
            return loc
    return location


def get_tag(tag):
    for loc in all_positions:
        if all_positions[loc] == tag:
            return loc
    raise ValueError("Tag not found")


for y, row in enumerate(grid):
    for x, value in enumerate(row):
        if value.isupper():
            neigh_value, dir = get_neighboring_value(y, x)
            all_positions[get_start_pos(y, x, dir)] = alphabetize(value, neigh_value)

for loc in all_positions:
    if loc in outer_edge:
        outer_warps[loc] = get_matching_tag(loc)
    else:
        inner_warps[loc] = get_matching_tag(loc)


start_position = get_tag("AA")
end_position = get_tag("ZZ")
outer_warps.pop(start_position)
outer_warps.pop(end_position)
Q = deque()
Q.append((start_position, 0, 0))
seen = []

while Q:
    loc, d, l = Q.popleft()
    seen.append((loc, l))
    y, x = loc[0], loc[1]
    if (y, x) == end_position and l == 0:
        print(d)
        exit(1)
    else:
        for tile, layer in get_available_tiles(y, x, l):
            if (tile, layer) not in seen:
                Q.append((tile, d + 1, layer))

