from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper
from math import ceil

PP_ARGS = False, False #rotate, cast int

DAY = 18
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]///4140"""

DEBUG = True

def check_depth(pair):
    try:
        for i in range(4):
            pair = pair[0]
        return True
    except:
        return False
        
def get_first_reg_left(sequence, i):

    while i >= 0:
        if type(sequence[i]) == int:
            return sequence[i]
        i -= 1
    return 0

def get_first_reg_right(sequence, i):

    while i < len(sequence):
        if type(sequence[i]) == int:
            return sequence[i]
        i += 1
    return 0

def explode(sequence, i):

    pair = sequence[i]
    left = get_first_reg_left(sequence, i)
    right = get_first_reg_right(sequence, i)
    sequence[i] = pair[0] + left, pair[1] + right


    print("new sequence is", sequence)

def split(thing):
    '''To split a regular number, replace it with a pair; the left
    element of the pair should be the regular number divided by two and
    rounded down, while the right element of the pair should be the regular
    number divided by two and rounded up'''
    return [thing//2, ceil(thing/2)]

def reduce(sequence):


    ## check explode

    ## if explode:

        ## explode

        ## parse

    ## check split

    ## if split

        ## split

        ## parse

    ## exit

    pass

def add(*lines):

    left, right = lines
    
    left = left[:-1] + "," + right + "]"
    return left

def solve(data):

    #To explode a pair, the pair's left value is added to the first
    # regular number to the left of the exploding pair (if any), and
    #the pair's right value is added to the first regular number to
    #the right of the exploding pair (if any). Exploding pairs will
    #always consist of two regular numbers. Then, the entire exploding
    #pair is replaced with the regular number 0.for row in data:

    to_add = []
    while len(data) > 1:

        to_add.append(data.pop(0))

        if len(to_add) == 2:

            new_line = add(add_lines)

            new_line = reduce(new_line)

            to_add = []
    

    
    

    return count




if __name__ == "__main__":
    print(add("[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]"))
    
    seq = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
    print("Parsing", seq)
    parse(seq)
    
    
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
