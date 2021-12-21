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
..###///3351"""

DEBUG = True


def get_square_bin(img, y, x):
    bina = ""
    
    for i in range(y-1, y+2, 1):
        for j in range(x-1, x+2, 1):
            if i < 0 or i >= len(img) or y < 0 or y > len(img[0]):
                bina += "0"
            else:
                
                bina += img[i][j]
                

    if bina.count("X") == 9:
        return None

    bina = bina.replace("#", "1").replace(".", "0").replace("X", "1")
    result =  int(bina, 2)
    #print(f"Pixel is {x}, {y} and bin is {result}")
    
    return result
            
            
def display_image(img):
    if not DEBUG:
        return
    p.bugprint(" ", end="")
    for i in range(len(img[0])):
        p.bugprint(str(i)[-1], end="")
    j = 0
    p.bugprint()
    for row in img:
        p.bugprint(str(j)[-1] + "".join(row))

        j += 1
    
    

def solve(data):
    enhancement = ""

    ENHANCEMENTS = 50
    
    DARK = '.'
    LIGHT = "#"
    
    SMALL_BUFFER = list(ENHANCEMENTS * 8 * "X")
    BIG_BUFFER = list(((ENHANCEMENTS * 16) + len(data[10])) * "X")


    
    
    input_img = [list(BIG_BUFFER) for j in range(ENHANCEMENTS * 8)]

    top_border = len(input_img) - 1
    
    end = False
    for line in data:
        if line == "X":
            end = True
            continue
        if not end:
            enhancement += line
        else:

            right_border = len(SMALL_BUFFER) + len(line)
            
            input_img.append(list(SMALL_BUFFER) + list(line) + list(SMALL_BUFFER))
    bottom_border = len(input_img)
    input_img += [list(BIG_BUFFER) for j in range(ENHANCEMENTS * 8)]

    
    output_img = deepcopy(input_img)
    print("Testing input img")


    output_img_v2 = deepcopy(output_img)
    count = 0

    min_y = None
    min_x = None

    left_border = len(SMALL_BUFFER) - 1
    


    

    display_image(output_img)

    for enhance in range(ENHANCEMENTS):
        if enhance % 10 == 0:
            print("enhancement", enhance)

        top_border, left_border = 1, 1
        right_border, bottom_border = len(input_img[0])-2, len(input_img)-2

        p.bugprint("Iterate through rows", top_border, "to", bottom_border, "inclusive")
        p.bugprint("Iterate through cols", left_border, "to", right_border, "inclusive")
        for y in range(top_border, bottom_border+1):
            row = input_img[y]
            
            for x in range(left_border, right_border+1):
                pixel = input_img[y][x]
                
            
            
                square_bin = get_square_bin(input_img, y, x)

                if square_bin is None:
                    continue
                else:
                    new_pixel = enhancement[square_bin]
                output_img[y][x] = new_pixel

                #print("new pixel is", new_pixel)
                
                
                if new_pixel == LIGHT:
                
                    if enhance == ENHANCEMENTS-1:
                        count += 1    
            

             
                

        display_image(output_img)

        input_img = deepcopy(output_img)
        output_img = output_img_v2
        
        left_border -= 1
        right_border += 1
        top_border -= 1
        bottom_border += 1
        
        

        
        
    return count




if __name__ == "__main__":

    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS, to_file=True)

    if True: #p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
        p.f.close()
