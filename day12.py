from typing import List, Tuple, Set, Dict
from functools import reduce
from collections import defaultdict

def get_input() -> Dict[str, List[str]]:
    f = open("input/day12.txt", "r")
    lines = [line.strip().split("-") for line in f.readlines()]
    edges = defaultdict(set)
    for (a, b) in lines:
        edges[a].add(b)
        if a != 'start':
            edges[b].add(a)
    return edges

def is_small(cave: str):
    return cave.lower() == cave
def is_big(cave: str):
    return cave.upper() == cave
def no_double_small_caves(path: List[str]):
    seen = set([])
    for cave in path:
        if is_small(cave) and cave in seen:
            return False
        seen.add(cave)
    return True

def find_paths(edges: Dict[str, List[str]]):
    paths = set([])
    queue = [['start']]
    while len(queue):
        path = queue.pop()
        cave = path[-1]
        for next_cave in edges[cave]:
            next_path = path[:] + [next_cave]
            if next_cave == 'end':
                paths.add(tuple(next_path))
            elif next_cave == 'start':
                continue
            elif is_big(next_cave) or next_cave not in path or no_double_small_caves(path):
                queue.append(next_path)
    for path in paths:
        print(path)
    return len(paths)

print(find_paths(get_input()))
# 96466 - too high