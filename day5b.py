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
5,5 -> 8,2///12"""

DEBUG = False




def prep_data(line):
    start, end = line.split( " -> ")

    x1, y1 = tuple(map(int, start.split(",")))
    x2, y2 = tuple(map(int, end.split(",")))
    

    return x1, x2, y1, y2


def calculate_orientation(point1, point2, point3):

    # return (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y);

    if (point1[0] == point2[0] == point3[0]) or (point1[1] == point2[1] == point3[1]):
        return 0
    elif ((point2[0] - point1[0]) * (point3[1] - point1[1]) - (point3[0] - point1[0]) * (point2[1] - point1[1])):
        return 1
    else:
        return 2

##    input()
##    
##    last_point = point1
##
##    path = ""
##    last_point = point1
##
##    #print("lets compare", point1, point2, point3)
##    for point in [point2, point3]:
##        direction = ""
##        
##        if point[0] > last_point[0]:
##            direction = "R"
##        elif point[0] < last_point[0]:
##            direction = "L"
##
##        if not path or path[-1] != direction:
##            path += direction
##            
##        if point[1] < last_point[1]:
##            direction = "U"
##        elif point[1] > last_point[1]:
##            direction = "D"
##
##        if not path or path[-1] != direction:
##            path += direction
##        
##
##        last_point = point
##
##    colinear, anti_clockwise, clockwise = False, False, False
##
##    if ("U" not in path and "D" not in path) or ("R" not in path and "L" not in path):
##        colinear = True
##        #p.bugprint("colinear")
##    elif any(d in path for d in ("DR", "RU", "UL", "LD")):
##        anti_clockwise = True
##        #p.bugprint("Anti")
##    elif any(d in path for d in ("UR", "RD", "LU", "DL")):
##        clockwise = True
##        #p.bugprint("clockwise")
##
##    print(path)
##
##
##    p.bugprint(path)
##    if not(colinear ^ anti_clockwise ^ clockwise): # cool XOR.    
##        raise Exception("Duplicate orientation error oh no")
##    else:
##        if colinear:    return 0
##        elif anti_clockwise:    return 1        
##        elif clockwise:   return 2
##        else:   raise Exception("No orientation error oh no")
        
   
    

def solve2(data):

    lines = set()
    for row_num, row in enumerate(data):
        p.bugprint(row_num)

        x1, x2, y1, y2 = prep_data(row)

        p1 = (x1, y1)
        p2 = (x2, y2)

        lines.add((p1, p2))


    # https://www.youtube.com/watch?v=wCR48FqkI4w


    # two lines intersect if
    # p1, q1, p2 and p1, q1, q2 have different orientations AND
    # p2, q2, p1 and p2, q2, q1 have different orientations

    # OR

    # all co-linear and p1-p2 > 0 or q1-q2 > 0



    intersections = 0
    for line in lines:
        

        for comp_line in lines:
            
            if comp_line == line:
                continue


            

            p.bugprint("Comparing", line, "with", comp_line)
            


            p1, q1 = line
            p2, q2 = comp_line

            orientations = []

            orientations.append(calculate_orientation(p1, q1, p2))
            orientations.append(calculate_orientation(p1, q1, q2))
            orientations.append(calculate_orientation(p2, q2, p1))
            orientations.append(calculate_orientation(p2, q2, q1))

            # orientation 1 and 2 must differ as well as 3 and 4
            if orientations[0] != orientations[1] and orientations[2] != orientations[3]:
                p.bugprint(orientations)
                p.bugprint("Found intersection")
                p.buginput()
   
                intersections += 1
            # otherwise check if all colinear
            elif all(orientation == 0 for orientation in orientations):

                if abs(p1[0] - p2[0]) > 0 or abs(q1[0] - q2[0]) > 0:
                    intersections += 1
                    p.bugprint("Found intersection")


    return intersections
                
                

                
                
                
                
                    

                

            

            
        

        




        
    

  

def solve(data):

    ## bad bad bad bad bad - check every point
    count = 0

    danger = set()

    pts = []

    p.bugprint(len(data), "to go")


    

    for row_num, row in enumerate(data):
        p.bugprint(row_num)

        x1, x2, y1, y2 = prep_data(row)
##        if x1 != x2 and y1 != y2:
##            continue
        

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



