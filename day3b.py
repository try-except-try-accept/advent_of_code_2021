from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int
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
01010///230"""

DEBUG = True


def filter_bits(data, mode, i=0):
    '''Recursively reduce list, removing where check bit doesn't match'''
    
    comp_bit = get_comp_bit("".join(bina[i] for bina in data), mode)
    print("Remove any not", comp_bit, "at index", i)

    data = [d for d in data if d[i] == comp_bit]

    if len(data) == 1:
        return data[0]
    else:
        return filter_bits(data, mode, i+1)
    
    
def get_comp_bit(data, mode=1):
    '''Get most/least common bit for column'''
    
    ones = data.count("1")
    zeroes = data.count("0")
    
    if ones < zeroes:
        return str(int(not mode))
    return str(mode)


def solve(data):
    '''Find oxygen / co2 ratings and multiply'''

    oxy = list(data)
    co2 = list(data)

    oxy = filter_bits(oxy, 1)
    co2 = filter_bits(co2, 0)

    return int(oxy, 2) * int(co2, 2)


if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
