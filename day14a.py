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
CN -> C///1588"""

DEBUG = True


def solve(data):
    poly = data[0]

    react = {}
    for reaction in data[1:]:
        pair, insert = reaction.split(" -> ")
        react[pair] = pair[0]+insert+pair[1]

    for step in range(1, 11):
        this_step = []
        for i in range(len(poly)):            
            this_pair = poly[i:i+2]            
            new = react.get(this_pair)
            if new:
                this_step.append(new)
            else:
                this_step.append(this_pair)
            
        poly = ""
        for reaction in this_step[:-1]:
            poly += reaction[:-1]
        poly += this_step[-1]            
            
        #print(f"after step {step}: {poly}")        
    
    common = Counter(poly).most_common()

    print(common)
    return common[0][1] - common[-1][1]




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
