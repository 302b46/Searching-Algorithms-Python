from heapq import heappop, heappush
from math import inf

class Graph:
    def __init__(self, directed=True):
        self.edges = {}
        self.huristics = {}
        self.directed = directed

    def add_edge(self, node1, node2, cost = 1, __reversed=False):
        try: neighbors = self.edges[node1]
        except KeyError: neighbors = {}
        neighbors[node2] = cost
        self.edges[node1] = neighbors
        if not self.directed and not __reversed: self.add_edge(node2, node1, cost, True)

    def set_huristics(self, huristics={}):
        self.huristics = huristics

    def neighbors(self, node):
        try: return self.edges[node]
        except KeyError: return []

    def cost(self, node1, node2):
        try: return self.edges[node1][node2]
        except: return inf


    def best_first_search(self, start, goal):
        found, edge, visited, came_from, cost_so_far = False, [(self.huristics[start], start)], set([start]), {start: None}, {start: 0}
        print('{:15s} | {}'.format('Node', 'Edge'))
        print('---------------------------------------------')
        print('{:15s} | {}'.format('-', str(edge[0])))
        while not found and len(edge):
            _, current = heappop(edge)
            print('{:15s}'.format(current), end=' | ')
            if current == goal: found = True; break
            for node in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, node)
                if node not in visited or cost_so_far[node] > new_cost:
                    visited.add(node); came_from[node] = current; cost_so_far[node] = new_cost
                    heappush(edge, (new_cost + self.huristics[node], node))
            print(', '.join([str(n) for n in edge]))
        if found: print(); return came_from, cost_so_far[goal]
        else: print('No path from {} to {}'.format(start, goal)); return None, inf

    @staticmethod
    def print_path(came_from, goal):
        parent = came_from[goal]
        if parent:
            Graph.print_path(came_from, parent)
        else: print(goal, end='');return
        print(' ==>', goal, end='')


    def __str__(self):
        return str(self.edges)


graph = Graph(directed=True)
graph.add_edge('Arad', 'Zerind', 75)
graph.add_edge('Arad', 'Timisoara', 118)
graph.add_edge('Arad', 'Sibiu', 140)

graph.add_edge('Zerind', 'Arad', 75)
graph.add_edge('Zerind', 'Oradea', 71)

graph.add_edge('Timisoara', 'Arad', 118)
graph.add_edge('Timisoara', 'Lugoj', 111)

graph.add_edge('Sibiu', 'Oradea', 151)
graph.add_edge('Sibiu', 'Arad', 140)
graph.add_edge('Sibiu', 'Fagaras', 99)
graph.add_edge('Sibiu', 'Rimnicu Vilcea', 80)

graph.add_edge('Oradea', 'Zerind', 71)
graph.add_edge('Oradea', 'Sibiu', 151)

graph.add_edge('Lugoj', 'Timisoara', 111)
graph.add_edge('Lugoj', 'Mehadia', 70)

graph.add_edge('Rimnicu Vilcea', 'Sibiu', 80)
graph.add_edge('Rimnicu Vilcea', 'Pitesti', 97)
graph.add_edge('Rimnicu Vilcea', 'Craiova', 146)

graph.add_edge('Mehadia', 'Lugoj', 70)
graph.add_edge('Mehadia', 'Dobreta', 75)

graph.add_edge('Craiova', 'Dobreta', 120)
graph.add_edge('Craiova', 'Rimnicu Vilcea', 146)
graph.add_edge('Craiova', 'Pitesti', 138)
graph.add_edge('Craiova', 'Pitesti', 138)

graph.add_edge('Pitesti', 'Craiova', 138)
graph.add_edge('Pitesti', 'Rimnicu Vilcea', 97)
graph.add_edge('Pitesti', 'Bucharest', 101)

graph.add_edge('Fagaras', 'Bucharest', 211)
graph.add_edge('Fagaras', 'Sibiu', 99)

graph.add_edge('Dobreta', 'Mehadia', 75)
graph.add_edge('Dobreta', 'Craiova', 120)

graph.add_edge('Bucharest', 'Pitesti', 101)
graph.add_edge('Bucharest', 'Fagaras', 211)
graph.add_edge('Bucharest', 'Giurgiu', 90)

graph.add_edge('Giurgiu', 'Bucharest', 90)

graph.set_huristics({'Arad': 366, 'Zerind': 374, 'Timisoara': 329, 'Sibiu': 253,'Oradea': 300,'Lugoj': 244,
                     'Fagaras': 178,'Rimnicu Vilcea': 193,'Mehadia': 241,'Pitesti': 98,'Craiova': 160,'Dobreta': 242,
                     'Bucharest': 0,'Fagaras': 178,'Giurgiu': 77})

def result(start, goal):
    traced_path, cost = graph.best_first_search(start, goal)
    if (traced_path): print('The Path:', end=' '); Graph.print_path(traced_path, goal); print('\nTotal Cost:', cost)
