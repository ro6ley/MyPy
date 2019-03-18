"""
BFS Steps:
- Check the starting node and add its neighbors to the queue
- Mark starting node as explored
- Get the first node from the queue/dequeue it
- Check if node has already been visited
- If not, go through the neighbors of the node and enqueue them
- Mark node as explored
- Repeat until queue is empty

BFS uses a FIFO queue.

I'll use a FIFO Queue Python Object since it is faster than using an array for
    queue operations. EG. queue.popleft() has a time complexity of O(1) while 
    array.pop() has a time complexity of O(n).
"""
from collections import deque

# sample graph implemented as a dictionary
graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}


def bfs_traverse_graph(graph, start):
    """
    Visit all nodes in graph using BFS Algorithm from a particular
    starting point.
    """
    # keep track of all visited nodes
    visited = []

    # keep track of the nodes to be explored, starting with the starting node
    # provided
    queue = deque([start])

    # keep looping while queue still has nodes to be checked
    while queue:
        # get the first node
        node = queue.popleft()

        if node not in visited:
            # add node to list of checked nodes
            visited.append(node)
            # find the neighbors of the current node
            neighbors = graph[node]

            # add neighbors to queue
            for neighbor in neighbors:
                queue.append(neighbor)

    # return the order in which the graph was explored using BFS
    return visited


def bfs_shortest_path(graph, start, goal):
    """
    Find the shortest path from a node to another using BFS
    """
    # keep track of all visited nodes
    visited = []

    # keep track of the nodes to be explored, starting with the starting node
    # provided
    # queue = [[start]]
    queue = deque([[start]])

    if start == goal:
        return "The start element is the goal element"

    while queue:
        # get the first element of the current path
        path = queue.popleft()

        # get the last node from the path
        node = path[-1]

        if node not in visited:
            neighbors = graph[node]

            # create a new path for all the neighbors and push it into the queue
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                # return path to goal if neighbor is goal
                if neighbor == goal:
                    return new_path

            visited.append(node)
    
    return "There is no path between {} and {}".format(start, goal)


print(bfs_traverse_graph(graph, 'A'))   # ['A', 'B', 'C', 'E', 'D', 'F', 'G']

print(bfs_shortest_path(graph, 'A', 'D'))  # ['A', 'B', 'D']
