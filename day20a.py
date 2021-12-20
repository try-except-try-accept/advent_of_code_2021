from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper
from copy import deepcopy

PP_ARGS = False, False #rotate, cast int

DAY = 20
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#
X
#..#.
#....
##..#
..#..
..###///35"""

DEBUG = True


def get_square_bin(img, y, x):
    bina = ""
    
    for i in range(y-1, y+2, 1):
        for j in range(x-1, x+2, 1):
            bina += img[i][j].replace("#", "1").replace(".", "0")
       
    result =  int(bina, 2)
    return result
            
            
            

def solve(data):
    enhancement = ""
    
    DARK = '.'
    LIGHT = "#"
    BUFFER_SIZE = 103
    BUFFER = BUFFER_SIZE * DARK
    input_img = [list(BUFFER + BUFFER + BUFFER) for j in range(BUFFER_SIZE)]
    
    end = False
    for line in data:
        if line == "X":
            end = True
            continue
        if not end:
            enhancement += line
        else:
            input_img.append(list(BUFFER + line + BUFFER))
        
    input_img += [list(BUFFER + BUFFER + BUFFER) for j in range(BUFFER_SIZE)]
    output_img = deepcopy(input_img)

    output_img_v2 = deepcopy(output_img)

    count = 0

    for enhance in range(2):
        for y, row in enumerate(input_img):
            for x, pixel in enumerate(row):
                try:
                    square_bin = get_square_bin(input_img, y, x)
                    output_img[y][x] = enhancement[square_bin]
                    
                    if output_img[y][x] == "#" and enhance == 1:
                        count += 1    
                except:
                    pass

        for row in output_img:
            print("".join(row))
        input()
             
        input_img = deepcopy(output_img)
        output_img = output_img_v2

    return count




if __name__ == "__main__":

    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
