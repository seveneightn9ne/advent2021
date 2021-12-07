from typing import List, Tuple, Dict
from functools import reduce
from collections import defaultdict

def get_input() -> List[int]:
    f = open("input/day6.txt", "r")
    lines = f.readlines()

    return list(map(int,lines[0].strip().split(',')))

def simulate(fishes: Dict[int, int]):
    next_fishes = defaultdict(int)
    for fish_timer in fishes.keys():
        n_fish = fishes[fish_timer]
        if fish_timer == 0:
            next_fishes[8] += n_fish
            next_fishes[6] += n_fish
        else:
            next_fishes[fish_timer-1] += n_fish
    return next_fishes

def simulate_days(fishes: List[int], n_days: int):
    fish_dict = defaultdict(int)
    for fish in fishes:
        fish_dict[fish] += 1
    for day in range(n_days):
        fish_dict = simulate(fish_dict)
    return sum(fish_dict.values())


print(simulate_days(get_input(), 256))