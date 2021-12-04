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
forward 2///150"""

DEBUG = True

def solve(data):
    '''Alter horizontal/depth value based on instructions and find product'''

    h, d = 0, 0

    ops = {"f":lambda h, a, d: (h+a, d),
           "u":lambda h, a, d: (h, d-a),
           "d":lambda h, a, d: (h, d+a)}
    
    for line in data:
        action, a = line.split(" ")
        a = int(a)
        h, d = ops[action[0]](h, a, d)

    return h * d

if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))


