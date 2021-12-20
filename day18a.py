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



def explode(pair, d=0, left=None, right=None, explode_pair=None):

     print("parsing", pair)

     if d==4:
          print("EXPLODE", pair)
          return left, right, pair

     for i, thing in enumerate(pair):
          if type(thing) == list:
               if not explode_pair:
                    left, right, explode_pair = explode(thing, d+1, left, right)               
          else:
               
               if i == 0:
                    print("left is", pair)
                    left = pair
               elif not right or not explode_pair:
                    print("Right is", pair)
                    right = pair
                    

     return left, right, explode_pair


def process_explode(sequence):



     left_int, right_int, explode_pair = explode(sequence)
     print("Explode was", explode_pair)
     print("left was", left_int)
     print("Right was", right_int)

     if explode_pair:
          if left_int:
               left_int[0] += explode_pair[0]

          ## hacky fix to deal with wrong right int
          
##          if len(findall("\d{1,2}", left_int) > 3:
##               #left was [7, [[8, 4], 9]  ... the 9 is the right int
          if right_int:
               right_int[1] += explode_pair[1]

          sequence = dumps(sequence)
          sequence = sequence.replace(dumps(explode_pair), "0", 1)

     

          return loads(sequence)

     return sequence
     

def split(sequence):

     sequence = dumps(sequence)
     try:
          big_num = search("\d\d", sequence).group()
          print("Big num", big_num)
          i = int(big_num)
          replace_pair = f"[{i//2}, {ceil(i/2)}]"
          sequence = sub(big_num, replace_pair, sequence, count=1)
          return loads(sequence)
     except Exception as e:
          print(e)
          return loads(sequence)

     

     
     
     

DEBUG = True


def add(lines):

    left, right = lines
    
    final = left[:-1] + "," + right + "]"

    print("added.", final)
    
    return final


def solve(data):

    for row in data:

        row = loads(row)

        action = True

        while action:
            print(row)
            input()

            exploded_row = process_explode(row)
            if exploded_row != row:
                 row = exploded_row
                 print("After explode")
                 continue
            
            split_row = split(row)
            if split_row != row:
                 print("After split")
                 row = split_row
                 continue
            
            action = False

        print("Finalised row:", row)
        input()


if __name__ == "__main__":
    data = """[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]""".split("\n")
    
    
    solve(data)
    
    
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))

