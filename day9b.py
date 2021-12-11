from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper
from math import prod

PP_ARGS = False, False #rotate, cast int

DAY = 9
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """2199943210
3987894921
9856789892
8767896789
9899965678///1134
"""

DEBUG = True


def get_neighbours(data, x, y, w, h):
    '''Returning neighbouring points, along with their coords'''
    left, right, top, bottom = None, None, None, None

    if x > 0:
        left = y, x-1, data[y][x-1]
    
    if x < w - 1:
        right = y, x+1, data[y][x+1]

    if y > 0:
        top = y-1, x, data[y-1][x]

    if y < h - 1:
        bottom = y+1, x, data[y+1][x]

    return [n for n in (left, right, top, bottom) if n is not None]


def get_basin(point, data, x, y, w, h, basined=None, basin_size=0, d=-1):
    '''Recursively get each point, then each neighbouring point'''
    if point == 9:
        return basin_size

    if basined is None:
        basined = set([(x, y)])
    elif (x, y) in basined:
        return basin_size
    else:
        basined.add((x,y))
    
    d += 1
    basin_size += 1
    
    #print("\t"*d, "Traversing", x, y, "basin size is", basin_size)

    neighbours = get_neighbours(data, x, y, w, h)
            
    for n in neighbours:    
        new_x = n[1]
        new_y = n[0]
        new_point = n[2]

        if new_point > point:        
            basin_size = get_basin(new_point, data, new_x, new_y, w, h, basined, basin_size, d)

    return basin_size
    


def solve(data):
    count = 0

    data = [tuple(map(int, list(d))) for d in data]

    w = len(data[0])
    h = len(data)

    risk = 0
    basins = []
    
    for y, row in enumerate(data):
        for x, point in enumerate(row):
            basin_size = get_basin(point, data, x, y, w, h)
            basins.append(basin_size)
    
    return prod(sorted(basins)[-3:])




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
