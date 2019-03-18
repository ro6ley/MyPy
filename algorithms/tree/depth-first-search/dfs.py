"""
DFS Steps:
- create and empty stack and and list of explored elements
- take the starting element and push it into the stack and add it to the visited list
- check if it has any children that are unvisited.
- if it has unvisited kids, pick one and add it to the top of the stack and the visited list
- recursively check them kids till there are no more kids or all kids are visited.
- when you get to a leaf or node with all visited kids, pop it off the top of the stack
- pick the previous node and check it's kids for unvisited ones
- rinse and repeat till you find the destination node you were looking for

"""
graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}


def dfs_recursive(graph, start, visited=[]):
    # put the starting element into our stack
    visited += [start]

    # for all the neighbors of our current node, perform dfs
    for neighbor in graph[start]:
        if neighbor not in visited:
            # current neigbor becomes new start
            visited = dfs_recursive(graph, neighbor, visited)

    return visited


def depth_first_search(graph, start):
    """
    Without recursion
    """
    visited = []
    stack = [start]

    while stack:
        # get the element at the top of the stack
        node = stack.pop()
        
        if node not in visited:
            # add it to the list of visited nodes
            visited.append(node)
            
            # get its neighbors
            neighbors = graph[node]

            # for all it's unvisited neighbors, add them to the stack
            # each of them will be visited later
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited


print(dfs_recursive(graph, 'A'))  # ['A', 'B', 'D', 'E', 'C', 'F', 'G']

print(depth_first_search(graph, 'A'))  # ['A', 'E', 'D', 'B', 'C', 'G', 'F']
