from typing import List
from functools import reduce

def get_input() -> List[int]:
    f = open("input/day1.txt", "r")
    lines = filter(lambda line: line, f.readlines())
    return list(map(int, lines))

def how_many_increased(input: List[int]) -> int:
    sums = list(map(sum, zip(input, input[1:], input[2:])))
    s = 0
    for a, b in zip(sums, sums[1:]):
        if b > a:
            s += 1
    return s

print(how_many_increased(get_input()))