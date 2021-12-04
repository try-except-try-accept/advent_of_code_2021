from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper
from copy import deepcopy


PP_ARGS = False, False #rotate, cast int
DAY = 3
TEST_DELIM = "---"
FILE_DELIM = "\n"
DAY = 4
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
x
22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19
x
 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6
x
14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7///1924"""

DEBUG = True


def solve(data):
    count = ""

    processed = []

    numbers = list(map(int, data[0].split(",")))

    boards = [[]]
    for row in data[2:]:       

        if row.strip() == "x":
            boards.append([])
            continue

        row = row.strip().replace(" ", ",").replace(",,", ",")
        boards[-1].append(list(map(int, row.split(","))))


    winner = -1
    count = 5
    completed_boards = []    
    stop = False
    
    while not stop:
        print("Completed so far")
        print(completed_boards)
        winner = False
        draw = [numbers.pop(0) for i in range(count)]
    
        
        for this_num in draw:

            print("Drew", this_num)

            for  i, board in enumerate(boards):
                if i in completed_boards:
                    continue
                
                for j, row in enumerate(board):
                    for x, cell in enumerate(row):
                        
                    
                    
                        if cell == this_num:
                            boards[i][j][x] = None

            for board_num, board in enumerate(boards):
                if board_num in completed_boards:                    
                    continue
                
                if any(row.count(None) == 5 for row in board):
                    print("board", board_num, "wins")
                    winner = board_num
                    if board_num not in completed_boards:
                        completed_boards.append(board_num)
      
                for i in range(5):
                    col = [row[i] for row in board]
                    if col.count(None) == 5:
                        winner = board_num
                        print("board", board_num, "wins")
                        if board_num not in completed_boards:
                            completed_boards.append(board_num)
                        
                

                    

            if len(completed_boards) == len(boards):
                print("Everyone won!")
                stop = True

            if stop:
                break           

        count += 1
        
    winner = completed_boards[-1]
    print("board", winner, "wins")
    print("Winning number", this_num)

    final = 0

    
    for row in boards[winner]:
        
        for num in row:
            if num is not None:
                final += num
            


    return final * this_num




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
