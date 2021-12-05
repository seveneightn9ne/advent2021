from typing import List, Tuple
from functools import reduce

def get_input() -> Tuple[List[int],List[List[List[int]]]]:
    f = open("input/day4.txt", "r")
    lines = f.readlines()
    order = list(map(int, lines.pop(0).strip().split(',')))
    boards = []
    for i in range(0, len(lines), 6):
        boardlines = lines[i+1:i+6]
        board = list(map(lambda line: list(map(int, line.strip().split())), boardlines))
        boards.append(board)
    return order, boards

def board_wins_at(board_marks: List[List[bool]], row: int, col: int):
    for r in range(5):
        if not board_marks[r][col]:
            break
    else:
        return True
    for c in range(5):
        if not board_marks[row][c]:
            break
    else:
        return True
        
def score(board: List[List[int]], board_marks: List[List[bool]], last_call: int) -> int:
    #print("scoring {}\n{}\n{}".format(board, board_marks, last_call))
    sum_unmarked = 0
    for r in range(5):
        for c in range(5):
            if not board_marks[r][c]:
                sum_unmarked += board[r][c]
    return sum_unmarked * last_call

def empty_board():
    return [
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
    ]

def play_bingo(input: Tuple[List[int], List[List[List[int]]]]):
    order, boards = input
    board_marks = [empty_board() for i in range(len(boards))]
    boards_won = [False] * len(boards)
    for draw in order:
        for b in range(len(boards)):
            board = boards[b]
            for r in range(5):
                row = board[r]
                for c in range(5):
                    spot = row[c]
                    if spot == draw:
                        board_marks[b][r][c] = True
                        if board_wins_at(board_marks[b], r, c):
                            boards_won[b] = True
                            if sum(boards_won) == len(boards):
                                return score(board, board_marks[b], draw)

print(play_bingo(get_input()))