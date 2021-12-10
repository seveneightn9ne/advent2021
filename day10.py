from typing import List, Tuple, Dict
from functools import reduce
from collections import defaultdict

def get_input() -> List[str]:
    f = open("input/day10.txt", "r")
    return [line.strip() for line in f.readlines()]

PAIRS = {
    "{": "}",
    "[": "]",
    "(": ")",
    "<": ">",
}
SCORE_PART1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
    None: 0,
}
SCORE_PART2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

def first_corrupt_char(line: str):
    q = []
    for c in line:
        if c in PAIRS.keys():
            q.append(c)
        else:
            must_match = q.pop(-1)
            if c != PAIRS[must_match]:
                return c
    return None

def part2_score(line: str):
    q = []
    for c in line:
        if c in PAIRS.keys():
            q.append(c)
        else:
            must_match = q.pop(-1)
            if c != PAIRS[must_match]:
                return None # corrupt line
    score = 0
    for c in reversed(q):
        score = score * 5 + SCORE_PART2[c]
    return score
            
def part2_winner(input: List[str]):
    scores = sorted(filter(lambda s: s != None, map(part2_score, input)))
    return scores[len(scores)//2]


def part1_score(input: List[str]):
    return sum(map(lambda c: SCORE_PART1[c], map(first_corrupt_char, input)))

print(part2_winner(get_input()))
