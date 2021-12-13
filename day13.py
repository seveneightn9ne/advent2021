from typing import List, Tuple, Set, Dict
from functools import reduce
from collections import defaultdict

def get_input() -> Tuple[List[Tuple[int, int]], List[Tuple[str, int]]]:
    f = open("input/day13.txt", "r")
    coords = []
    folds = []
    for line in f.readlines():
        if ',' in line:
            x, y = map(int, line.strip().split(','))
            coords.append((y, x))
        if 'fold' in line:
            dimension, foldline = line.strip().split(" ")[-1].split('=')
            folds.append((dimension, int(foldline)))
    return (coords, folds)

def make_map(coords: List[Tuple[int, int]]) -> List[List[bool]]:
    height = max(coords, key=lambda c: c[0])[0] + 1
    width = max(coords, key=lambda c: c[1])[1] + 1
    #print("Height:{}, Width:{}".format(height, width))
    m = [[False] * width for h in range(height)]
    for y, x in coords:
        #print("Placing {},{}".format(y, x))
        m[y][x] = True
    return m

def transform_coord(point: int, foldline: int):
    if point < foldline:
        return point
    # foldline = 7
    # x = 8 -> 6
    distance = point - foldline
    return foldline - distance

def fold_map(m: List[List[bool]], fold: Tuple[str, int]) -> List[List[bool]]:
    dim, fline = fold
    new_map_height = fline + 1 if dim == 'y' else len(m)
    new_map_width = fline + 1 if dim == 'x' else len(m[0])
    new_map = [row[:new_map_width] for row in m[:new_map_height]]
    for y, row in enumerate(m):
        for x, hole in enumerate(row):
            new_y, new_x = (y, transform_coord(x, fline)) \
                if dim == 'x' else (transform_coord(y, fline), x)
            new_map[new_y][new_x] |= hole
    return new_map

def count_holes(m: List[List[bool]]) -> int:
    return sum([sum(r) for r in m])

coords, folds = get_input()
m = make_map(coords)
# for row in m:
#     print(row)
for fold in folds:
    m = fold_map(m, fold)
# print("--")
for row in m:
    print(''.join(list(map(lambda c: '*' if c else ' ', row))))
# print(count_holes(next))
