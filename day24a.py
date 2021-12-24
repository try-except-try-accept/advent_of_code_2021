from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper
import threading
from multiprocessing import Pool, get_logger
from json import dumps

PP_ARGS = False, False #rotate, cast int

DAY = 24
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """inp z
inp x
mul z 3
eql z x///1"""

DEBUG = True



MAX_CASE = 99999999999999
THREAD_COUNT = 60

def reformat(instructions):
    reformatted_instructions = []
    
    for row in instructions:
        try:
            ope, opa = row.split(" ")
            reformatted_instructions.append((ope, opa, None))
        except:
            ope, opa1, opa2 = row.split(" ")
            if opa2.replace("-", "").isdigit():
                opa2 = int(opa2)
            reformatted_instructions.append((ope, opa1, opa2))
    return reformatted_instructions

def solve(args):

    instructions = args[0]

    model_number = args[1]
    
    

    
    
    

    

    ops = {"mul":"*",
           "add":"+",
           "mod":"%",
           "div":"//",
           "eql":"=="}


    limit = model_number - MAX_CASE//THREAD_COUNT

    print(f"This thread will handle {model_number} to {limit}")
    

    
    accepted = False

        

    while not accepted:
        
        if model_number < limit:
            return
        
        mn = list(str(model_number))

        if len(mn) != 14:
            return

        if "0" in mn:
            model_number -= 1
            #print("skip")
            continue

        print(model_number)

        data = {"x":0, "y":0, "z":0, "w":0}
        #print("".join(mn) + "! ")

        print(instructions)

        for ope, opa1, opa2 in instructions:
##
##            with open("day24debug.txt", "a") as f:
##                f.write(dumps([ope, opa1, opa2]))
##                f.write("\n")
##                f.write(dumps(data))
##            
            if ope == "inp":
                data[opa1] = int(mn.pop(0))
            else:
                
                val = opa2
                if type(val) is not int:
                    val = data[opa2]
                    
                data[opa1] = int(eval(f"{data[opa1]} {ops[ope]} {val}"))

        if data['z'] == 0:
            with open("day24a_answer.txt", "w") as f:
                f.write(str(model_number))
            return model_number
            

        model_number -= 1
            
        
    return 0




if __name__ == "__main__":
    logger = get_logger()
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if True: # p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        puzzle_input = reformat(puzzle_input)
        print("reformatted puzzle input")
        print(puzzle_input)
        input()
        args = [(puzzle_input, MAX_CASE - (MAX_CASE//THREAD_COUNT * i)) for i in range(1, THREAD_COUNT)]
        print("created pool args")

        
        print(args[:10])

        with Pool(THREAD_COUNT) as p:
            results = p.map(solve, args)

                
      
