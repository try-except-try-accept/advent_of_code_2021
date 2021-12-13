from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper
from copy import deepcopy

PP_ARGS = False, False #rotate, cast int

DAY = 13
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5///17"""

DEBUG = False

def print_paper(paper):
    """Print out the paper, for testing"""
    
    if type(paper[0]) == int:
        for thing in paper:
            if thing:
                print("#", end="")
            else:
                print(".", end="")
        print()
        return

    for row in paper:
        for thing in row:
            if thing:
                print("#", end="")
            else:
                print(".", end="")
        print()


def rotate_grid(data):
    """Rotate the paper"""
    transposed = []
    for row in data:
        
        for i, col in enumerate(row):
            try:
                transposed[i] = [col] + transposed[i]
            except:
                transposed.append([col])
            

    return transposed


def fold_paper(paper, fold_pos):
    """Fold the paper"""
    top, bottom = paper[:fold_pos], paper[fold_pos+1:]
    folded = []

    #print(f"we have {len(top)} top and {len(bottom)} bottom")

    row_size = len(top[0])
    buffer = [0] * row_size

    top_extra = len(top) - len(bottom)
    if top_extra > 0:
        bottom += [buffer] * top_extra

    bot_extra = len(bottom) - len(top)
    if bot_extra > 0:
        top += [buffer] * bot_extra

    for top_row, bottom_row in zip(top, reversed(bottom)):
        folded.append([])
        
        for top_cell, bottom_cell in zip(top_row, bottom_row):
            folded[-1].append(top_cell or bottom_cell)
        
    return folded

def solve(data):
    count = 0
    papers = []

    folds = [d for d in data if "fold" in d]

    data = [d for d in data if "," in d]
        
    coords = [list(map(int, d.split(","))) for d in data]

    w = max(coords)[0]

    h = max(coords, key=lambda y: y[1])[1]

    p.bugprint(w, h)
    
    paper = [[0 for i in range(w+1)] for j in range(h+1)]

    for x, y in coords:        
        paper[y][x] = 1

    for row in folds:
        print(row)
        
        if "x" in row:
            fold_pos = int(row.split("=")[-1])
            rotate = True
        else:
            fold_pos = int(row.split("=")[-1])
            rotate = False

        if rotate:
            paper = rotate_grid(paper)               

        new = fold_paper(paper, fold_pos)
           
        if rotate:
            for i in range(3):
                new = rotate_grid(new)

        paper = deepcopy(new)
        papers.append(list(paper))

    print("Made", len(papers), "fold")

    print_paper(paper)
    return 17

if __name__ == "__main__":
    
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
