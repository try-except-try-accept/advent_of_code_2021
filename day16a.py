from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int

DAY = 16
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """D2FE28///6
---
38006F45291200///8
---
EE00D40C823060///7
---
8A004A801A8002F478///16
---
620080001611562C8802118E34///12
---
C0015000016115A2E0802F182340///23
---
A0016C880162017C3686B18A3D4780///31

---"""

DEBUG = True

#0123456789012345678901234567890123456789
#00111000000000000110111101000101001010010001001000000000
#VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB



def process_literal(bits, version, tot):
    print("LITERAL")

    index = 0
    first_bit = bits[index]

    number = ""
    while True:
        chunk = bits[index:index+5]
        number += chunk[1:]
        if chunk[0] == "0":
            break

        index += 5

    tot += int(number, 2)

    return version

def process_operator(bits, version, tot):

    print("Bits is", bits)

    
    length_type_id = int(bits[0], 2)
    print(f"length_type_id is {length_type_id}")

    if length_type_id == 0:
        length = int(bits[1:16], 2)
        print("length is", length)
        index = 16
        sub_packet = bits[index:index+11]
        tot += process_bits(sub_packet)
        sub_packet = bits[index+11:]
        tot += process_bits(sub_packet)
        
        

    else:
        number_of_sub_packets = int(bits[1:12], 2)
        print(f"Number of sub packets is {number_of_sub_packets}", bits[1:12])

        index = 12
        for j in range(number_of_sub_packets):
            sub_packet = bits[index:index+11]
            print("Found a sub packet", sub_packet)
            tot += process_bits(sub_packet)
            index += 11
        
    return tot

    




def process_bits(bits, tot=0):
    tot = 0
    version = int(bits[:3], 2)
    type_ = int(bits[3:6], 2)

    print(f"Version is {version} type is {type_}")

    payload = bits[6:]

    if type_ == 4:
        tot += process_literal(payload, version, tot)

    else:
        tot += process_operator(payload, version, tot)

    return tot                      

    
        

    
    

def solve(data):
    count = 0
    tot = 0

    bits = "".join([bin(int(digit, 16))[2:].zfill(4) for digit in data[0]])
    print(bits)

    return process_bits(bits)





if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
