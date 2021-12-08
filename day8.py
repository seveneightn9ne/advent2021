from typing import List, Tuple, Dict
from functools import reduce
from collections import defaultdict

def get_input() -> List[Tuple[List[str], List[str]]]:
    f = open("input/day8.txt", "r")
    lines = [line.split('|') for line in f.readlines()]
    lines = [(line[0].strip().split(), line[1].strip().split()) for line in lines]
    return lines

digits = {
    # 2
    1: 'cf',
    # 3
    7: 'acf',
    # 4
    4: 'bcdf',
    # 5
    2: 'acdeg',
    3: 'acdfg',
    5: 'abdfg',
    # 6
    0: 'abcefg',
    6: 'abdefg',
    9: 'abcdfg',
    # 7
    8: 'abcdefg',
}

def decode_signals(signals: List[str]) -> Dict[str, int]:
    decoded_digits = {} # int -> str
    signals_by_length = defaultdict(list)
    for signal in signals:
        signals_by_length[len(signal)].append(signal)
    for digit in [1, 4, 7, 8]:
        decoded_digits[digit] = signals_by_length[len(digits[digit])][0]
    
    bd = ''.join([c for c in decoded_digits[4] if c not in decoded_digits[1]])
    cf = decoded_digits[1]
    # len(6) signals: 9 contains 4; 0 contains cf
    for signal in signals_by_length[6]:
        if all([c in signal for c in decoded_digits[4]]):
            decoded_digits[9] = signal
        elif all([c in signal for c in cf]):
            decoded_digits[0] = signal
        else:
            decoded_digits[6] = signal
    # len(5) signals: 5 contains bd; 3 contains cf
    for signal in signals_by_length[5]:
        if all([c in signal for c in bd]):
            decoded_digits[5] = signal
        elif all([c in signal for c in cf]):
            decoded_digits[3] = signal
        else:
            decoded_digits[2] = signal
    return {normalize(v): k for k, v in decoded_digits.items()}

def normalize(signal: str) -> str:
    return ''.join(sorted(signal))

def decode_line(signals: List[str], output: List[str]):
    key = decode_signals(signals)
    return int(''.join([str(key[normalize(digit)]) for digit in output]))

def decode_all(input: List[Tuple[List[str], List[str]]]) -> int:
    return sum([decode_line(signal, output) for signal, output in input])

def how_many_easy_digits(input: List[Tuple[List[str], List[str]]]) -> int:
    print(input)
    easy_digits = 0
    for signals, output in input:
        for digit in output:
            if len(digit) in [2, 3, 4, 7]:
                easy_digits += 1
    return easy_digits

print(decode_all(get_input()))
