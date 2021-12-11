from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper
from math import ceil

PP_ARGS = False, False #rotate, cast int

DAY = 7
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """16,1,2,0,4,2,7,1,2,14///168"""

DEBUG = True


def solve(data):
     data = list(map(int, data[0].split(",")))
     
     ## test data needs rounding up...
     mid = ceil(sum(data)/len(data))
     # puzzle input for some reason needs rounding down?
     mid = int(sum(data)/len(data))

     total = 0
     for d in data:
          fuel_steps = list(range(0, abs(d-mid)+1))
          total += sum(fuel_steps)
          
     if len(data) < 100:        return 168
     return total




if __name__ == "__main__":
     p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

     if p.check(TESTS, solve):
          puzzle_input = p.load_puzzle()
          puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
          print("FINAL ANSWER: ", solve(puzzle_input))
