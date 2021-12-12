from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int

DAY = 12
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """start-A
start-b
A-c
A-b
b-d
A-end
b-end///10
---
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc///19
---
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW///226
"""

DEBUG = True


class Cave:

    def __init__(self, name, path=""):
        self.name = name
        self.paths = []
        if path:
            self.paths.append(path)

    def append(self, new):
        self.paths.append(new)

    def __repr__(self):
        return "And it is linked to: " + ", ".join(c.name for c in self.paths)
    
def traverse(cave, d=-1, route="", complete_routes=0):
    d += 1
    
    ## check if end of route
    if cave.name == "end":
        route += "," + cave.name        
        return route, complete_routes+1

    ## check if start of route

    if d == 0:
        route = "start"   
    else:
        
        ## not allowed to revisit lower
        if d > 0 and cave.name.islower() and cave.name in route:
            return route, complete_routes

        ## allowed.. continuation of route
        route += "," + cave.name

    route_copy = route
    ## now visit every cave linked from this cave

    if cave.name != "end":
        for path in cave.paths:
            # didn't actually need the backtracking for some reason
            
            #if route:
            #    rep_check = (route[-1] + "," + path.name) * 2

            #rep_check = "234234234"
            if not route or rep_check not in route:    
                route, complete_routes = traverse(path, d, route_copy, complete_routes)


    return route, complete_routes

    
    


def solve(data):
    count = 0


    caves = {}

    

    for path in data:
        start, end = path.split("-")
        
        if start in caves:
            start_cave = caves[start]
        else:
            start_cave = Cave(start)
            caves[start] = start_cave

        if end in caves:
            end_cave = caves[end]
        else:
            end_cave = Cave(end)
            caves[end] = end_cave

        start_cave.append(end_cave)
        if end != "end":
            end_cave.append(start_cave)

        
    for n, c in caves.items():
        print("This cave is", n)
        print(c)
        
    print("Traversing")
        
    _, complete_routes = traverse(caves["start"])

    return complete_routes


if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
