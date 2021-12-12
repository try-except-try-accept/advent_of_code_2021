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
b-end///36
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
kj-dc///103
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
start-RW///3509
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
    
def traverse(cave, d=-1, route="", complete_routes=0, allow_twice=""):
    d += 1

    #print(cave.name, end=",")
    
    ## check if end of route
    if cave.name == "end":
        route += "," + cave.name
        if route in unique_routes:
            count = 0
        else:
            count = 1
            unique_routes.add(route)
        
        return route, complete_routes+count, allow_twice

    ## check if start of route
    

    if d == 0:
        ## this is actually the start
        route = "start"

    elif cave.name == "start": # we've gone back to the start
        return route, complete_routes, allow_twice

    else:

        if cave.name.islower():           

            if cave.name == allow_twice:
                allow = 2
            else:
                allow = 1
        
            if route.count(cave.name) == allow:
                ## already visited so no more allowed
                return route, complete_routes, allow_twice

        ## allowed.. continuation of route
        route += "," + cave.name

    
    ## now visit every cave linked from this cave

    route_copy = route

    for path in cave.paths:
        route, complete_routes, allow_twice = traverse(path, d, route_copy,
                                                            complete_routes, allow_twice)

            
    return route, complete_routes, allow_twice

    



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
        if end != "end" and start != "start":
            end_cave.append(start_cave)

            
    small_caves = []
        
    for n, c in caves.items():
        print("This cave is", n)
        if n.islower():
            small_caves.append(n)

    print("Traversing")


    total = 0

    for s in small_caves:
        
        _, complete_routes, _ = traverse(caves["start"], allow_twice=s)
        total += complete_routes

    return total

    
        
    

    

unique_routes = set()


if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
