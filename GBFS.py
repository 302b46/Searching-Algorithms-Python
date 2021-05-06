from heapq import heappop, heappush
from math import inf

class Graph:
    def __init__(self, directed=True):
        self.edges = {}
        self.heuristics = {}
        self.directed = directed

    def add_edge(self, node1, node2, cost = 1, __reversed=False):
        try: neighbors = self.edges[node1]
        except KeyError: neighbors = {}
        neighbors[node2] = cost
        self.edges[node1] = neighbors
        if not self.directed and not __reversed: self.add_edge(node2, node1, cost, True)

    def set_heuristics(self, heuristics=None):
        if heuristics is None:
            heuristics = {}
        self.heuristics = heuristics

    def neighbors(self, node):
        try: return self.edges[node]
        except KeyError: return []

    def cost(self, node1, node2):
        try: return self.edges[node1][node2]
        except: return inf


    def best_first_search(self, start, goal):
        found, fringe, visited, came_from, cost_so_far = False, [(self.heuristics[start], start)], {start}, {start: None}, {start: 0}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', str(fringe[0])))
        while not found and len(fringe):
            _, current = heappop(fringe)
            print('{:11s}'.format(current), end=' | ')
            if current == goal: found = True; break
            for node in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, node)
                if node not in visited or cost_so_far[node] > new_cost:
                    visited.add(node); came_from[node] = current; cost_so_far[node] = new_cost
                    heappush(fringe, (new_cost + self.heuristics[node], node))
            print(', '.join([str(n) for n in fringe]))
        if found: print(); return came_from, cost_so_far[goal]
        else: print('No path from {} to {}'.format(start, goal)); return None, inf

    @staticmethod
    def print_path(came_from, goal):
        parent = came_from[goal]
        if parent:
            Graph.print_path(came_from, parent)
        else: print(goal, end='');return
        print(' =>', goal, end='')


    def __str__(self):
        return str(self.edges)


graph = Graph(directed=True)
graph.add_edge('Arad', 'Sibiu', 140)
graph.add_edge('Arad', 'Timisoara', 118)


graph.add_edge('Bucharest', 'Fagaras', 211)
graph.add_edge('Bucharest', 'Giurgiu', 90)
graph.add_edge('Bucharest', 'Pitesti', 101)
graph.add_edge('Bucharest', 'Urziceni', 85)

graph.add_edge('Craiova', 'Dobreta', 120)
graph.add_edge('Craiova', 'Pitesti', 138)
graph.add_edge('Craiova', 'Rimnicu Vilcea', 146)

graph.add_edge('Dobreta', 'Mehadia', 75)

graph.add_edge('Eforie', 'Hirsova', 98)

graph.add_edge('Fagaras', 'Sibiu', 99)

graph.add_edge('Hirsova', 'Urzinceni', 98)

graph.add_edge('Iasi', 'Neamt', 87)
graph.add_edge('Iasi', 'Vaslui', 92)

graph.add_edge('Lugoj', 'Mehadia', 70)
graph.add_edge('Lugoj', 'Timisoara', 111)

graph.add_edge('Oradea', 'Sibiu', 151)

graph.add_edge('Pitesti', 'Rimnicu Vilcea', 97)

graph.add_edge('Rimnicu Vilcea', 'Sibiu', 80)

graph.add_edge('Urzinceni', 'Vaslui', 142)





graph.set_heuristics({'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242,
                      'Eforie': 161, 'Fagaras': 178, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226,
                       'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234, 'Oradea': 300, 'Pitesti': 98,
                      'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80,
                      'Vaslui': 199, 'Zarind': 374})

def result(start, goal):
    traced_path, cost = graph.best_first_search(start, goal)
    if (traced_path): print('Path:', end=' '); Graph.print_path(traced_path, goal); print('\nCost:', cost)