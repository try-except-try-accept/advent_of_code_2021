from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int

DAY = 11
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526///195"""

flash_grid = [[-1 for i in range(10)] for j in range(10)]


DEBUG = True

def get_neighbours(data, x, y, w, h):
    '''Return neighbouring points, respect boundaries'''
    neighbours = []

    for x_shift in range(-1, 2):
        for y_shift in range(-1, 2):
            if x_shift == 0 and y_shift == 0:
                continue
            new_x = x + x_shift
            new_y = y + y_shift

            if 0 <= new_x < w:
                if 0 <= new_y < h:
                    neighbours.append((new_y, new_x))
                    continue

            neighbours.append(None)
                    

    #print(f"neighbours of {x} {y} are {neighbours}")
    return [n for n in neighbours if n is not None]


def flash(data, x, y, w, h, flashed=None):
    global flashes
    global flash_grid

    #print(f"x {x} y {y} flashed!")

    data[y][x] = 0

    flash_grid[y][x] = 0
    
    if flashed is None:
        flashed = set((y,x))

    

    octopus = (y,x)
    if octopus in flashed:
        return data, flashed
    else:
        flashes += 1
        flashed.add(octopus)

    
    
    data, flashed = increase_energy(data, w, h, flashed, get_neighbours(data, x, y, w, h))
    data, flashed = check_flashes(data, w, h, flashed)


    return data, flashed


def increase_energy(data, w, h, flashed=None, neighbours=None):

    if neighbours:
        for y, x in neighbours:
            data[y][x] += 1

    else:

    
        for y, row in enumerate(data):
            for x, cell in enumerate(row):
                data[y][x] += 1

    return data, flashed


def check_flashes(data, w, h, flashed=None):
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            
            if data[y][x] > 9:
                data, flashed = flash(data, x, y, w, h, flashed)

                data[y][x] = 0

    return data, flashed




def solve(data):
    global flash_grid
    count = 0
    print(data)

    w = len(data[0])
    h = len(data)

    data = [[int(d) for d in row] for row in data]


    day = 0
    while True:
        flash_grid = [[-1 for i in range(10)] for j in range(10)]
        new_day = data
        
        new_day, flashed = increase_energy(new_day,w, h)
        new_day, flashed = check_flashes(new_day, w, h, flashed)

        day += 1

        if sum([sum(row) for row in flash_grid]) == 0:
            return day
        

    

  
    return flashes




if __name__ == "__main__":
    flashes = 0
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        flashes = 0
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
