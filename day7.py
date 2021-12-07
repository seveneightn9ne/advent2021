from typing import List, Tuple, Dict
from functools import reduce
from collections import defaultdict

def get_input() -> List[int]:
    f = open("input/day7.txt", "r")
    lines = f.readlines()

    return list(map(int,lines[0].strip().split(',')))

costs = defaultdict(int)
def build_costs(max: int):
    for i in range(1, max+1):
        costs[i] = costs[i-1] + i

def average(crabs: List[int]) -> int:
    return sum(crabs)//len(crabs)

def cost(crabs: List[int], point: int) -> int:
    return sum([
        costs[abs(point - crab)] for crab in crabs
    ])

def best_point(crabs: List[int]) -> int:
    start = average(crabs)
    start_cost = cost(crabs, start)
    asc = start + 1
    asc_cost = cost(crabs, asc)
    if asc_cost < start_cost:
        walk_dir = 1
        best = asc
        best_cost = asc_cost
    else:
        walk_dir = -1
        best = start
        best_cost = start_cost
    while True:
        next = best + walk_dir
        next_cost = cost(crabs, next)
        if next_cost > best_cost:
            return best
        best = next
        best_cost = next_cost

crabs = get_input()
build_costs(max(crabs)-min(crabs))
print(cost(crabs, best_point(crabs)))

# for pos in range(min(crabs), max(crabs)+1):
#     print("{}: {}".format(pos, cost(crabs, pos)))

