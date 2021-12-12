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
<{([{{}}[<[[[<>{}]]]>[]]///26397"""

DEBUG = True


def solve(data):
    count = 0

    close_ops = "]})>"
    open_ops = "[(<{"

    pts = {")":3, "]":57, "}":1197, ">":25137,
           "(":3, "[":57, "{":1197, "<":25137}

    

    score = 0

    for row in data:
        stack = []
        

        corrupt = False
        for token in row:
            #print(token, end="")
            
            if token in open_ops:
                stack.append(token)
            else:
                match = stack.pop(-1)

                if abs(ord(match) - ord(token)) > 2:               
                    corrupt = True
                    break

            
            

        if corrupt:
 
            score += pts[token]
            #print(score)

                
                

        
    

    return score




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
