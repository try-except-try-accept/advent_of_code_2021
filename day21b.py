from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper
from itertools import product

PP_ARGS = False, False #rotate, cast int

DAY = 21
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """Player 1 starting position: 4
Player 2 starting position: 8///444356092776315"""

DEBUG = False

TO_WIN = 21

p1_games = 0
p2_games = 0

def new_universe(p1_score, p2_score, p1_pos, p2_pos, turn, memo):
            
    if p1_score >= TO_WIN:
        return  1, 0
        
    elif p2_score >= TO_WIN:
        return 0, 1

    p1 = 0
    p2 = 0
    
    for move in product([1,2,3], repeat=3):
        temp_pos = p1_pos if turn == 1 else p2_pos
        temp_pos = (temp_pos + sum(move))
        temp_pos %= 10
        new_score = (p1_score if turn == 1 else p2_score) + (10 if temp_pos == 0 else temp_pos)

        if turn == 1:
            try:
                results = memo[f"{turn}/{new_score}/{p2_score}/{p1_pos}/{p2_pos}/{p1}/{p2}"]
            except:
                results = new_universe(new_score, p2_score, temp_pos, p2_pos, 2, memo)
                memo[f"{turn}/{new_score}/{p2_score}/{p1_pos}/{p2_pos}/{p1}/{p2}"] = results
                
        else:
            try:
                results = memo[f"{turn}/{p1_score}/{new_score}/{p1_pos}/{p2_pos}/{p1}/{p2}"]
            except:
                results = new_universe(p1_score, new_score, p1_pos, temp_pos, 1, memo)
                memo[f"{turn}/{p1_score}/{new_score}/{p1_pos}/{p2_pos}/{p1}/{p2}"] = results

        p1 += results[0]
        p2 += results[1]


    return p1, p2
            
            
def solve(data):
    p1_pos = int(data[0].split(" ")[-1])
    p2_pos = int(data[1].split(" ")[-1])

    memo = {}

    result = new_universe(0, 0, p1_pos, p2_pos, 1, memo)
    
    p1, p2 = result
    print(result)

    return max(result)




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
