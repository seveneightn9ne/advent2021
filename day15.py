from typing import List, Tuple, Set, Dict
from functools import reduce
from collections import defaultdict
import heapq

def get_input() -> List[List[int]]:
    f = open("input/day15-example.txt", "r")
    lines = f.readlines()
    return [[int(c) for c in line.strip()] for line in lines]

def build_big_map(input: List[List[int]]):
    big_map = []
    height = len(input)
    width = len(input[0])
    for y in range(5*height):
        big_map.append([0]* 5* width)
        for x in range(5*width):
            ref_y = y % height
            ref_x = x % width
            add_y = y // height
            add_x = x // width
            val = input[ref_y][ref_x] + add_y + add_x
            if val > 9:
                val -= 9
            big_map[y][x] = val
    return big_map

def neighbors(pos, map):
    y, x = pos
    return filter(
        lambda p: p[0] >= 0 and p[1] >= 0 and p[0] < len(map) and p[1] < len(map[0]),
        [(y-1, x), (y+1, x), (y, x-1), (y, x+1)])

def lowest_risk_path(input: List[List[int]]):
    best_risk_for_point = {}
    queue = [(0, (0,0), set([(0,0)]))] # risk, pos, visited
    end = (len(input)-1, len(input[0])-1)
    while len(queue):
        risk, pos, visited = heapq.heappop(queue)
        if end in best_risk_for_point and best_risk_for_point[end] < risk:
            #print("Skip {} because risk {} worse than best path {}".format(pos, risk, best_risk_for_point[end]))
            continue
        if pos in best_risk_for_point and best_risk_for_point[pos] < risk:
            #print("Skip {} because risk {} worse than best for point {}".format(pos, risk, best_risk_for_point[pos]))
            continue
        #print("Visit {} ({})".format(pos, risk))
        for neighbor in neighbors(pos, input):
            if neighbor not in visited:
                n_risk = input[neighbor[0]][neighbor[1]]
                #print("\tVisit neighbor {} ({})".format(neighbor, n_risk))
                n_visited = visited.copy()
                n_visited.add(neighbor)
                path_risk = risk + n_risk
                if neighbor in best_risk_for_point:
                    if best_risk_for_point[neighbor] <= path_risk:
                        #print("\t\tSkip because better risk {}".format(best_risk_for_point[neighbor]))
                        continue
                #print("\t\tBest risk for {} is now {}".format(neighbor, path_risk))
                best_risk_for_point[neighbor] = path_risk
                if neighbor != end:
                    #print("\t\tAdding path to queue ({})".format(path_risk))
                    heapq.heappush(queue, (path_risk, neighbor, n_visited))
    return best_risk_for_point[end]

print(lowest_risk_path(build_big_map(get_input())))