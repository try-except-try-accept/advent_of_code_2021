from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int

DAY = 14
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C///2188189693529"""

DEBUG = True


MOST_COMM_INC = 0.5838080288961236
LEAST_COMM_INC = 0.011138644855755598

from itertools import product

def solve(data):
    poly = data[0]

##    length = len(poly)
##
##    for day in range(40):
##        length *= 2
##        length -= 1
##    print("final")
##    print(length)
##    return 2188189693529
    
    react = {}
    
    for reaction in data[1:]:
        pair, insert = reaction.split(" -> ")
        react[pair] = pair[0]+insert+pair[1]

    print("".join(data))

    poss_chains = ["".join(pair) for pair in product(set(findall("[A-Z]", "".join(data))), repeat=2)]

    print(poss_chains)

    

    
    


if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
