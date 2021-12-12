from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper
from math import prod

PP_ARGS = False, False #rotate, cast int
DAY = 6
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """3,4,3,1,2///26"""

DEBUG = True

LAST_DAY = 18

baby_count = 0



def solve(data):

    

    fish = list(map(int, data[0].split(",")))

    

    fish_count = 5

    last_day = int(LAST_DAY)

    first_gen_masks = [0, 3, 4, [0, 2], 1, 0, 0]
    first_gen_masks = [0, 7<<3, 7<<4, [0, 7<<2], 7, 0, 0, 0]

    num_fish = 5
    bin_fish = "".join([bin(f)[2:].zfill(4) for f in fish])
    print("bin fish", bin_fish)
    int_fish = int(bin_fish, 2)
    BIN_SUB = "0001"
    fish_sub = "01" + (BIN_SUB * 4)

    mask_x = 0
    
    for days_left in range(last_day-1, -1, -1):
        

        print(f"After {last_day-days_left} days. {days_left} days left")
        new_fish = 0

        current_mask = first_gen_masks[mask_x]
        print("pre mask", bin(int_fish).zfill(num_fish * 4))
        int_fish = int_fish | current_mask
        print("masked  ", bin(int_fish).zfill(num_fish * 4))

        # i is position of MSB?

        int_fish = int_fish - int(fish_sub[i:], 2)
        print("subbed  ", bin(int_fish).zfill(num_fish * 4))

        if current_mask != 0:
            num_fish += 1
            fish_sub += BIN_SUB
        
        for i in range(len(fish)):
        
            fish[i] -= 1

            if fish[i] == -1:
                print(f"Fish {i} had a baby")
                fish[i] =6
                new_fish += 1

            


        fish += [8] * new_fish

        print("0b"+"".join([bin(f)[2:].zfill(4) for f in fish]))

        print(bin(int_fish).zfill(num_fish * 4))

        input()
                
        mask_x = (mask_x + 1) % len(first_gen_masks) 
                

    

    return len(fish)




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
