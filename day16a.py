from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int

DAY = 16
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """D2FE28///6
---
38006F45291200///9
---
EE00D40C823060///14
---
8A004A801A8002F478///16
---
C0015000016115A2E0802F182340///23
---
620080001611562C8802118E34///12
---
A0016C880162017C3686B18A3D4780///31

---"""

DEBUG = True

#0123456789012345678901234567890123456789
#00111000000000000110111101000101001010010001001000000000
#VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB



def process_literal(bits, version, tot):
    print("LITERAL", bits)

    
    
    try:
        number = ""
        chunk_num = 0
        while True:
            print("chunking", bits)
            chunk = "".join(bits.pop(0) for i in range(5))
            number += chunk[1:]
            if chunk[0] == "0":
                break
            chunk_num += 1
        print(f"{number} literal was {int(number, 2)}")

    except:
        pass

    
    return tot, bits



def process_operator(bits, version, tot):

    print(bits)
    final_bits = None
    length_type_id = int(bits.pop(0), 2)
    print(f"{length_type_id} length_type_id is {length_type_id}")


    if length_type_id == 0:
        length = int("".join(bits.pop(0) for i in range(15)), 2)
        print("length is", length)
        bits = bits[:length]
        
        print(f"sub_packet is now {''.join(bits)}")
        tot, bits = process_bits(bits, tot)
        
    else:
        number_of_sub_packets = "".join(bits.pop(0) for i in range(11))
        
        print(f"{number_of_sub_packets} num of sub packets is {int(number_of_sub_packets, 2)}", )
        number_of_sub_packets = int(number_of_sub_packets, 2)

        bits_left = len("".join(bits).rstrip("0"))

        bits_left = len(bits)
        
        packet_length = bits_left//number_of_sub_packets
        
        print(f"Packet length is {packet_length}")
        for j in range(number_of_sub_packets):
            
            sub_packet = [bits.pop(0) for i in range(packet_length)]
            print(f"sub_packet is now {(sub_packet)}")
            
            if not sub_packet:
                break
            tot, final_bits = process_bits(sub_packet, tot)

        if final_bits:
            bits = final_bits

    print("Exit")
        
    return tot, bits

    




def process_bits(bits, tot=0):
    print("".join(bits))

    print(len(bits))
    

    while bits:
        print(f"bits left {bits} {len(bits)} tot is {tot}")
        version = "".join(bits.pop(0) for i in range(3))
        
        type_ = "".join(bits.pop(0) for i in range(3))

        print(f"{version} version is {int(version, 2)}")
        print(f"{type_} type is {int(type_, 2)}")

        version, type_ = int(version, 2), int(type_, 2)

        tot += version
        
        payload = bits

        if type_ == 4:
            tot, bits = process_literal(payload, version, tot)

        else:
            tot, bits = process_operator(payload, version, tot)

    return tot, bits                  

    
        

    
    

def solve(data):
    count = 0
    tot = 0

    bits = list("".join([bin(int(digit, 16))[2:].zfill(4) for digit in data[0]]).rstrip("0"))

    result = process_bits(bits)[0]

    print(f"result is {result}")

    return result





if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
