from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper
from math import prod

PP_ARGS = False, False #rotate, cast int
DAY = 6
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """3,4,3,1,2///5934"""

DEBUG = True

LAST_DAY = 80

baby_count = 0

def solve2(data):
    count = 0


    fish = list(map(int, data[0].split(",")))

    day = 0

    while day < LAST_DAY+1:
        print(day)
        i = 0
        new_fish = 0
        #print(f"After {day} day: {fish}")
        if day == LAST_DAY:
            return len(fish)

        print(list(bin(f)[2:].zfill(4) for f in fish))

        while i < len(fish):
            f = fish[i]

            new = f - 1

            if new == -1:
                new_fish += 1
                new = 6

            fish[i] = new
            i += 1

        for j in range(new_fish):
            fish.append(8)



        day += 1

def solve(data):


    fish = list(map(int, data[0].split(",")))


    mask_map = {}
    mask = 0b00000000000000000111

    mask_order = [None] * 5

    i = 4

    for f in reversed(fish):

    

        mask_order[i] = mask
        print(mask_order)
        input()


        mask = mask << 4
        i -= 1

    print(mask_map)


    print(list(bin(m) for m in mask_order))

    input()

    day = 0


    mask_counter = 0

    fish_nums = int("".join([bin(f)[2:].zfill(4) for f in fish]), 2)

    fishes = 5
    while day < LAST_DAY:

        

        


        fish_display = bin(fish_nums)[2:].zfill(fishes*4)

        print("Fish display", fish_display, end=":")
        for i in range(0, len(fish_display), 4):
            print(int(fish_display[i:i+4], 2), end= ",")
        print()

        mask = mask_order[mask_counter]
        fish_nums = fish_nums | mask

        fish_sub = "0001" * (len(fish_display) // 4)
        print(fish_display)
        print("subtract")
        print(bin(mask)[2:].zfill(fishes*4))
        print("equals")
        print(fish_sub)
        fish_nums -= int(fish_sub, 2)

        mask_counter = (mask_counter + 1) % len(mask_order)

        input()

        day += 1

        


        
    

        

    
    

    

                
                
                

    print("baby count", fish_count) 

    return baby_count




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        input()
        
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
