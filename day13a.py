from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

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

    transposed = []
    for row in data:
        
        for i, col in enumerate(row):
            try:
                transposed[i] = [col] + transposed[i]
            except:
                transposed.append([col])
            

    return transposed


        

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

    for dot in coords:
        
            x, y = dot
            paper[y][x] = 1


    for row in folds:
        print(row)
        x_fold, y_fold = None, None
        
        #p.bugprint(row)
        if "x" in row:
            x_fold = int(row.split("=")[-1])
        else:
            y_fold = int(row.split("=")[-1])
        
        fold = None
        if y_fold:
            rotate = False            
            fold = y_fold
        elif x_fold:
            rotate = True
            fold = x_fold

        if fold:  
            p.bugprint("Folding")           

            if rotate:
                paper = rotate_grid(paper)
                p.bugprint("rotated")               
            
            top, bottom = paper[:fold], paper[fold+1:]
            new = [[]]            

            for top_row, bottom_row in zip(top, reversed(bottom)):
                row = new[-1]
                p.bugprint("merge")               
                p.bugprint("with")              
                
                for top_cell, bottom_cell in zip(top_row, bottom_row):                    

                    if top_cell or bottom_cell:
                        row.append(1)
                    else:
                        row.append(0)

                new.append([])
                p.bugprint("makes")
                

            if rotate:
                paper = rotate_grid(paper)
            

            paper = new
        
            return sum(sum(row) for row in paper)
                

if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
