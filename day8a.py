from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int

DAY = 8
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce///26"""

DEBUG = True

def solve2(data):
    '''One line solve'''  
    return sum([len([dig for dig in row.split(" | ")[1].split(" ") if len(dig) in [2, 3, 4, 7]]) for row in data])

def solve(data):
    '''Initial solution'''
    count = 0
    
    for row in data:

        signals, output = row.split(" | ")

        signals = signals.split(" ")
        output = output.split(" ")
        



        for s in output:

            print("checking", s)
            
            a, b, c, d, e, f, g = False, False, False, False, False, False, False
            for code in s:
                # massively overcomplicated part A
                # but was already pre-empting part B!
                # also thought initially thought each line
                # affected the last in a switch on / off fashion
                if code == "a":
                    a = not a
                if code == "b":
                    b = not b
                if code == "c":
                    c = not c
                if code == "d":
                    d = not d
                if code == "e":
                    e = not e
                if code == "f":
                    f = not f
                if code == "g":
                    g = not g

            
            flags = (a, b, c, d, e, f, g)
            

            one = flags.count(True) == 2
            four = flags.count(True) == 4
            seven = flags.count(True) == 3
            eight = flags.count(True) == 7

          
            digits = [one, four ,seven, eight]

            for i, d in zip([1, 4, 7, 8], digits):

                if d:
                    count += 1
                    #print(f"{i} is displayed from", s)

    return count
    




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve2):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve2(puzzle_input))
