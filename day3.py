from typing import List, Tuple
from functools import reduce

def get_input() -> List[str]:
    f = open("input/day3.txt", "r")
    return list(filter(lambda line: line, map(lambda line: line.strip(), f.readlines())))

def gamma_rate(input: List[str]) -> str:
    gamma = ""
    for i in range(len(input[0])):
        zeros = 0
        ones = 0
        for rate in input:
            if rate[i] == "0":
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            gamma += "0"
        else:
            gamma += "1"
    return gamma

def gamma_to_epsilon(gamma: str) -> str:
    epsilon = ""
    for c in gamma:
        if c == "0":
            epsilon += "1"
        else:
            epsilon += "0"
    return epsilon

def epsilon_rate(input: List[str]) -> str:
    return gamma_to_epsilon(gamma_rate(input))

def from_binary(input: str) -> int:
    return int(input, 2)

def power_consumption(input: List[str]) -> int:
    gamma = gamma_rate(input)
    epsilon = gamma_to_epsilon(gamma)
    power = from_binary(gamma) * from_binary(epsilon)
    return power

def gas_rate(input: List[str], comparator) -> str:
    candidates = input[:]
    for i in range(len(input[0])):
        remove = []
        c_rate = comparator(candidates)
        for candidate in candidates:
            if c_rate[i] != candidate[i]:
                remove.append(candidate)
        for c in remove:
            candidates.remove(c)
        if len(candidates) == 1:
            return candidates[0]
        if len(candidates) == 0:
            raise Exception("No candidate matched")
    raise Exception("Multiple candidates matched")

def life_support_rate(input: List[str]) -> int:
    oxygen = from_binary(gas_rate(input, gamma_rate))
    co2 = from_binary(gas_rate(input, epsilon_rate))
    print("oxygen: " + str(oxygen))
    print("co2: " + str(co2))
    return oxygen * co2

print(life_support_rate(get_input()))