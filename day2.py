from typing import List, Tuple
from functools import reduce

def get_input() -> List[Tuple[str, int]]:
    f = open("input/day2.txt", "r")
    lines = filter(lambda line: line, f.readlines())
    return list(map(lambda line: (line.split()[0], int(line.split()[1])), lines))


def follow(instructions: List[Tuple[str, int]]) -> Tuple[int, int]:
    x, z, aim = 0, 0, 0
    for (dir, amt) in instructions:
        if dir == "forward":
            x += amt
            z += aim * amt
        elif dir == "down":
            aim += amt
        elif dir == "up":
            aim -= amt
    return x, z


def how_many_increased(input: List[int]) -> int:
    sums = list(map(sum, zip(input, input[1:], input[2:])))
    s = 0
    for a, b in zip(sums, sums[1:]):
        if b > a:
            s += 1
    return s

def total(input: List[Tuple[str, int]]) -> int:
    x, z = follow(input)
    return x * z

print(total(get_input()))