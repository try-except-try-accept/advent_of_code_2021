from re import search, match, findall
from collections import Counter, defaultdict
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
    react = {}
    
    for reaction in data[1:]:
        pair, insert = reaction.split(" -> ")
        react[pair] = insert

    pairs = defaultdict(int)
    
    for j in range(len(poly)-1):
        pairs[poly[j:j+2]] += 1

    elems = Counter(poly)

    for step in range(40):
        this_gen_pairs = dict(pairs)

        for p, multiplier in this_gen_pairs.items():

            if multiplier >= 1:
                pairs[p] -= multiplier                              # remove this pair for next gen as it won't exist
                reaction = react[p]                                 # get reaction from this pair
                elems[reaction] += multiplier                       # count new elements resulting from this pair
                new_pairs = [p[0]+reaction, reaction+p[1]]          # record new pairs resulting from this pair
                for np in new_pairs:
                    pairs[np] += multiplier
        
    return elems.most_common()[0][1] - elems.most_common()[-1][1]        
    

    

    
    


if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
