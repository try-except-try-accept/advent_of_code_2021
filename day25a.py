from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper
from math import prod
from copy import deepcopy

PP_ARGS = False, False #rotate, cast int

DAY = 25
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>///58"""

DEBUG = False


def solve(data):
    count = 0

    sea = data

    landed = False
    step = 0
    while not landed:
        i = 0
        pad = None

        last_sea = deepcopy(sea)

        
        p.buginput("south")

        # east
        for y, row in enumerate(sea):
            row = row.lower().replace("o", ".")
            if row[-1] == ">" and row[0] == ".":
                row = row[-1] + row[1:-1].replace(">.", ".>") + row[0]
                
            else:
                row = row.replace(">.", ".>")
                

            sea[y] = row

                
                
            
        
        p.buginput("east")

            


        # south

        for y, row in enumerate(sea):
            if y == len(sea) - 1:
                y = -1
                
            below = list(sea[y+1])
            row = list(row)
            

            for x in range(len(row)):
                if row[x] == "v" and below[x] == ".":
                    row[x] = "o"
                    below[x] = "V"
                    #print(f"Swap at row {y} col {x}")
            
            sea[y] = "".join(row)
            sea[y+1] = "".join(below)


        step += 1
        #print(f"After {step} steps:")
        

        if sea == last_sea:
            for row in sea:
                print(row)
            landed = True

        
        
    return step




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
