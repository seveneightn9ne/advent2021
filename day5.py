from typing import List, Tuple
from functools import reduce
from collections import defaultdict

def get_input() -> Tuple[List[int],List[List[List[int]]]]:
    f = open("input/day5.txt", "r")
    lines = f.readlines()

    pairs = list(map(lambda l: # each line
        list(map(lambda ps: # each pair str "3,4"
            list(map(int, ps.split(","))),
            l.strip().split(" -> "))), lines))
    return pairs

def only_hv_lines(lines: List[List[List[int]]]):
    hv_lines = []
    for p1, p2 in lines:
        if p1[0] == p2[0] or p1[1] == p2[1]:
            hv_lines.append([p1, p2])
    return hv_lines

def p_range(p1, p2):
    if p1[0] == p2[0]:
        x = p1[0]
        y_min = min(p1[1], p2[1])
        y_max = max(p1[1], p2[1])
        return [(x, y) for y in range(y_min, y_max+1)]
    elif p1[1] == p2[1]:
        y = p1[1]
        x_min = min(p1[0], p2[0])
        x_max = max(p1[0], p2[0])
        return [(x, y) for x in range(x_min, x_max+1)]
    else:
        x_0 = p1[0]
        x_1 = p2[0]
        y_0 = p1[1]
        y_1 = p2[1]
        x_step = 1 if x_1 > x_0 else -1
        y_step = 1 if y_1 > y_0 else -1
        return zip(range(x_0, x_1, x_step), range(y_0, y_1, y_step))

def points_2_overlap(lines: List[List[List[int]]]):
    points = defaultdict(lambda: defaultdict(lambda: False))
    points_2_overlap = set()
    #lines = only_hv_lines(lines)
    for p1, p2 in lines:
        for x, y in p_range(p1, p2):
            if points[x][y]:
                points_2_overlap.add((x,y))
            points[x][y] = True
    return len(points_2_overlap)


print(points_2_overlap(get_input()))