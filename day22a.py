from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper
from math import inf

PP_ARGS = False, False #rotate, cast int

DAY = 22
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10///39
---
on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682///590784
"""

DEBUG = True


def solve(data):
    all_data = "".join(data)
    
    
    

    instructions = []

    min_x, max_x, min_y, max_y, min_z, max_z = -50, 50, -50, 50, -50, 50

    for row in data:

        mode, ins = row.split(" ")
        mode = bool(mode.replace("off", ""))

        x, y, z = ins.split(",")

        x_from, x_to = list(map(int, x.replace("x=", "").split("..")))
        y_from, y_to = list(map(int, y.replace("y=", "").split("..")))
        z_from, z_to = list(map(int, z.replace("z=", "").split("..")))
            
        instructions.append((mode, x_from, x_to, y_from, y_to, z_from, z_to))


    cubes = [[[False for z in range(min_z, max_z+1)] for y in range(min_y, max_y+1)] for x in range(min_x, max_x+1)]

    print("prepped cubes")
    
    for mode, x_from, x_to, y_from, y_to, z_from, z_to in instructions:
        if x_from < min_x:
            x_from = min_x
        if x_to > max_x:
            x_to = max_x
        if y_from < min_y:
            y_from = min_y
        if y_to > max_y:
            y_to = max_y
        if z_from < min_z:
            z_from = min_z
        if z_to > max_z:
            z_to = max_z
        
        for x in range(x_from, x_to+1):
            x -= min_x
            for y in range(y_from, y_to+1):
                y -= min_y
                for z in range(z_from, z_to+1):
                    z -= min_z
                    try:
                        cubes[z][y][x] = mode
                    except:
                        pass

    return sum([sum([face.count(True) for face in cube]) for cube in cubes])

if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
