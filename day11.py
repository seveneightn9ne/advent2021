from typing import List, Tuple, Set
from functools import reduce

def get_input() -> List[List[int]]:
    f = open("input/day11.txt", "r")
    lines = f.readlines()
    return [list(map(int, [c for c in line.strip()])) for line in lines]

def neighbors(y, x, map):
    return filter(
        lambda p: p[0] >= 0 and p[1] >= 0 and p[0] < len(map) and p[1] < len(map[0]),
        [(y-1, x), (y-1, x-1), (y-1, x+1), (y+1, x), (y+1, x+1), (y+1, x-1), (y, x-1), (y, x+1)])

def flash(y, x, map: List[List[int]], has_flashed: Set[int]) -> int:
    if (y, x) in has_flashed:
        return 0
    n_flashes = 1
    has_flashed.add((y, x))
    for (n_y, n_x) in neighbors(y, x, map):
        map[n_y][n_x] += 1
        if map[n_y][n_x] > 9:
            n_flashes += flash(n_y, n_x, map, has_flashed)
    return n_flashes

def step(input: List[List[int]], n: int) -> int:
    has_flashed = set([])
    n_flashes = 0
    for y, row in enumerate(input):
        for x, ocotopus in enumerate(row):
            # print("Stepping at {},{}: {}".format(y, x, ocotopus))
            input[y][x] = ocotopus + 1
            if input[y][x] > 9:
                # print("flashing {},{}".format(y, x))
                n_flashes += flash(y, x, input, has_flashed)
    if len(has_flashed) == len(input) * len(input[0]):
        print("All flashed at step {}".format(n+1))
    for (y, x) in has_flashed:
        # print("Zeroing {},{}".format(y, x))
        input[y][x] = 0
    # print("finished step")
    # print_map(input)
    return n_flashes

def print_map(input):
    for row in input:
        print(''.join(map(str, row)))

input = get_input()
n_flashes = 0
for i in range(100000):
    # print_map(input)
    n_flashes += step(input, i)
    # print(n_flashes)

