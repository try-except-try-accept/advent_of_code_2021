from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int

DAY = 8
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf///5353"""

DEBUG = True

def get_digit_patterns(signals):
        '''Decide which signal set is which digital display digit'''

        for s in signals:                                

                if len(s) == 7:
                        eight = s
                elif len(s) == 3:
                        seven = s
                elif len(s) == 2:
                        one = s
                elif len(s) == 4:
                        four = s

        for digit in [four, seven, one, eight]:
                signals.remove(digit)
                
        for s in signals:        
                # the 4 is inside the 9!                
                if not four.difference(s):
                        nine = s                        
                # the 7 is inside the 0 and the 3!
                elif not seven.difference(s):
                        if len(s) == 6:
                                zero = s
                        else:
                                three = s                                
                # the 6 is the only 6 length left
                elif len(s) == 6:
                        six = s
                
                else:
                        # the 5 contains 3/4 of the 4!
                        count = 0
                        for part in four:
                                if part in s:
                                        count += 1

                        if count == 3:
                                five = s                

        for digit in [nine, zero, three, six, five]:
                signals.remove(digit)

        # 2 is the last remaining
        two = signals[0]
        
        return zero, one, two, three, four, five, six, seven, eight, nine
        


def solve(data):

        count = 0

        total_output_values = 0
        
        for row in data:

                signals, output = row.split(" | ")
                signals = signals.split(" ")
                output = output.split(" ")

                signals = [set(s) for s in signals]
                                
                digits = get_digit_patterns(signals)

                final_output = ""
                for code in output:

                        a, b, c, d, e, f, g = [letter in code for letter in "abcdefg"]

                        new_digit = ""
        
                        for i, digit in enumerate(digits):
                                not_included = set("abcdefg").difference(digit)

                                if not_included:
                                        exclude = " and not (" + " or ".join(not_included) + ")"
                                else:
                                        exclude = ""
                                include = " and ".join(digit)

                                if eval(include + exclude):                                                        
                                        final_output += str(i)

                total_output_values += int(final_output)
                
        return total_output_values
        




if __name__ == "__main__":
        p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

        if p.check(TESTS, solve):
                puzzle_input = p.load_puzzle()
                puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
                print("FINAL ANSWER: ", solve(puzzle_input))
