from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper
from math import inf, sqrt

PP_ARGS = False, False #rotate, cast int

DAY = 15
TEST_DELIM = "---"
FILE_DELIM = "\n"

TESTS = """
0551
1959
1159///17
---
041
326
731///9
---
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

DEBUG = False


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

    def __init__(self, val, key, average, w, h):
        self.key = key
        self.cost = int(val)
        self.neighbours = []
        self.h_cost = self.calculate_h_cost(key, average, w, h)


    def append(self, new):
        self.neighbours.append(new)

    def __repr__(self):
        
        #return str(node_names_test[self.key])
        return str(self.key)
        neighbours = ",".join(str(n.cost) for n in self.neighbours)
        return f"I'm at {self.key} ({self.cost}) and my neighbours are {neighbours}"

    def get_cost(self):
        return self.cost

    def calculate_h_cost(self, key, average, w, h):
        x_diff = abs(key[0] - (w-1))
        y_diff = abs(key[1] - (h-1))

        h_cost = sqrt(x_diff**2 + y_diff**2)
        p.bugprint(key, "h cost is", h_cost, "based on", w, h)
        return h_cost
        

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



        
def finalise_shortest_path(destination, path_data, origin):
    node = destination
    tot = 0
    p.bugprint("Find shortest path from", destination, "back to", origin)

    while node != origin:
        cost = node.cost
        
        tot += cost
        next_ = path_data[node][-1]

        p.bugprint(f"At {node}, shortest path is via {next_} cost {cost}")
        node = next_

    return tot

    


def use_a_star(origin, destination, graph):
    
    def calculate_costs(node, path_data):
        comp_node = path_data[node][3]
        
        g_cost = node.cost
        while comp_node is not None:
            g_cost += comp_node.cost
            comp_node = path_data[comp_node][3]        

        path_data[node][0] = g_cost

        # calculate f_cost
        p.bugprint("My g cost is", g_cost)
    
        path_data[node][2] = g_cost + node.h_cost



        return path_data


    ## each vertex stores:

    ## distance from A | h cost | f = g + h | prev vertex

    path_data = {n:[None, n.h_cost, None, None]  for n in graph.values()}

    

    
    closed_vertices = []


    current_node = None

    

    while destination not in closed_vertices:

        if not current_node:

            current_node = origin
            open_vertices = [current_node]

        else:

            ## select new current node
            lowest = inf
            select_node = None
            
            for n in open_vertices:
                data = path_data[n]
                if data[2] <= lowest:
                    lowest = data[2]
                    #p.bugprint("current lowest is", n)
                    select_node = n

            current_node = select_node
            for v, row in path_data.items():
                p.bugprint(v, row)




        


        path_data = calculate_costs(current_node, path_data)


        
        for n in current_node.neighbours:
            if n not in closed_vertices and n not in open_vertices:
                open_vertices.append(n)
                # set previous vertex
                path_data[n][3] = current_node
                path_data = calculate_costs(n, path_data)

        open_vertices.remove(current_node)
        closed_vertices.append(current_node)
                

                



    
    return finalise_shortest_path(destination, path_data, origin) 
    

    

def use_dijkstras(origin, destination, graph, unvisited):


    ## each vertex stores:

    ## distance from A |  prev vertex

    path_data = {n:[inf, None]  for n in unvisited}

    tot = 0

    
    p.bugprint("Starting dijkstras")
    
    visited = []



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
                

                
        current_node = smallest_known

        for neighbour in current_node.neighbours:
            if neighbour is not origin and neighbour not in visited:
                distance = neighbour.cost + current_node.cost
                if distance <= path_data[neighbour][0]:
                
                    path_data[neighbour] = [distance, current_node]


        unvisited.remove(current_node)
        visited.append(current_node)


    return finalise_shortest_path(destination, path_data, origin)
        


def solve(data):
    count = 0

    graph = {}

    w = len(data[0])
    h = len(data)

    

    unvisited = []
    visited = []

    all_data = []

    all_data = list(map(int, findall("\d", "".join(data))))

    average = sum(all_data) / len(all_data)

    p.bugprint("Average is", average)

    p.bugprint("Creating graph")
    
    for y,row in enumerate(data):
        for x,cell in enumerate(row):
            key = (x,y)
            this_node = graph.get(key)
            if not this_node:
                this_node = Node(cell, key, average, w, h)
                graph[key] = this_node

            for n in get_neighbours(data, x, y, w, h):
                n_key = (n[0], n[1])
                this_neigh = graph.get(n_key)    
                if not this_neigh:
                    this_neigh = Node(n[2], n_key, average, w, h)
                    graph[n_key] = this_neigh

                this_node.append(this_neigh)
                
            unvisited.append(this_node)
            
    origin = graph[(0,0)]

    destination = graph[(w-1, h-1)]


    #shortest_path_cost = use_dijkstras(origin, destination, graph, unvisited)

    shortest_path_cost = use_a_star(origin, destination, graph)
    
    return shortest_path_cost




if __name__ == "__main__":

    



    
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
