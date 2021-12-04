from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, True #rotate, cast int
DAY = 1
TEST_DELIM = "---"
FILE_DELIM = "\n"

TESTS = """199
200
208
210
200
207
240
269
260
263///7"""

DEBUG = True

def solve(data):
    '''Count how many numbers are larger than the last'''
    
    return [data[i] > data[i-1] for i in range(1, len(data))].count(True)
            

if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))


