from re import search, match, findall
from collections import Counter


GREEDY = "\[.+\]" # greedily match anything between [ and ]
LAZY = "\[.+?\]"  # lazily match anything between [ and ]

DAY = 3
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010///230"""

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
        data = f.read().strip()

    return data

def pre_process(data, rotate=False, cast_int=True):

    data = data.split(FILE_DELIM)
    
    if rotate:
        cols = len(data[0])
        
        new = [""] * cols
        
        for row in data:
            for i in range(cols):
                new[i] += row[i]

        data = new

    if not cast_int:
        return data
        
    
    numeric = all(d.isdigit() for d in data)
    
    if numeric:
        data = map(int, data)
    return data

def filter_bits(data, mode, i=0):
    
    comp_bit = get_comp_bit("".join(bina[i] for bina in data), mode)
    print("Remove any not", comp_bit, "at index", i)
    x = 0

    data = [d for d in data if d[i] == comp_bit]

    if len(data) == 1:
        return data[0]
    else:
        return filter_bits(data, mode, i+1)
        

    
def get_comp_bit(data, mode=1):
    
    ones = data.count("1")
    zeroes = data.count("0")
    
    if ones < zeroes:
        return str(int(not mode))
    return str(mode)

    

def solve(data):

    oxy = list(data)
    co2 = list(data)

    oxy = filter_bits(oxy, 1)
    co2 = filter_bits(co2, 0)

    return int(oxy, 2) * int(co2, 2)
            

def check():

    success = True

    for row in TESTS.split(TEST_DELIM):
        if not len(row):    continue

        data, expected = row.split("///")
        data = pre_process(data, *ppargs)
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
    ppargs = False, False #rotate, cast int

    if check():
        puzzle = pre_process(load_puzzle(), *ppargs)
        print("FINAL ANSWER: ", solve(puzzle))
