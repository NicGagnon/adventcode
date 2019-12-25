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


def get_sp(k):
    for sp in keys:
        if k == keys[sp]:
            return sp


if __name__ == '__main__':
    Q = deque()
    start_pos = get_sp('b')
    key = keys.pop(start_pos)
    open_door(key, doors)
    Q.append(('h', start_pos))
    tmp_doors, tmp_keys = doors.copy(), keys.copy()
    while Q:
        target, sp = Q.popleft()
        p_keys = search_key(sp, tmp_keys, tmp_doors)
        for key in p_keys:
            Q.append((key, get_sp(key)))
