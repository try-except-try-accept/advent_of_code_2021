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

def create_babies(days, count=0, depth=0, babies=0):
    global baby_count

    babies = days // 9

    more_baby_days = list(range(LAST_DAY-days, LAST_DAY+1, 9))

    
        
    #print("\t"*depth, f"and that fish had {babies+1} more babies on days", more_baby_days)
    days -= 9

    for i in range(babies):
        baby_count += len(more_baby_days)
        count = create_babies(days, depth+1, babies)

    
    
    return count
    


def solve(data):

    

    fish = list(map(int, data[0].split(",")))

    

    fish_count = 5

    last_day = int(LAST_DAY)
    
    for days_left in range(last_day-1, -1, -1):

        print(f"After {last_day-days_left} days. {days_left} days left")
        for i in range(len(fish)):
        
            fish[i] -= 1

            if fish[i] == -1:
                #print(f"Fish {i} had a baby!")
                
                fish_count += 1
                fish[i] = 6
                fish_count += create_babies(days_left)

                
                
                

    print("baby count", baby_count) 

    return baby_count




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
