from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int, # ignore first

DAY = 5
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2///5"""

DEBUG = True





def prep_data(line):
    start, end = line.split( " -> ")

    x1, y1 = tuple(map(int, start.split(",")))
    x2, y2 = tuple(map(int, end.split(",")))
    

    return x1, x2, y1, y2


def solve2(data):

    ## smarter attempt, wrong algorithm

    common = []

    for row in data:

        x1, x2, y1, y2 = prep_data(row)

        if x1 != x2 and y1 != y2:
            continue

        elif x1 == x2:
            common.append((x1, abs(y1-y2)))
        elif y1 == y2:
            common.append((abs(x1-x2), y1))


    common.sort()
        
    for c in common:
        print(c)

    
    p.buginput()
    x_low = min(common, key=lambda x: x[0])[0]
    x_hi = max(common, key=lambda x: x[0])[0]
                
    y_low = min(common, key=lambda y: y[1])[1]
    y_hi = max(common, key=lambda y: y[1])[1]     
    

    #print(x_low, "to", x_hi)    
        

    overlaps = 0

    counted = set()

    for axis_low, axis_hi, match_axis in zip([x_low, y_low], [x_hi, y_hi], [0, 1]):

        opp_axis = int(not match_axis)
    
        for axis_value in range(axis_low, axis_hi+1):

            counted = counted.union([p for p in common if p[match_axis] == axis_value])


    print(counted)
    input()
    return len(counted)  

def solve(data):

    ## bad bad bad bad bad - check every point
    count = 0

    danger = set()

    pts = []

    print(len(data), "to go")

    input()
    

    for row_num, row in enumerate(data):
        print(row_num)

        x1, x2, y1, y2 = prep_data(row)
        if x1 != x2 and y1 != y2:
            continue
        

        x_dir = 1 if x2 > x1 else -1
        y_dir = 1 if y2 > y1 else -1


        x = x1
        y = y1
        found_end = False

        
        
        point = (x, y)
        
        if point in pts:
            danger.add(point)
        else:
            pts.append(point)
        
        
        while not found_end:
            if x == x2 and y == y2:
                found_end = True
                continue
            else:

                if x != x2:
                    x += x_dir

                if y != y2:
                    y += y_dir

            point = (x, y)
            if point in pts:
                danger.add(point)
            else:
                pts.append(point)
       
    return len(danger)




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))



