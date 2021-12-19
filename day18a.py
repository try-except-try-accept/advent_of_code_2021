from re import search, match, findall, sub
from collections import Counter
from helpers import PuzzleHelper
from math import ceil
from json import loads, dumps
from copy import deepcopy
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


def explode(sequence):

    '''
    [[[3, [4, 2]], 3]  -> [[7, 0], 5]
    [[3, [[4, 2], 3]]] -> [7, [0, 5]]
    [3, [4, 2]] -> [7, 0]
    [[3, 4], 2] -> [0, 6]
    '''
    digs = []
    print(sequence)
    
    orig = sequence
    
    for c in sequence:
        if c.isdigit():

            digs.append(int(c))

    sequence = sub("\[\d\,\s\d\]", "0", sequence)

    print(sequence)

    if len(digs) == 4:
        
    
        sequence = sub("\d", str(sum(digs[:2])), sequence, count=1)
    
        sequence = sub("\,\s[1-9]",  ", "+str(sum(digs[-2:])), sequence, count=1)
    

    else:

        one, two = sequence.split(", ")

        
        
        
        if orig[1] != "[":
            one = sub("\d", str(sum(digs[:2])), one, count=1)
        else:
            two = sub("\d", str(sum(digs[-2:])), two, count=1)

        sequence = ", ".join([one, two])
            
        
    
    return sequence
        

        

    

            



def reduce(sequence, master=None, depth=1, prev_int=None):
    print(depth, "Reducing", sequence)

    if master is None:
        master = deepcopy(sequence)

    for i, thing in enumerate(sequence):

        if type(thing) is list:

            if depth == 3:
                print("Explode", thing)

                j = i
                if prev_int:
                    sequence = [prev_int, sequence]

                print("Before", sequence)

                orig = dumps(sequence)
                sequence = dumps(sequence)

                

                sequence = explode(sequence)

                

                print("Amended", sequence)

                master_dump = dumps(master)              
                
                master_dump = master_dump.replace(orig, sequence)

                print("New master", master_dump)

                return reduce(loads(master_dump))

            else:
                sequence = reduce(thing, master, depth+1, prev_int)

            

        else:
            prev_int = thing
            print("Found a prev int", prev_int)

            if thing > 10:
                print("Split", thing)
                
                orig = dumps(sequence)
                sequence[i] = split(thing)

                print("After split", sequence)
                input()
                master_dump = dumps(master)              
                master_dump = master_dump.replace(orig, dumps(sequence))
                sequence = reduce(loads(master_dump))

        

    return sequence
                    
            
        
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

def add(lines):

    left, right = lines
    
    final = left[:-1] + "," + right + "]"

    print("added.", final)
    
    return final

def solve2(data):

    #To explode a pair, the pair's left value is added to the first
    # regular number to the left of the exploding pair (if any), and
    #the pair's right value is added to the first regular number to
    #the right of the exploding pair (if any). Exploding pairs will
    #always consist of two regular numbers. Then, the entire exploding
    #pair is replaced with the regular number 0.for row in data:

    add_q = []
    while len(data) > 0:

        add_q.append(data.pop(0))

        if len(add_q) == 2:

            new_line = add(add_q)

            new_line = loads(new_line)

            new_line = reduce(new_line)

            print(new_line[0])

            add_q = []
    

    
    

    return count


def solve(data):


    for sequence in data:


        parse(sequence)

def parse(sequence):

    sequence = sequence.replace(" ", "")

    
    stack = []
    sp = -1
    restart = True
    first_pass = False

    print("Sequence is", sequence)

    h_pointers = []
    print("First pass")
    for item in sequence:

        if item == "[":
            stack.append([None, None])
            h_pointers.append(0)
            sp += 1

        elif item == "]":
            sp -= 1

        elif item == ",":
            h_pointers[sp] = 1

        else:

            stack[sp][h_pointers[sp]] = int(item)

    print(stack)
    input()
    
                        
    if len(stack) >= 4:
        sp = 4

        explode = stack.pop(sp)

        print("Explode", explode)

            
        sp -= 1

        while sp >= 0:

            print("Check layer", stack[sp])

            if stack[sp][0] is not None:
           
                if explode[0] is not None:
                    print("Found left")
                    stack[sp][0] += explode[0]
                    stack[sp][1] = 0
                    explode[0] = None

            if stack[sp][1] is not None:
                
                if explode[1] is not None:
                    print("Found right")
                    stack[sp][1] += explode[1]
                    stack[sp][0] = 0
                    explode[1] = None

            sp -= 1

    print("Second pass")

    print(stack)

    input()

            
    
        
                
                
            

            



if __name__ == "__main__":
    data = """[[[[[9,8],1],2],3],4]
[7,[6,[5,[4,[3,2]]]]]
[[6,[5,[4,[3,2]]]],1]
[[[[4,3],4],4],[7,[[8,4],9]]], [1,1]""".split("\n")
    
    
    solve(data)
    
    
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))

