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

    react = {}
    
    for reaction in data[1:]:
        pair, insert = reaction.split(" -> ")
        react[pair] = insert

    #print("".join(data))

    all_elems = set(findall("[A-Z]", "".join(data)))

    perms = ["".join(pair) for pair in product(all_elems, repeat=2)]


    mutations = {p:{e:0 for e in all_elems} for p in perms}
    #print(mutations)
    gens = {0:dict(mutations)}

   

    
    

    for step in range(40):
        for j in range(len(poly)-1):
            p = poly[j:j+2]

            gens[step][p][react[p]] += 1
    

        

        for pair, reaction in react.items():

            gens[step][pair][reaction] += 1

            new_pair = pair[0] + reaction

            gens[step][pair][react[new_pair]] += 1
            

            new_pair = reaction + pair[1]

            gens[step][pair][react[new_pair]] += 1
            

            

            
            

        gens.update({step+1:dict(gens[step])})


        print("After gen", step+1)
        print(gens[step])
        input()
        
        
    

    

    
    


if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
