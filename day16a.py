from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int

DAY = 16
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """EE00D40C823060///14
---
620080001611562C8802118E34///12
---
8A004A801A8002F478///16
---
C0015000016115A2E0802F182340///23
---
A0016C880162017C3686B18A3D4780///31
"""

DEBUG = False

def pop_bits(bits, amt):
    return [bits.pop(0) for i in range(amt)]

def get_bits(hexa):
    return list("".join(bin(int(d, 16))[2:].zfill(4) for d in hexa))

def get_version(bits):
    version = pop_bits(bits, 3)
    version_num = int("".join(version), 2)
    p.bugprint(f"The three bits labeled V ({version}) are the packet version, {version_num}.")
    return version_num, bits

def get_type_id(bits):
    type_ = pop_bits(bits, 3)
    type_id = int("".join(type_), 2)
    p.bugprint(f"The three bits labeled V ({type_}) are the packet type_id, {type_id}.")
    return type_id, bits

def get_length(bits):
    length_type = pop_bits(bits, 1)[0]
    exp_bits = {'0':15, '1':11}[length_type]
    length = int("".join(pop_bits(bits, exp_bits)), 2)
    p.bugprint(f"The length type ID is {length_type}")
    if length_type == '0':
        p.bugprint(f"the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.")
    else:
        p.bugprint(f"the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.")
    return length, length_type, bits

def get_literal(bits):
    literal = []
    end_literal = False
    while not end_literal:
        chunk = pop_bits(bits, 5)
        literal += chunk[1:]
        end_literal = chunk[0] == "0"
        p.bugprint(f"The five bits ({chunk}) start with a {chunk[0]} contain four bits of the number, {chunk[1:]}.")

    literal_value = int("".join(literal), 2)
    p.bugprint(f"So, this packet represents a literal value with binary representation {literal}, which is {literal_value} in decimal.")
    return literal_value, bits

def solve(data):
    count = 0

    bits = get_bits(data[0])
    version_sum = 0
    
    while len(bits):
        p.bugprint("Bits left...", "".join(bits))

        version, bits = get_version(bits)
        version_sum += version
        type_id, bits = get_type_id(bits)
        
        if type_id == 4:
            literal, bits = get_literal(bits)
        else:
            length, length_type, bits = get_length(bits)



        if set(bits) == {'0'}:
            break

    return version_sum




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
