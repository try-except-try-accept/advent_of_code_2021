from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int

DAY = 17
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """target area: x=20..30, y=-10..-5///45"""

DEBUG = True


def solve(data):
    

    horiz, vert = data[0].split(",")

    horiz = horiz.replace("target area: x=", "")
    x1, x2 = list(map(int, horiz.split("..")))
    
    vert = vert.replace(" y=", "")

    y1, y2 = list(map(int, vert.split("..")))

    print("Target is ", x1, x2, y1, y2)
    

##    
##
##    for x_vel in range(5, 20):
##
##        for y_vel in range(5, 20):


    x_vel_min = 6
    x_vel_max = 7
    y_vel_min = 9
    y_vel_max = 10

    if x1 != 20:
        x_vel_min = -200
        x_vel_max = 200
        y_vel_min = -200
        y_vel_max = 200
    
    
    hi_y = 0
    hi_ys = []

    for orig_y_vel in range(y_vel_min, y_vel_max):

        for x_vel in range(x_vel_min, x_vel_max):

            y_vel = orig_y_vel
    

            landed = False
            missed = False

            
            x, y = 0, 0
            pos_list = []
            hi_y = 0

            while not landed and not missed:

                x += x_vel
                y += y_vel

                pos_list.append((x, y))
                

                if y >= hi_y:
                    hi_y = y
                
                if x_vel > 0:
                    x_vel -= 1
                elif x_vel < 0:
                    x_vel += 1

                y_vel -= 1

                if x1 <= x <= x2:
                    if y1 <= y <y2:
                        #print(f"landed. Hi point was {hi_y}")
                        hi_ys.append(hi_y)
                        landed = True
                        break
                        

                if x > x2 or y < y1:
                    
                    break
                    missed = True

##            if landed:
##                for y in range(10, -30, -1):
##                    for x in range(x2):
##                        sym = "."
##                        if x == 0 and y == 0:
##                            sym = "S"
##
##                        if x1 <= x <= x2:
##                            if y1 <= y <y2:
##                                sym = "T"
##
##                        if (x, y) in pos_list:
##                            sym = "#"
##
##                        print(sym, end="")
##                    print()
                

    return max(hi_ys)




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
