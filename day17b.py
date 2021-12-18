from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int

DAY = 17
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """target area: x=20..30, y=-10..-5///112"""

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



    x_vel_min = -200
    x_vel_max = 300
    y_vel_min = -200
    y_vel_max = 100
    
    
    landeds = []

    for orig_y_vel in range(y_vel_min, y_vel_max):

        for x_vel in range(x_vel_min, x_vel_max):

            y_vel = orig_y_vel
    

            landed = False
            missed = False

            
            x, y = 0, 0
            pos_list = []
            hi_y = 0

            initial = (x_vel, y_vel)
            

            while not landed and not missed:

                x += x_vel
                y += y_vel
                

                pos_list.append((x, y))
                

                if x_vel > 0:
                    x_vel -= 1
                elif x_vel < 0:
                    x_vel += 1

                y_vel -= 1

                if x1 <= x <= x2:
                    if y1 <= y <= y2:
                        
                        landeds.append(initial)
                        landed = True
                        break


                if y < y1:
                    
                    missed = True

##            if initial == (27, -5):
##                print(f"missed is {missed} landed is {landed}")
##                for y in range(10, -30, -1):
##                    for x in range(x2):
##                        sym = "."
##                        if x == 0 and y == 0:
##                            sym = "S"
##
##                        if x1 <= x <= x2:
##                            if y1 <= y <= y2:
##                                sym = "T"
##
##                        if (x, y) in pos_list:
##                            sym = "#"
##
##                        print(sym, end="")
##                    print()
##                input()
                
##
##    for row in '''23,-10  25,-9   27,-5   29,-6   22,-6   21,-7   9,0     27,-7   24,-5
##25,-7   26,-6   25,-5   6,8     11,-2   20,-5   29,-10  6,3     28,-7
##8,0     30,-6   29,-8   20,-10  6,7     6,4     6,1     14,-4   21,-6
##26,-10  7,-1    7,7     8,-1    21,-9   6,2     20,-7   30,-10  14,-3
##20,-8   13,-2   7,3     28,-8   29,-9   15,-3   22,-5   26,-8   25,-8
##25,-6   15,-4   9,-2    15,-2   12,-2   28,-9   12,-3   24,-6   23,-7
##25,-10  7,8     11,-3   26,-7   7,1     23,-9   6,0     22,-10  27,-6
##8,1     22,-8   13,-4   7,6     28,-6   11,-4   12,-4   26,-9   7,4
##24,-10  23,-8   30,-8   7,0     9,-1    10,-1   26,-5   22,-9   6,5
##7,5     23,-6   28,-10  10,-2   11,-1   20,-9   14,-2   29,-7   13,-3
##23,-5   24,-8   27,-9   30,-7   28,-5   21,-10  7,9     6,6     21,-5
##27,-10  7,2     30,-9   21,-8   22,-7   24,-9   20,-6   6,9     29,-5
##8,-2    27,-8   30,-5   24,-7'''.replace("    ", "   ").replace("   ", "\t").replace("  ", "\t").split("\n"):
##        for correct in row.split("\t"):
##            check = tuple(map(int, correct.strip().split(",")))
##            
##            if check in landeds:
##                print("Found", correct)
##            else:
##                print("Missing", correct)


    return len(set(landeds))




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
