from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper
from math import inf

PP_ARGS = False, False #rotate, cast int

DAY = 15
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581///40"""

DEBUG = True


node_names_test = {(0, 0): 'A',
(1, 0): 'B',
(2, 0): 'C',
(0, 1): 'D',
(1, 1): 'E',
(2, 1): 'F',
(0, 2): 'G',
(1, 2): 'H',
(2, 2): 'I'}

class Node:

    def __init__(self, val, key):
        self.key = key
        self.cost = int(val)

        self.neighbours = []


    def append(self, new):
        self.neighbours.append(new)

    def __repr__(self):
        
        #return str(node_names_test[self.key])
        return str(self.key)
        neighbours = ",".join(str(n.cost) for n in self.neighbours)
        return f"I'm at {self.key} ({self.cost}) and my neighbours are {neighbours}"

    def get_cost(self):
        return self.cost

def get_neighbours(data, x, y, w, h):
    '''Return neighbouring points, respect boundaries'''

    left, right, top, bottom = None, None, None, None

    if x > 0:
        left = x-1, y, data[y][x-1]
    
    if x < w - 1:
        right = x+1, y, data[y][x+1]

    if y > 0:
        top = x, y-1, data[y-1][x]

    if y < h - 1:
        bottom = x, y+1, data[y+1][x]

    return [n for n in (left, right, top, bottom) if n is not None]


def solve(data):
    count = 0

    graph = {}

    w = len(data[0])
    h = len(data)

    

    unvisited = []
    visited = []
    
    for y,row in enumerate(data):
        for x,cell in enumerate(row):
            key = (x,y)
            this_node = graph.get(key)
            if not this_node:
                this_node = Node(cell, key)
                graph[key] = this_node

            for n in get_neighbours(data, x, y, w, h):
                n_key = (n[0], n[1])
                this_neigh = graph.get(n_key)    
                if not this_neigh:
                    this_neigh = Node(n[2], n_key)
                    graph[n_key] = this_neigh

                this_node.append(this_neigh)
                
            unvisited.append(this_node)
            
    origin = graph[(0,0)]

    destination = graph[(w-1, h-1)]
    
    path_data = {n:[inf, None]  for n in unvisited}

    
    
    
    visited = []

##    print(graph)

    while len(unvisited):

        if not visited:
            smallest_known = origin
        else:
            smallest = inf
            smallest_known = None
            for node, data in path_data.items():
                
                if data[0] < smallest:
                    if node in unvisited:
                        smallest = data[0]
                        smallest_known = node
                

                
        
        ## find node with shortest distance from A
        #print("Smallest known is", smallest_known)
                
        ## current vertex. examine unvisited neighbours
        current_node = smallest_known

        for neighbour in current_node.neighbours:
            if neighbour is not origin and neighbour not in visited:
                distance = neighbour.cost + current_node.cost
                if distance <= path_data[neighbour][0]:
                
                    path_data[neighbour] = [distance, current_node]

        #print(unvisited)


        unvisited.remove(current_node)
        visited.append(current_node)
        
##        for p in path_data.items():
##            print(p)
##
##        input()

    node = destination
    tot = 0
    print("Find shortest path from", destination, "back to", origin)

    while node != origin:
        cost = node.cost
        
        tot += cost
        next_ = path_data[node][1]

        print(f"At {node}, shortest path is via {next_} cost {cost}")
        node = next_

        


    ## off by 1 error don't include home node
    return tot-1




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
