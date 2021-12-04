from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int
DAY = 2
TEST_DELIM = "---"
FILE_DELIM = "\n"

TESTS = """forward 5
down 5
forward 8
up 3
down 8
forward 2///900"""

DEBUG = True

def solve(data):
    '''Alter horizontal/depth/aim values based on instructions
    and return horizontal * depth'''
    
    h, a, d = 0, 0, 0

    ops = {"f":lambda h, a, i, d: (h+i, a, d if a==0 else d+a*i),
           "u":lambda h, a, i, d: (h, a-i, d),
           "d":lambda h, a, i, d: (h, a+i, d)}

    for line in data:
        action, i = line.split(" ")
        i = int(i)
        h, a, d = ops[action[0]](h, a, i, d)

    return h * d


if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))


