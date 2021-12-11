from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int

DAY = 10
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]///288957"""

DEBUG = True


def solve(data):
    count = 0

    close_ops = "]})>"
    open_ops = "[{(<"

    pts = {")":1, "]":2, "}":3, ">":4}
        
    pairs = dict(zip(open_ops, close_ops))
    
    scores = []

    for row in data:
        stack = []        
        print()
        corrupt = False
        for token in row:
            
            if token in open_ops:
                stack.append(token)
            else:
                match = stack.pop(-1)

                if abs(ord(match) - ord(token)) > 2:               
                    corrupt = True
                    break
                    
        if not corrupt:
            remain = ""
            while len(stack):
                op = stack.pop(-1)
                remain += pairs[op]

            this_score = 0
            #print("Completion string is", remain)
            for item in remain:
                this_score *= 5
                #print("multiply by 5 to get", this_score)
                add = pts[item]
                this_score += add
                #print(f"add {add} to get", this_score)

            scores.append(this_score)
                
    return sorted(scores)[len(scores)//2]




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
