from collections import deque
from itertools import permutations

A = open("18.in").read().split("\n")[:-1]
grid = [[x for x in range(81)] for y in range(81)]
start_pos = (0, 0)
keys, doors = {}, {}
walls, paths = {}, {}
for y, row in enumerate(A):
    for x, i in enumerate(row):
        grid[y][x] = i
        if i == '@':
            start_pos = y, x
        elif i.islower():
            keys[(y, x)] = i
        elif i.isupper():
            doors[(y, x)] = i
        elif i == "#":
            walls[(y, x)] = i
        else:
            paths[(y, x)] = i


# b
## d and g
# i

def neighbors(y, x):
    return [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]


def search_key(sp, _keys, _doors):
    Q = deque()
    Q.append((sp, 0))
    seen = {}
    poss_keys = []
    while Q:
        loc, d = Q.popleft()
        seen[loc] = True
        if loc in _keys:
            poss_keys.append(_keys.pop(loc))
        for n in neighbors(*loc):
            if n not in _doors and n not in walls and n not in seen:
                Q.append((n, d + 1))
    return poss_keys


def open_door(k, ds):
    for d in ds:
        if k.upper() == ds[d]:
            ds.pop(d)
            return


def get_sp(k, ks):
    for x in ks:
        if k == ks[x]:
            ks.pop(x)
            return x


if __name__ == '__main__':

    Q = deque()
    Q.append('b')

    while Q:
        target = Q.popleft()
        p_keys = search_key(start_pos)
    """all_distances = []
    total_distance = 0
    possible_keys = []
    routes = []
    sp, tmp_keys, tmp_doors = start_pos, keys.copy(), doors.copy()
    p_keys = search_key(sp, tmp_keys, tmp_doors)
    for p in p_keys:
        new_route = list(p)
        routes.append(new_route)

    for k in p_keys:
        tmp_keys, tmp_doors = keys.copy(), doors.copy()
        sp = get_sp(k, tmp_keys)
        open_door(k, tmp_doors)
        p_keys = search_key(sp, tmp_keys, tmp_doors)
        for route in routes:
            for p in p_keys:
                new_route = route.copy()
                new_route.append(p)
                routes.append(new_route)"""
    print(routes)
    # total_distance += relative_distance
    # print("relative distance to {} is {}".format(key, relative_distance))
    # print("key order {} was succesful and total distance was {}".format(perm, total_distance))
    all_distances.append(total_distance)
