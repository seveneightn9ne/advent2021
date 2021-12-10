from typing import List, Tuple, Dict
from functools import reduce
from collections import defaultdict

def get_input() -> List[List[int]]:
    f = open("input/day9.txt", "r")
    return [[int(c) for c in line.strip()] for line in f.readlines()]

def is_low_point(y, x, map):
    point = map[y][x]
    for (i, j) in neighbors(y, x, map):
        if point > map[i][j]:
            return False
    return True

def neighbors(y, x, map):
    return filter(
        lambda p: p[0] >= 0 and p[1] >= 0 and p[0] < len(map) and p[1] < len(map[0]),
        [(y-1, x), (y+1, x), (y, x-1), (y, x+1)])

def size_basin(y, x, map):
    points_in_basin = set([(y, x)])
    queue = [(y, x)]
    while len(queue):
        (py, px) = queue.pop()
        for (i, j) in neighbors(py, px, map):
            if map[i][j] != 9 and (i, j) not in points_in_basin:
                points_in_basin.add((i, j))
                queue.append((i, j))
    return len(points_in_basin)

def part2(map: List[List[int]]):
    basin_sizes = []
    for i, row in enumerate(map):
        for j, p in enumerate(row):
            if is_low_point(i, j, map):
                print("{},{} is a low point: {}".format(i, j, map[i][j]))
                basin_sizes.append(size_basin(i, j, map))
                print("basin size is {}".format(basin_sizes[-1]))
    top3 = sorted(basin_sizes)[-3:]
    return reduce(lambda a,b: a*b, top3)

print(part2(get_input()))
