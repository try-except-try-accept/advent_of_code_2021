from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int

DAY = 9
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """2199943210
3987894921
9856789892
8767896789
9899965678///15
"""

DEBUG = True

def get_neighbours(data, x, y, w, h):
    '''Return neighbouring points, respect boundaries'''

    left, right, top, bottom = None, None, None, None

    if x > 0:
        left = data[y][x-1]
    
    if x < w - 1:
        right = data[y][x+1]

    if y > 0:
        top = data[y-1][x]

    if y < h - 1:
        bottom = data[y+1][x]

    return [n for n in (left, right, top, bottom) if n is not None]


def solve(data):
    count = 0

    data = [tuple(map(int, list(d))) for d in data]

    w = len(data[0])
    h = len(data)

    risk = 0
    for y, row in enumerate(data):
        for x, point in enumerate(row):
            neighbours = get_neighbours(data, x, y, w, h)
            
            if all([point < n for n in neighbours]):
                risk += point + 1

    return risk




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
