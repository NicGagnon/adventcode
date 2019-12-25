from copy import deepcopy
A = open('24.in').read().split("\n")[:-1]
grids = [[["." for x in range(5)] for y in range(5)] for z in range(200)]
recursive_squares = {(1, 2): [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], (2, 1): [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],
                     (2, 3): [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)], (3, 2): [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]}
outter_layer = {(0, 0): [(1, 2), (2, 1)], (0, 1): [(1, 2)], (0, 2): [(1, 2)], (0, 3): [(1, 2)], (0, 4): [(1, 2),
                (2, 3)], (1, 0): [(2, 1)], (2, 0): [(2, 1)], (3, 0): [(2, 1)], (4, 0): [(2, 1), (3, 2)], (1, 4):
                [(2, 3)], (2, 4): [(2, 3)], (3, 4): [(2, 3)], (4, 4): [(2, 3), (3, 2)], (4, 1): [(3, 2)], (4, 2):
                [(3, 2)], (4, 3): [(3, 2)]}
grid_record = {}
for y, row, in enumerate(A):
    for x, value in enumerate(row):
        grids[100][y][x] = value

def stringify_grid(g):
    return "".join([x for row in g for x in row])


def calc_bio(g):
    multiplier = [2 ** i for i in range(25)]
    flat_grid = [1 if i == "#" else 0 for _row in g for i in _row]
    return sum([i*j for i,j in zip(multiplier, flat_grid)])


def min_neighbor(z, y, x):
    neighbor_count, neighbors = 0, []
    if (y, x) in recursive_squares:
        neighbors.extend(recursive_squares[(y, x)])
        for loc in neighbors:
            if 1 <= z:
                if grids[z-1][loc[0]][loc[1]] == "#":
                    neighbor_count += 1
    elif (y, x) in outter_layer:
        neighbors.extend(outter_layer[(y, x)])
        for loc in neighbors:
            if z <= 198:
                if grids[z+1][loc[0]][loc[1]] == "#":
                    neighbor_count += 1
    directions = [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]
    for d in directions:
        if (0 <= d[0] <= 4 and 0 <= d[1] <= 4) and (d[0] != 2 and d[1] != 2):
            if grids[z][d[0]][d[1]] == "#":
                neighbor_count += 1
    return 1 <= neighbor_count <= 2


def one_neighbor(z, y, x):
    neighbor_count, neighbors = 0, []
    if (y, x) in recursive_squares:
        neighbors.extend(recursive_squares[(y, x)])
        for loc in neighbors:
            if 1 <= z:
                if grids[z - 1][loc[0]][loc[1]] == "#":
                    neighbor_count += 1
    elif (y, x) in outter_layer:
        neighbors.extend(outter_layer[(y, x)])
        for loc in neighbors:
            if z <= 198:
                if grids[z+1][loc[0]][loc[1]] == "#":
                    neighbor_count += 1
    directions = [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]
    for d in directions:
        if (0 <= d[0] <= 4 and 0 <= d[1] <= 4) and (d[0] != 2 and d[1] != 2):
            if grids[z][d[0]][d[1]] == "#":
                neighbor_count += 1
    return neighbor_count == 1


def bug_migrate(g):
    new_grids = deepcopy(g)
    for z, layer in enumerate(new_grids):
        for y, row in enumerate(layer):
            for x, ele in enumerate(row):
                if ele == ".":
                    if min_neighbor(z, y, x):
                        new_grids[z][y][x] = "#"
                else:
                    if not one_neighbor(z, y, x):
                        new_grids[z][y][x] = "."
    return new_grids


def count_bugs(g):
    count = 0
    for z, layer in enumerate(g):
        for y, row in enumerate(layer):
            for x, value in enumerate(row):
                if value == "#":
                    count += 1
    return count


minute = 0
while minute != 200:
    grids = bug_migrate(grids)
    """record = stringify_grid(grid)
    if record in grid_record:
        print(calc_bio(grid))
        break
    grid_record[record] = True
    """
    minute += 1
    print(count_bugs(grids))

