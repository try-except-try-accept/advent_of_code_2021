from re import search, match, findall
from collections import Counter


GREEDY = "\[.+\]" # greedily match anything between [ and ]
LAZY = "\[.+?\]"  # lazily match anything between [ and ]

DAY = 1
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """a,a///aa
"""

DEBUG = True

def bugprint(*s, end="\n"):
    if DEBUG:
        for item in s:
            print(str(item), end=" ")
        print(end)


def buginput(s=""):
    if DEBUG:
        print(s)
        input()


def load_puzzle():
    with open(f"day{DAY}.txt") as f:
        data = f.read().strip().split(FILE_DELIM)

    return data

def pre_process(data):
    numeric = all(d.isdigit() for d in data)
    if numeric:
        data = map(int, data)
    return data

def solve(data):

    for row in data.split("\n"):
        pass
        

        
    

    return count


def check():

    success = True

    for row in TESTS.split(TEST_DELIM):
        if not len(row):    continue

        data, expected = row.split("///")
        data = pre_process(data)
        print(data, "should get", expected)
        
        outcome = solve(data)
        if str(outcome).strip() == expected.strip():
            print("Test passed")
        else:
            print("Test failed")
            success = False
            print(outcome)

    return success


if __name__ == "__main__":

    if check():
        puzzle = pre_process(load_puzzle())
        print("FINAL ANSWER: ", solve(puzzle))
