"""
file: escape.py
language: python3
author: pvc8661@rit.edu by  Pallavi Chandanshive
author: pan7447@rit.edu by  Parvathi Nair
description: Implementation of graph to find an escape point from the pond
Based off of searchalgs.py created and distributed by CSCI-603 faculty.
"""

from graph import Graph

def findShortestPath(start, end):
    """
    Find the shortest path, if one exists, between a start and end vertex
    :param start (Vertex): the start vertex
    :param end (Vertex): the destination vertex
    :return: A list of Vertex objects from start to end, if a path exists,
        otherwise None
    """
    # Using a queue as the dispenser type will result in a breadth first
    # search
    queue = []
    queue.append(start)         # prime the queue with the start vertex

    # The predecessor dictionary maps the current Vertex object to its
    # immediate predecessor.  This collection serves as both a visited
    # construct, as well as a way to find the path
    predecessors = {}
    predecessors[start] = None  # add the start vertex with no predecessor

    # Loop until either the queue is empty, or the end vertex is encountered
    while len(queue) > 0:
        current = queue.pop(0)
        if current == end:
            break
        for neighbor in current.getConnections():
            if neighbor not in predecessors:        # if neighbor unvisited
                predecessors[neighbor] = current    # map neighbor to current
                queue.append(neighbor)              # enqueue the neighbor

    # If the end vertex is in predecessors a path was found
    if end in predecessors:
        path = []
        current = end
        while current != start:              # loop backwards from end to start
            path.insert(0, current)          # prepend current to the path list
            current = predecessors[current]  # move to the predecessor
        path.insert(0, start)
        return path
    else:
        return None



def buildTestGraph():
    g = Graph()
    g.addEdge("A", "B")
    g.addEdge("B", "A")
    g.addEdge("B", "C")
    g.addEdge("C", "D")
    g.addEdge("A", "C")

    for source, dest in [("A", "D"), ("B", "D")]:
        
        sv = g.getVertex(source)
        dv = g.getVertex(dest)
        #print("DFS (" + source + "->" + dest + "): " + str([x.id for x in pathFinder(sv, dv, stack.Stack())]))
        #print("BFS (" + source + "->" + dest + "): " + str([x.id for x in pathFinder(sv, dv, queue.Queue())]))
        #print("DJI (" + source + "->" + dest + "): " + str([x.id for x in findDJI(sv, dv)]))
        print("FSP (" + source + "->" + dest + "): " + str([x.id for x in findShortestPath(sv, dv)]))
    return g

def buildG1():
    # Builds the following graph:
    #
    #       A - B - C     J-K
    #      / \      |
    #     D   E     F
    #      \ /      |
    #       G - H - I
    # 
    # Note that the graph class is directed,
    # so we add bidirectional edges with uniform
    # positive cost.

    g = Graph()

    for source, dest in [("A", "B"), ("B", "C"), ("A", "D"), ("A", "E"), ("D", "G"), ("E", "G"), ("G", "H"), ("H", "I"), ("C", "F"), ("I", "F"), ("J", "K")]:
        g.addEdge(source, dest, 1)
        g.addEdge(dest, source, 1)
    return g

if __name__ == '__main__':
    buildTestGraph()


