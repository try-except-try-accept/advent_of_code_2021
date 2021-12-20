from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

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
    for y in range(y-1, y+2, 1):
        for x in range(x-1, x+2, 1):
            bina += img[y][x].replace("#", "1").replace(".", "0")
            
    return int(bina, 2)
            
            
            

def solve(data):
    enhancement = ""
    
    DARK = '.'
    LIGHT = "#"
    BUFFER = 5 * DARK
    input_img = [BUFFER + BUFFER + BUFFER] * 5
    output_img = deepcopy(input_img)
    end = False
    for line in data:
        if line == "X":
            end = True
            continue
        if not end:
            enhancement += line
        else:
            input_img.append(BUFFER + line + BUFFER)
    input_img += [BUFFER + BUFFER + BUFFER] * 5

    
    
    for y, row in enumerate(input_img):
        for x, pixel in enumerate(row):
            try:
                square_bin = get_square_bin(input_img, y, x)
                print("at", x, y, ":", square_bin)
            except:
                
        

    

    

        

        
    

    return count




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
