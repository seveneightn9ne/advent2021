from typing import List, Tuple, Set, Dict
from functools import reduce
from collections import defaultdict

def get_input() -> Tuple[str, List[List[str]]]:
    f = open("input/day14.txt", "r")
    lines = f.readlines()
    template = "^" + lines[0].strip() + "$"
    rule_list = [tuple(line.strip().split(" -> ")) for line in lines[2:]]
    rules = {k: v for k, v in rule_list}
    return (template, rules)

def run_step(template: str, rules: Dict[str, str]):
    output = ""
    for i in range(len(template)-1):
        pair = template[i:i+2]
        insert = rules[pair]
        output += template[i] + insert
    output += template[-1]
    return output

def template_to_pair_counts(template: str) -> Dict[str, int]:
    d = defaultdict(int)
    for i in range(len(template)-1):
        d[template[i:i+2]] += 1
    return d

def run_step_optimized(pair_counts: Dict[str, int], rules:Dict[str, str]):
    new_pair_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        if pair in rules:
            insert = rules[pair]
            new_pair_counts[pair[0] + insert] += count
            new_pair_counts[insert + pair[1]] += count
        else:
            new_pair_counts[pair] += count
    return new_pair_counts

def part1():
    template, rules = get_input()
    for i in range(10):
        template = run_step(template, rules)
        #print(template)
    counts = defaultdict(int)
    for c in template:
        counts[c] += 1
    print(max(counts.values())-min(counts.values()))

def part2():
    template, rules = get_input()
    pair_counts = template_to_pair_counts(template)
    for i in range(40):
        pair_counts = run_step_optimized(pair_counts, rules)
    char_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        char_counts[pair[0]] += count
        char_counts[pair[1]] += count
    char_counts = {
        char: count//2 for char, count in char_counts.items() if char not in "^$"
    }
    for char, count in char_counts.items():
        print("{}:{}".format(char, count))
    print(max(char_counts.values())-min(char_counts.values()))

part2()