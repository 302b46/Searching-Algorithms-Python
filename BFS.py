
from collections import deque

class Graph:
    def __init__(self, directed=True):
        self.edges = {}
        self.directed = directed

    def add_edge(self, node1, node2, __reversed=False):
        try: neighbors = self.edges[node1]
        except KeyError: neighbors = set()
        neighbors.add(node2)
        self.edges[node1] = neighbors
        if not self.directed and not __reversed: self.add_edge(node2, node1, True)

    def neighbors(self, node):
        try: return self.edges[node]
        except KeyError: return []

    def breadth_first_search(self, start, goal):
        found, edge, visited, came_from = False, deque([start]), {start}, {start: None}
        print('{:15s} | {}'.format('Node', 'Edge'))
        print('--------------------------------------------')
        print('{:15s} | {}'.format('-', start))
        while not found and len(edge):
            current = edge.pop()
            print('{:15s}'.format(current), end=' | ')
            if current == goal: found = True; break
            for node in self.neighbors(current):
                if node not in visited: visited.add(node); edge.appendleft(node); came_from[node] = current
            print(', '.join(edge))
        if found: print(); return came_from
        else: print('No path from {} to {}'.format(start, goal))

    @staticmethod
    def print_path(came_from, goal):
        parent = came_from[goal]
        if parent:
            Graph.print_path(came_from, parent)
        else: print(goal, end='');return
        print(' ==>', goal, end='')


    def __str__(self):
        return str(self.edges)


graph = Graph(directed=False)
graph.add_edge('Arad', 'Zerind')
graph.add_edge('Arad', 'Timisoara')
graph.add_edge('Arad', 'Sibiu')

graph.add_edge('Zerind', 'Arad')
graph.add_edge('Zerind', 'Oradea')

graph.add_edge('Timisoara', 'Arad')
graph.add_edge('Timisoara', 'Lugoj')

graph.add_edge('Sibiu', 'Oradea')
graph.add_edge('Sibiu', 'Arad')
graph.add_edge('Sibiu', 'Fagaras')
graph.add_edge('Sibiu', 'Rimnicu Vilcea')

graph.add_edge('Oradea', 'Zerind')
graph.add_edge('Oradea', 'Sibiu')

graph.add_edge('Lugoj', 'Timisoara')
graph.add_edge('Lugoj', 'Mehadia')

graph.add_edge('Rimnicu Vilcea', 'Sibiu')
graph.add_edge('Rimnicu Vilcea', 'Pitesti')
graph.add_edge('Rimnicu Vilcea', 'Craiova')

graph.add_edge('Mehadia', 'Lugoj')
graph.add_edge('Mehadia', 'Dobreta')

graph.add_edge('Craiova', 'Dobreta')
graph.add_edge('Craiova', 'Rimnicu Vilcea')
graph.add_edge('Craiova', 'Pitesti')
graph.add_edge('Craiova', 'Pitesti')

graph.add_edge('Pitesti', 'Craiova')
graph.add_edge('Pitesti', 'Rimnicu Vilcea')
graph.add_edge('Pitesti', 'Bucharest')

graph.add_edge('Fagaras', 'Bucharest')
graph.add_edge('Fagaras', 'Sibiu')

graph.add_edge('Dobreta', 'Mehadia')
graph.add_edge('Dobreta', 'Craiova')

graph.add_edge('Bucharest', 'Pitesti')
graph.add_edge('Bucharest', 'Fagaras')
graph.add_edge('Bucharest', 'Giurgiu')

graph.add_edge('Giurgiu', 'Bucharest')


def result(start,goal):
    traced_path = graph.breadth_first_search(start, goal)
    if (traced_path): print('The Path:', end=' '); Graph.print_path(traced_path, goal);print()
