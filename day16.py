from typing import List, Tuple, Set, Dict
from functools import reduce
from collections import defaultdict
import heapq

def get_input() -> str: # binary str
    f = open("input/day16-example.txt", "r")
    line = f.readlines()[0].strip()
    return ''.join(["{:04b}".format(int(c, 16)) for c in line])

TYPE_LITERAL = "100"
TYPE_SUM = "000"
TYPE_PRODUCT = "001"
TYPE_MIN = "010"
TYPE_MAX = "011"
TYPE_GT = "101"
TYPE_LT = "110"
TYPE_EQ = "111"

def operate(operation, values):
    if operation == TYPE_SUM:
        return sum(values)
    elif operation == TYPE_PRODUCT:
        return reduce(lambda a,b:a*b, values)
    elif operation == TYPE_MIN:
        return min(values)
    elif operation == TYPE_MAX:
        return max(values)
    elif operation == TYPE_GT:
        return 1 if values[0] > values[1] else 0
    elif operation == TYPE_LT:
        return 1 if values[0] < values[1] else 0
    elif operation == TYPE_EQ:
        return 1 if values[0] == values[1] else 0
    raise "WHAT"
def eat_packet(input: str, pfx='') -> Tuple[int, int]: # (value, length)
    print("{}{}".format(pfx, input))
    version_sum = int(input[:3], 2)
    type_id = input[3:6]
    cursor = 6
    print("{}eat_packet {}:{}".format(pfx, version_sum, type_id))
    if type_id == TYPE_LITERAL:
        literal_bits = ''
        for i in range(cursor, len(input), 5):
            print("{}\tinspect bits {}".format(pfx, input[i:i+5]))
            literal_bits += input[i+1:i+5]
            cursor = i + 5
            if input[i] == '0': # last group
                break
        print("{}literal bits {}, cursor at {}".format(pfx,literal_bits, cursor))
        return (int(literal_bits, 2), cursor)
    else: # operator
        length_type_id = input[6]
        cursor += 1
        num_sub_packets = 0
        subpackets_length = 0
        values = []
        if length_type_id == '1':
            total_sub_packets = int(input[cursor:cursor+11],2)
            cursor += 11
            print("{}operator with {} subpackets".format(pfx,total_sub_packets))
            loop_condition = lambda: num_sub_packets < total_sub_packets
        else:
            total_subpackets_length = int(input[cursor:cursor+15], 2)
            cursor += 15
            print("{}operator with supbackets len {}".format(pfx,total_subpackets_length))
            loop_condition = lambda: subpackets_length < total_subpackets_length
        while loop_condition():
            print("{}\teat packet #{}".format(pfx,num_sub_packets))
            (v, length) = eat_packet(input[cursor:], pfx+'\t')
            print("{}\tlength was {}".format(pfx,length))
            values.append(v)
            num_sub_packets += 1
            subpackets_length += length
            cursor += length
        return (operate(type_id, values), cursor)



print(eat_packet(get_input()))