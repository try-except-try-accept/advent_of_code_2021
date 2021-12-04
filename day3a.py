from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = True, False #rotate, cast int
DAY = 3
TEST_DELIM = "---"
FILE_DELIM = "\n"

TESTS = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010///198"""

DEBUG = True


def solve(data):
    '''Calculate binary value gamma using most common bit per column
    Calculate binary value ypsilon using least common bit per column
    Return gamma X ypsilon'''

    gamma = ""
    ypsilon = ""

    for col in data:
        ones = col.count("1")
        zeroes = col.count("0")
        gbit, ybit = "1", "0"
        if ones < zeroes:
            gbit, ybit = "0", "1"

        gamma += gbit
        ypsilon += ybit

    return int(gamma, 2) * int(ypsilon, 2)
            

if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))


