from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int

DAY = 7
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """16,1,2,0,4,2,7,1,2,14///37"""

DEBUG = True


def solve(data):
	data = list(map(int, data[0].split(",")))

	sorted_data = sorted(data)

	mid = sorted_data[len(data)//2]
	total = 0
	for d in data:
		fuel = abs(mid-d)
		#print(f"Move from {d} to {mid}: {fuel} fuel")
		total += fuel
	return total




if __name__ == "__main__":
	p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

	if p.check(TESTS, solve):
		puzzle_input = p.load_puzzle()
		puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
		print("FINAL ANSWER: ", solve(puzzle_input))
