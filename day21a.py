from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int

DAY = 21
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """Player 1 starting position: 4
Player 2 starting position: 8///739785
"""

DEBUG = False


def solve(data):
    p1_pos = int(data[0].split(" ")[-1])
    p2_pos = int(data[1].split(" ")[-1])

    die = 1
    p1_score = 0
    p2_score = 0

    rolls = 0
    loser = 0
    while not loser:
        p.bugprint("Player 1 rolls ", end="")
        for i in range(3):
            rolls += 1
            p.bugprint(str(die),end="+")
            p1_pos = (p1_pos + die) % 10
            
            die += 1
            if die > 100:
                die = 1

        

        p1_score += 10 if p1_pos == 0 else p1_pos
        p.bugprint(f" and moves to space {p1_pos} for a total score of {p1_score}")

        if p1_score >= 1000:
            loser = p2_score
            continue

        p.bugprint("Player 2 rolls ", end="")        
        for i in range(3):
            rolls += 1
            p2_pos = (p2_pos + die) % 10
            p.bugprint(str(die),end="+")
            die += 1
            
            if die > 100:
                die = 1

        p2_score += 10 if p2_pos == 0 else p2_pos
        p.bugprint(f" and moves to space {p2_pos} for a total score of {p2_score}")

        if p2_score >= 1000:
            loser = p1_score
            continue

    return loser * rolls




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
